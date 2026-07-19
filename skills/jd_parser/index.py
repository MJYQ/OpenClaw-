def parse_job_description(text):

    result={}

    if "AI算法" in text:
        result["position"]="AI算法工程师"

    skills=[]

    for skill in ["Python","PyTorch","机器学习"]:

        if skill in text:
            skills.append(skill)


    result["skills"]=skills


    return result



if __name__=="__main__":

    print(
    parse_job_description(
    "招聘AI算法工程师，需要Python PyTorch"
    ))
