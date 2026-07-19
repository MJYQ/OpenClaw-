# OpenClaw智能招聘办公助手


## 1. 项目简介

OpenClaw智能招聘办公助手是一套基于多Agent协同架构的企业招聘自动化系统。

系统通过岗位分析Agent、简历筛选Agent、面试管理Agent以及报告生成Agent，实现招聘流程中的信息分析、候选人筛选、面试辅助和数据统计。


## 2. 项目功能

### （1）岗位分析

自动解析企业岗位JD：

- 岗位名称
- 技术要求
- 工作经验
- 技能关键词


### （2）简历筛选

支持：

- PDF简历读取
- Word简历读取
- 技能匹配分析


输出：

- 匹配评分
- 推荐等级


### （3）面试辅助

根据岗位和候选人信息：

- 自动生成面试问题
- 提供面试参考


### （4）招聘报告

自动生成：

- 候选人统计
- 招聘进度
- 分析报告



## 3. 系统架构

用户

↓

OpenClaw Gateway

↓

多个Agent

↓

Skill能力模块

↓

数据库


## 4. Agent列表

|Agent|功能|
|-|-|
|Job Agent|岗位分析|
|Resume Agent|简历筛选|
|Interview Agent|面试管理|
|Report Agent|报告生成|



## 5. 运行方式


安装依赖：

```bash
pip install -r requirements.txt
