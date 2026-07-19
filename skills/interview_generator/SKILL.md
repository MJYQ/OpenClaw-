# Interview Generator Skill

## Skill名称

面试题生成 Skill（Interview Generator Skill）

## Skill描述

该Skill根据岗位需求和候选人信息，自动生成面试问题。

## 功能说明

1. 接收岗位信息和候选人简历信息
2. 根据岗位技能要求生成技术面试题
3. 根据候选人项目经验生成行为面试题
4. 输出结构化面试问题列表

## 输入参数(Input)

接口：
```python
generate_interview_questions(job_info, resume_info)
```

## 输出

```json
{
  "technical_questions": ["问题1", "问题2"],
  "behavioral_questions": ["问题1", "问题2"],
  "total_questions": 4
}
```
