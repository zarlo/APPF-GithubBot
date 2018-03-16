import sys
import json
from github import Github, GithubObject

config = json.load(open('config.json'))

if config['Token'] is not None:
    g = Github(config['Token'])
else:
    g = Github(config['User'], config['Password'])
 
g.get_user(config['org']).get_repo(config['repo']).create_issue(sys.argv[1], sys.argv[2], GithubObject.NotSet, GithubObject.NotSet,  GithubObject.NotSet, sys.argv[3].split(','))
