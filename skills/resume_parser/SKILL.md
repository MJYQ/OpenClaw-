# Resume Parser Skill

## Skill名称

简历解析 Skill（Resume Parser Skill）


## Skill描述

该Skill用于自动读取和解析候选人简历文件，
提取候选人的基本信息、教育经历、技能信息和项目经验，
为招聘筛选Agent提供结构化数据。


## Skill目标

将非结构化简历文件转换为机器可识别的结构化信息，
提高招聘人员筛选简历的效率。


## 功能说明

主要功能：

1. 读取PDF/Word格式简历

2. 提取简历文本内容

3. 识别候选人技能

4. 提取项目经历

5. 输出标准JSON格式数据



## 输入参数（Input）

接口：

```python
parse_resume(file_path)
