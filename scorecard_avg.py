'''
Proof of concept for calculating the average of the OpenSSF's
scorecard from an author or organization
'''
import subprocess
import json
import yaml
from github import Github

with open("config.yaml", mode="r", encoding="utf-8") as file:
    config = yaml.safe_load(file)

g = Github(config['token'])

results = {}
for repo in g.get_user(config['user']).get_repos():
    cmd = 'docker run -e GITHUB_AUTH_TOKEN='+config['token'] + \
          ' gcr.io/openssf/scorecard:stable --format json --repo=https://github.com/' + \
          config['user'] + '/' + repo.name
    tmp = subprocess.check_output(cmd, shell=True)
    results[repo.name] = json.loads(tmp.decode('utf-8'))

TOTAL = 0
for repo in results.keys():
    TOTAL += results[repo]['score']

print(TOTAL/len(results))
