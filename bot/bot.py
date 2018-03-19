#!/usr/bin/env python3
import sys
import json
from github import Github, GithubObject

config = json.load(open('config.json'))

g = Github(config['token'])

try:
    user = g.get_organization(config['org'])
except:
    user = g.get_user(config['user'])

repo = user.get_repo(config['repo'])
title = sys.argv[1]

kwargs = {
    "body": sys.argv[2],
    "labels": sys.argv[3].split(',')
}
if "," in sys.argv[4]:
    kwargs["assignees"] = sys.argv[4].split(',')
else:
    kwargs["assignee"] = sys.argv[4].strip()
issue = repo.create_issue(title, **kwargs)

print(issue.number)