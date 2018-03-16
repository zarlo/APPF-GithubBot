import sys
import json
from github import Github, GithubObject

config = json.load(open('config.json'))

g = Github(config['Token'])

try:
    user = g.get_organizationr(config['org'])

except:
    user = g.get_user(config['User'])

repo = user.get_repo(config['repo'])

issue = repo.create_issue(sys.argv[1], sys.argv[2], GithubObject.NotSet, GithubObject.NotSet,  sys.argv[3].split(','), sys.argv[4].split(','))

print(issue.number)