'''
Proof of concept for calculating the average of the OpenSSF's
scorecard from an author or organization
'''
import os
import yaml
from github import Github

with open("config.yaml", mode="r", encoding="utf-8") as file:
    config = yaml.safe_load(file)

g = Github(config['token'])

results = {}
for repo in g.get_user(config['user']).get_repos():
    results[repo.name] = os.system('docker run -e GITHUB_AUTH_TOKEN='+config['token'] + ' gcr.io/openssf/scorecard:stable --repo=https://github.com/' + config['user'] + '/' + repo.name)

print(results)
