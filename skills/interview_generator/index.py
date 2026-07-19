def generate_interview_questions(job_info, resume_info):
    """
    根据岗位信息与候选人信息生成面试问题
    
    Args:
        job_info: 岗位信息，包含 position, skills 等
        resume_info: 候选人信息，包含 name, skills, projects 等
    
    Returns:
        包含技术面试题和行为面试题的字典
    """
    job_skills = job_info.get("skills", [])
    candidate_skills = resume_info.get("skills", [])
    projects = resume_info.get("projects", [])
    
    technical_questions = []
    for skill in job_skills:
        technical_questions.append(f"请谈谈你在 {skill} 方面的项目经验和技术深度。")
        technical_questions.append(f"在 {skill} 项目中，你遇到过哪些技术难点，是如何解决的？")
    
    behavioral_questions = []
    for project in projects:
        behavioral_questions.append(f"请描述你在「{project}」项目中承担的角色和具体贡献。")
        behavioral_questions.append(f"在「{project}」项目中，团队是如何协作的？遇到分歧如何处理？")
    
    # 通用行为面试题
    behavioral_questions.append("请分享一次你在工作中主动推动技术改进的经历。")
    behavioral_questions.append("当项目进度紧张时，你是如何平衡质量和效率的？")
    
    return {
        "technical_questions": technical_questions[:6],
        "behavioral_questions": behavioral_questions[:4],
        "total_questions": min(len(technical_questions), 6) + min(len(behavioral_questions), 4)
    }


if __name__ == "__main__":
    job = {
        "position": "AI算法工程师",
        "skills": ["Python", "PyTorch", "机器学习"]
    }
    resume = {
        "name": "张三",
        "skills": ["Python", "机器学习"],
        "projects": ["RAG问答系统"]
    }
    result = generate_interview_questions(job, resume)
    print(result)
