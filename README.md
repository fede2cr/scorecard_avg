# scorecard_avg
Proof of concept of a tool for measuring the average of the score from OpenSSF's scorecard, from an author or org

## Usage

- Install scorecard, from docker. *Note: your user needs docker group permissions*.
- Get a GitHub token
- Modify the default config file in YAML format to define the username or project you would like to scan, and add your GitHub token to it
- Config a python enviroment for this tool
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
- Run this python script to start the analysis

```
python3 scorecard_avg.py
```

## Configuration

By default this proof-of-concept tool will only print an average of the author or the org's projects. If you'd like to get the individual results, modify the config file to get them saved in json format.

### config.yaml

```
token: 123
user: Microsoft
avg_only: true
```
