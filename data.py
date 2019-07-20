from github import Github
import requests
import csv

def login():
    ACCESS_USERNAME =input("Please enter your Github username: ")
    ACCESS_PWD = input("Please enter your account password: ")
    client = Github(ACCESS_USERNAME, ACCESS_PWD, per_page=100)
    user = client.get_user(ACCESS_USERNAME)
    if user.public_repos == 0:
        print("You don't have public repositories.")

    def get_users_set(self, count=60, since=30000000):
        users = self.get_users(since=since)
        users_result = []
        for user, _ in zip(users, range(count)):
            users_result.append(user.login)
        return users_result

    get_users_d=get_users_set(client)
    print(get_repositories(get_users_d))
    print(get_users_d)

def get_repositories(get_users_d):
    result = []
    headline=['url','python','js','ruby','c++','java','c','css','html','tsql','C#','php','shell']
    for i in range(0,len(get_users_d)):
        res=[]
        python = 0
        cplusplus = 0
        javascript = 0
        ruby = 0
        java = 0
        c = 0
        css = 0
        html = 0
        tsql = 0
        cs=0
        php=0
        shell=0
        sum=0
        url = "https://api.github.com/users/{0}/repos".format(get_users_d[i])
        print(url,len(get_users_d))

        r = requests.get(url=url)
        if 'next' in r.links:
            result += get_repositories(r.links['next']['url'])

        for repository in r.json():
            lang=repository.get('language')
            if lang == "Python":
                python+=1
                sum+=1

            elif lang == "JavaScript":
                javascript +=1
                sum += 1

            elif lang == "Ruby":
                ruby +=1
                sum += 1

            elif lang == "C++":
                cplusplus +=1
                sum += 1

            elif lang == "Java":
                java +=1
                sum += 1

            elif lang == "C":
                c +=1
                sum += 1

            elif lang == "CSS":
                css = css + 1
                sum += 1

            elif lang == "HTML":
                html +=1
                sum += 1

            elif lang == "TSQL":
                tsql +=1
                sum += 1

            elif lang == "C#":
                cs +=1
                sum += 1

            elif lang == "PHP":
                php +=1
                sum += 1

            elif lang == "Shell":
                shell +=1
                sum += 1
        if (sum>0):
            res.append(get_users_d[i])
            res.append(python/sum)
            res.append(javascript/sum)
            res.append(ruby/sum)
            res.append(cplusplus/sum)
            res.append(java/sum)
            res.append(c/sum)
            res.append(css/sum)
            res.append(html/sum)
            res.append(tsql/sum)
            res.append(cs/sum)
            res.append(php/sum)
            res.append(shell/sum)
            result.append(res)
        else:
            res.append(get_users_d[i])
            res.append(python)
            res.append(javascript)
            res.append(ruby)
            res.append(cplusplus)
            res.append(java)
            res.append(c)
            res.append(css)
            res.append(html)
            res.append(tsql)
            res.append(cs)
            res.append(php)
            res.append(shell)
            result.append(res)

    print(len(result),result)
    with open('data1.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow([g for g in headline])
        for i in range(0,len(result)):
            w.writerow((result[i]))
        f.close()
    return result

login()