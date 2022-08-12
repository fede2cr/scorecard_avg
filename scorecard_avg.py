'''
Proof of concept for calculating the average of the OpenSSF's
scorecard from an author or organization
'''
import statistics
import requests
import yaml
from github import Github

with open("config.yaml", mode="r", encoding="utf-8") as file:
    config = yaml.safe_load(file)

g = Github(config['token'])

names = []
scores = []
results = {}
for repo in g.get_user(config['user']).get_repos():
    response = requests.get('https://api.securityscorecards.dev/projects/github.com/' + \
        config['user'] + '/' + repo.name)
    if response.status_code == 200:
        results[response.json()['repo']['name']] = { 'score': response.json()['score'] }
        results[response.json()['repo']['name']]['checks'] = \
            { check['name']:check['score'] for check in response.json()['checks'] }
        names.append(response.json()['repo']['name'])
        scores.append(response.json()['score'])
        if len(results) > 5: # While devel
            break
print("Average score for: " + config['user'] + " is: " + str(round(statistics.mean(scores), 2)))
print("Highest score is: " + str(round(max(scores), 2)) + " from project: " + \
    names[scores.index(max(scores))])
print("Lowest score is: " + str(round(min(scores), 2)) + " from project: " + \
    names[scores.index(min(scores))])
