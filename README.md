# GitHubApi
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

GitHubApi is the sample project for listing out the PR in Github created last week.

## Tech

It uses below tools & Technologies :

- [Python] - Scripting to fetch the objects and do the manipulation !
- [Docker] - Create Docker Images 

## Prerequisite
- Generate API token in your user account which would be used to retrive the object 
## Installation
GitHubApi requires Python run time environment and Docker Cli .

Install the python modules locally

```sh
pip install requests argparse datetime timedelta
```
To Run the Python locally...


```sh
python api.py --token "yourApi Token" --projectName "npm" --repoName "npm-expansions" > outputt.htm
# Repo used to get PR objects: https://github.com/npm/npm-expansions

```

To create Docker Image 
``` sh
docker build -t api . 
```

To run Docker Image
``` sh
docker run --rm --name api api:latest --token="" --projectName="npm" --repoName="npm-expansions"
```