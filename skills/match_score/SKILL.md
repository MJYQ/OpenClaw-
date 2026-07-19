
---

# 2. match_score/SKILL.md

```markdown
# Match Score Skill

## Skill名称

岗位匹配评分 Skill（Match Score Skill）


## Skill描述

该Skill用于比较候选人简历信息与岗位需求，
通过技能匹配、项目经验匹配等指标，
计算候选人与岗位的匹配程度。


## Skill目标

自动评估候选人是否符合岗位要求，
辅助HR快速筛选人才。


## 功能说明


主要功能：

1. 获取岗位需求信息

2. 获取候选人技能信息

3. 分析技能匹配程度

4. 计算综合评分

5. 输出推荐结果



## 输入参数(Input)


接口：

```python
calculate_match_score(
resume_info,
job_info
)
