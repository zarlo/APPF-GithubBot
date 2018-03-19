#!/usr/bin/env python3
import sys
import json
from github import Github, GithubObject


def make_issue():
    kwargs = {
        "body": json.load(sys.stdin)['message'],
        "labels": sys.argv[2].split(',')
    }
    if "," in sys.argv[3]:
        kwargs["assignees"] = sys.argv[3].split(',')
    else:
        kwargs["assignee"] = sys.argv[3].strip()
    issue = repo.create_issue(title, **kwargs)

    print(issue.number)


def make_update(issue):
    pass

config = json.load(open('config.json'))

g = Github(config['token'])

try:
    user = g.get_organization(config['org'])
except:
    user = g.get_user(config['user'])

repo = user.get_repo(config['repo'])
title = sys.argv[1]

for iss in repo.get_issues():
    if iss.title.startswith(title):
        iss.create_comment("some data")
        sys.exit(0)

make_issue()


