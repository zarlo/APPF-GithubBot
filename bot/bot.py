import sys
import json
from github import Github, GithubObject

config = json.load(open('config.json'))

if config['Token'] is not None:
    g = Github(config['Token'])
else:
    g = Github(config['User'], config['Password'])

if config['org'] is not None:
    user = g.get_user(config['User'])
else:
    user = g.get_organizationr(config['org'])

repo = user.get_repo(config['repo'])

repo.create_issue(sys.argv[1], sys.argv[2], GithubObject.NotSet, GithubObject.NotSet,  sys.argv[3].split(','), sys.argv[4].split(','))
