def calculate_match(resume,job):


    score=0


    for skill in resume["skills"]:

        if skill in job["skills"]:

            score+=50


    return {

    "score":score,

    "recommend":
    "推荐面试"

    }


