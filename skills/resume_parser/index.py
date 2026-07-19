def parse_resume(text):

    return {

    "name":"张三",

    "skills":[
        "Python",
        "机器学习"
    ],

    "projects":[
        "RAG问答系统"
    ]

    }



if __name__=="__main__":

    print(parse_resume("resume"))
