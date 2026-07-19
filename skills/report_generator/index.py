def generate_report(data):


    content=f"""

# 招聘分析报告


候选人数：

{data["number"]}


推荐人数：

{data["recommend"]}


"""


    with open(
    "report.md",
    "w",
    encoding="utf8"
    ) as f:

        f.write(content)



if __name__=="__main__":

    generate_report(
    {
    "number":10,
    "recommend":3
    })
