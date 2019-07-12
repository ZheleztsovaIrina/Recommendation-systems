from github import Github
ACCESS_USERNAME =input("Please enter your Github username: ")
ACCESS_PWD = input("Please enter your account password: ")
client = Github(ACCESS_USERNAME, ACCESS_PWD, per_page=100)
user = client.get_user(ACCESS_USERNAME)
repo_list = [repo.name for repo in user.get_repos() if not repo.fork]
print(repo_list, id)

python = 0
cplusplus = 0
javascript = 0
ruby = 0
java = 0
c=0
css=0
html=0
tsql=0

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



print("Python:",python, "JS:",javascript, "Ruby:", ruby, "C++",cplusplus, "Java:",java,"C",c, "CSS:",css,"HTML",html,
      "TSQL:",tsql)

def get_users_set(self, count=50, since=20000000):
    users = self.get_users(since=since)
    users_result = []
    for user, _ in zip(users, range(count)):
        users_result.append(user.login)
    return users_result

print(get_users_set(client))

g = github.Github("nsweet29", "PASSWORD")
users = g.search_users("franky in:nsweet29")
for user in users:
    print(user.login) # print the selected users' username.
