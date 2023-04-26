# verify-commit-message-action
## GitHub action to verify the commit messages

While we commit our code adding required commit message helps others understand the code and why its being added.
This GitHub Action will help in validating the commit message as per the regex value passed
The job will pass if the regex matches or exits with return code 1

### Input Variables
Required:

`regex:` Pattern used to match with the commit message (python re format)


### example use case
### adding this action to a workflow file which checks the commit message for jira story id
```yaml
on: [push]

jobs:
  commit-message-check-job:
    runs-on: ubuntu-latest
    name: commit-message-validation
    steps:
      - uses: actions/checkout@v3
      - id: foo
        uses: uptownaravi/verify-commit-message-action@v2
        with:
          regex: '(?i)jira-[0-9]{3,}'
```

