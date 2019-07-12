from github import Github

ACCESS_USERNAME = 'username'
ACCESS_PWD = "password"
client = Github(ACCESS_USERNAME, ACCESS_PWD, per_page=100)
user = client.get_user('ELLIOTTCABLE')
repo_list = [repo.name for repo in user.get_repos() if not repo.fork]
print(repo_list)

for j in repo_list:
    repo = user.get_repo(j)
    lang = repo.language
    print(j,':',lang)