from github import Github
import copy
import pandas as pd

def login_git(login, password):
    ACCESS_USERNAME = login
    ACCESS_PWD = password
    client = Github(ACCESS_USERNAME, ACCESS_PWD, per_page=100)
    user = client.get_user(ACCESS_USERNAME)
    if user.public_repos == 0:
        print("You don't have public repositories.")
    repo_list = [repo.name for repo in user.get_repos() if not repo.fork]
    python = 0
    cplusplus = 0
    javascript = 0
    ruby = 0
    java = 0
    c = 0
    css = 0
    html = 0
    tsql = 0
    php = 0
    cs=0
    shell = 0
    sum = 0
    for j in repo_list:
        repo = user.get_repo(j)
        lang = repo.language
        if lang == "Python":
            python += 1
            sum += 1

        elif lang == "JavaScript":
            javascript += 1
            sum += 1

        elif lang == "Ruby":
            ruby += 1
            sum += 1

        elif lang == "C++":
            cplusplus += 1
            sum += 1

        elif lang == "Java":
            java += 1
            sum += 1

        elif lang == "C":
            c += 1
            sum += 1

        elif lang == "CSS":
            css = css + 1
            sum += 1

        elif lang == "HTML":
            html += 1
            sum += 1

        elif lang == "TSQL":
            tsql += 1
            sum += 1

        elif lang == "C#":
            cs += 1
            sum += 1

        elif lang == "PHP":
            php += 1
            sum += 1

        elif lang == "Shell":
            shell += 1
            sum += 1
    res_login=[]
    if (sum > 0):
        res_login.append(python / sum)
        res_login.append(javascript / sum)
        res_login.append(ruby / sum)
        res_login.append(cplusplus / sum)
        res_login.append(java / sum)
        res_login.append(c / sum)
        res_login.append(css / sum)
        res_login.append(html / sum)
        res_login.append(tsql / sum)
        res_login.append(cs / sum)
        res_login.append(php / sum)
        res_login.append(shell / sum)
    else:
        res_login.append(python)
        res_login.append(javascript)
        res_login.append(ruby)
        res_login.append(cplusplus)
        res_login.append(java)
        res_login.append(c)
        res_login.append(css)
        res_login.append(html)
        res_login.append(tsql)
        res_login.append(cs)
        res_login.append(php)
        res_login.append(shell)
    #print(res_login)
    filename="data.csv"
    df=pd.read_csv(filename, sep=',',header=None)
    df=df.values
    prior_k = prior(res_login)
    interest_k, sum = interest(res_login, prior_k)
    sum_df=interest_df(df,prior_k)
    index=search(sum_df,interest_k,sum)
    return(recommendation(index,df))

def prior(res):
    res_log=copy.deepcopy(res)
    copy_res=copy.deepcopy(res)
    prior=[0]*len(copy_res)
    p=15
    for i in range (0,len(copy_res)):
        imax=copy_res.index(max(copy_res))
        for j in range (0,len(copy_res)):
            if ((res_log[imax])==(copy_res[j])):
                prior[j]=p
                copy_res[j]=-1
        p-=1
    return(prior)

def interest(res,prior):
    interest_k=[0]*len(res)
    sum=0
    for i in range(0,len(res)):
        interest_k[i]=res[i]*prior[i]
        sum+=interest_k[i]
    return(interest_k,sum)

def interest_df(res,prior):
    int_df=copy.deepcopy(res)
    sum_df = []
    for i in range (1,len(res)):
        sum=0
        for j in range (1, len(prior)+1):
            int_df[i][j]=float(res[i][j])*prior[j-1]
            sum+=int_df[i][j]
        sum_df.append(sum)
    return(sum_df)

def search(sum_df,res,sum):
    sum_c=copy.deepcopy(sum_df)
    index=[]
    kol=0
    for i in range (0,5):
        for j in range (0,len(sum_df)):
            idx = min(range(len(sum_c)), key=lambda p: abs(sum_c[p]-sum))
            for t in range (0,len(sum_df)):
                if (sum_c[t]==sum_df[idx] and kol<=5):
                    kol+=1
                    index.append(t+1)
                    sum_c[t]=-100
    return(index)

def recommendation(index,res):
    url=[]
    for i in range (0,len(index)):
        url.append("https://github.com/{0}".format(res[index[i]][0]))
    #print(url)
    return(url)






