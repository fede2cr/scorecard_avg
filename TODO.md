# TODO

## App

- [x] Create config file with GitHub token and user/org
- [x] Connect to GitHub and download list of repos from user/org in the config file
- [x] Run scorecard on all repos
- [x] Calculate average of the scores from the individual repos
- [ ] Add sleep so that this works on medium/large ammount of repos
- [ ] Add support to multiple users/repos on config file
- [ ] Save json files from scorecard. Save date of execution, and name of repo
- [ ] Web interface to select user/org and repos
- [ ] Web interface to graph worst and bess practices across al repos from user/org
- [ ] Web interface to graph practices and average across time
- [ ] Web interface to show indivudual repos' scorecard results
- [ ] Web interface to add user/repo to the config file
- [ ] Cron job to re-run all users/orgs on the config file every 15 days
- [ ] Move code to library, so that it can be reused by web and cli

## Repo

- [ ] Precommits for pylint, avoiding upload of github tokens
- [ ] Run scorecard on **this** repo and add banners

