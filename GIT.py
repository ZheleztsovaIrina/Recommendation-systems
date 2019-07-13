from github import Github
import requests

def login():
    ACCESS_USERNAME =input("Please enter your Github username: ")
    ACCESS_PWD = input("Please enter your account password: ")
    client = Github(ACCESS_USERNAME, ACCESS_PWD, per_page=100)
    user = client.get_user(ACCESS_USERNAME)
    if user.public_repos == 0:
        print("You don't have public repositories.")
    repo_list = [repo.name for repo in user.get_repos() if not repo.fork]
    print(repo_list)
    python = 0
    cplusplus = 0
    javascript = 0
    ruby = 0
    java = 0
    c = 0
    css = 0
    html = 0
    tsql = 0
    for j in repo_list:
        repo = user.get_repo(j)
        lang = repo.language
        if lang == "Python":
            python = python + 1

        elif lang == "JavaScript":
            javascript = javascript + 1

        elif lang == "Ruby":
            ruby = ruby + 1

        elif lang == "C++":
            cplusplus = cplusplus + 1

        elif lang == "Java":
            java = java + 1

        elif lang == "C":
            c = c + 1

        elif lang == "CSS":
            css = css + 1

        elif lang == "HTML":
            html = html + 1

        elif lang == "TSQL":
            tsql = tsql + 1
        print(j,':',lang)
    res_login=[]
    res_login.append(python)
    res_login.append(javascript)
    res_login.append(ruby)
    res_login.append(cplusplus)
    res_login.append(java)
    res_login.append(c)
    res_login.append(css)
    res_login.append(html)
    res_login.append(tsql)

    print("Python:",python, "JS:",javascript, "Ruby:", ruby, "C++",cplusplus, "Java:",java,"C",c, "CSS:",css,"HTML",html,
        "TSQL:",tsql,res_login)

    def get_users_set(self, count=50, since=20000000):
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
        url = "https://api.github.com/users/{0}/repos".format(get_users_d[i])
        print(url,len(get_users_d))

        r = requests.get(url=url)
        if 'next' in r.links:
            result += get_repositories(r.links['next']['url'])

        for repository in r.json():
            lang=repository.get('language')
            result.append(repository.get('name'))
            result.append(repository.get('language'))
            if lang == "Python":
                python = python + 1

            elif lang == "JavaScript":
                javascript = javascript + 1

            elif lang == "Ruby":
                ruby = ruby + 1

            elif lang == "C++":
                cplusplus = cplusplus + 1

            elif lang == "Java":
                java = java + 1

            elif lang == "C":
                c = c + 1

            elif lang == "CSS":
                css = css + 1

            elif lang == "HTML":
                html = html + 1

            elif lang == "TSQL":
                tsql = tsql + 1
        res.append(python)
        res.append(javascript)
        res.append(ruby)
        res.append(cplusplus)
        res.append(java)
        res.append(c)
        res.append(css)
        res.append(html)
        res.append(tsql)
        result.append(res)

    return result

login()

