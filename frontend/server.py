#!/usr/bin/env python3
"""
OpenClaw 智能招聘办公助手 — Web 前端后端服务
"""

import sys
import os
import json
import tempfile
from pathlib import Path

# 添加 Skill 路径
SKILLS_DIR = os.path.expanduser("~/.openclaw/workspace/skills")
for d in ["jd_parser", "resume_parser", "match_score", "interview_generator", "report_generator"]:
    sys.path.append(os.path.join(SKILLS_DIR, d))

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

app = Flask(__name__, static_folder="static")
CORS(app)

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(DATA_DIR, exist_ok=True)


# ==================== API 路由 ====================

@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/api/ping")
def ping():
    return jsonify({"status": "ok", "message": "招聘助手服务运行中"})


@app.route("/api/pipeline", methods=["POST"])
def run_pipeline():
    """运行完整招聘流水线"""
    from jd_parser.index import parse_job_description
    from resume_parser.index import parse_resume
    from match_score.index import calculate_match
    from interview_generator.index import generate_interview_questions
    from report_generator.index import generate_report

    jd_text = request.form.get("jd_text", "")
    files = request.files.getlist("resumes")

    if not jd_text:
        return jsonify({"error": "请提供岗位描述文本"}), 400
    if not files:
        return jsonify({"error": "请上传至少一份简历"}), 400

    # Step 1: 解析 JD
    job = parse_job_description(jd_text)

    # Step 2-3: 解析简历 + 匹配评分
    candidates = []
    raw_resumes = {}
    for f in files:
        filepath = os.path.join(UPLOAD_DIR, f.filename)
        f.save(filepath)
        resume = parse_resume(filepath)
        if "error" in resume:
            continue
        match = calculate_match(resume, job)
        raw_resumes[f.filename] = {"resume": resume, "match": match}
        candidates.append({
            "filename": f.filename,
            "name": resume["name"],
            "phone": resume["phone"],
            "education": resume["education"],
            "skills": resume["skills"],
            "projects": resume["projects"],
            "score": match["score"],
            "recommend": match["recommend"],
            "matched_skills": match["detail"]["matched_skills"],
            "missing_skills": match["detail"]["missing_skills"],
            "detail": match["detail"]
        })

    # 按评分降序排列
    candidates.sort(key=lambda c: c["score"], reverse=True)

    # Step 4: 面试题（仅推荐候选人）
    interview_data = {}
    for c in candidates:
        if "推荐" in c["recommend"]:
            resume_info = {
                "skills": c["skills"],
                "projects": c["projects"]
            }
            questions = generate_interview_questions(job, resume_info)
            interview_data[c["name"]] = questions

    # Step 5: 生成报告
    report_input = {
        "project": f"招聘：{job['position']}",
        "number": len(candidates),
        "recommend": len([c for c in candidates if "推荐" in c["recommend"]]),
        "candidates": [{
            "name": c["name"],
            "score": c["score"],
            "level": c["recommend"],
            "recommend": c["recommend"],
            "matched_skills": c["matched_skills"],
            "missing_skills": c["missing_skills"]
        } for c in candidates]
    }
    report = generate_report(report_input)

    result = {
        "job": job,
        "candidates": candidates,
        "interviews": interview_data,
        "report_path": report["path"],
        "report_content": report["content"]
    }

    return jsonify(result)


@app.route("/api/quick_test", methods=["GET"])
def quick_test():
    """快速测试 - 用内置样本数据跑一遍"""
    from jd_parser.index import parse_job_description
    from resume_parser.index import parse_resume, extract_skills, extract_name, extract_projects, extract_education
    from match_score.index import calculate_match
    from interview_generator.index import generate_interview_questions
    from report_generator.index import generate_report

    # 样本 JD
    sample_jd = """招聘岗位：AI算法工程师

岗位要求：
1. 本科及以上学历，计算机相关专业
2. 熟悉Python编程语言
3. 熟悉PyTorch深度学习框架
4. 掌握机器学习、深度学习基础知识
5. 了解Transformer、RAG等大模型相关技术

工作经验：1-3年

期望技能：Python PyTorch 机器学习 深度学习 Transformer RAG"""

    # 样本简历1 — 匹配
    sample_resume_1 = """姓名：张明远
电话：13800138000
邮箱：zhangmy@example.com
学校：上海交通大学
专业：计算机科学与技术
学历：硕士

技能：Python PyTorch TensorFlow Docker Kubernetes 机器学习 深度学习 NLP RAG

项目经验：
1. 智能客服RAG系统 - 基于LangChain构建企业级RAG问答系统
2. 图像分类模型优化 - 使用PyTorch实现模型部署
3. 推荐系统平台 - 基于深度学习的混合推荐"""

    # 样本简历2 — 不匹配
    sample_resume_2 = """姓名：李小明
电话：13912345678
邮箱：lixm@example.com
学校：武汉大学
专业：市场营销
学历：本科

技能：Excel PPT SPSS

项目经验：
1. 市场调研项目 - 数据分析与报告
2. 品牌推广方案"""

    job = parse_job_description(sample_jd)

    resumes = [
        (sample_resume_1, "简历1-张明远.txt"),
        (sample_resume_2, "简历2-李小明.txt")
    ]

    candidates = []
    for text, fname in resumes:
        # 模拟解析
        resume = {
            "name": fname.replace("简历1-", "").replace("简历2-", "").replace(".txt", ""),
            "phone": extract_name(text),
            "education": extract_education(text),
            "skills": extract_skills(text),
            "projects": extract_projects(text)
        }
        # 修正姓名
        resume["name"] = "张明远" if "张明远" in fname else "李小明"
        match = calculate_match(resume, job)
        candidates.append({
            "filename": fname,
            "name": resume["name"],
            "phone": resume.get("phone", "未识别"),
            "education": resume["education"],
            "skills": resume["skills"],
            "projects": resume["projects"],
            "score": match["score"],
            "recommend": match["recommend"],
            "matched_skills": match["detail"]["matched_skills"],
            "missing_skills": match["detail"]["missing_skills"],
        })

    candidates.sort(key=lambda c: c["score"], reverse=True)

    interview_data = {}
    for c in candidates:
        if "推荐" in c["recommend"]:
            questions = generate_interview_questions(job, c)
            interview_data[c["name"]] = questions

    return jsonify({
        "job": job,
        "candidates": candidates,
        "interviews": interview_data,
        "demo": True
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"🚀 招聘助手前端服务启动: http://127.0.0.1:{port}")
    print(f"📂 上传目录: {UPLOAD_DIR}")
    app.run(host="127.0.0.1", port=port, debug=True)
