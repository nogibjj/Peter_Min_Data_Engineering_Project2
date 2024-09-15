# Mini_Project_1
[![CI/CD Pipeline](https://github.com/nogibjj/Peter_Min_Project1/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Peter_Min_Project1/actions/workflows/cicd.yml)

This is the README for my Mini Project 1 for the IDS706 - Data Engineering Systems class at Duke University.

## Overview
The purpose of this first mini project is to 
> create a Python project skeleton that contains functioning placeholders for key Python project best-practice elements.

The elements include a `Makefile`, a `README` file, a `CI/CD` workflow supported by Github Actions, and a development container consisting of a `Dockerfile` and a `devcontainer.json` configuration file.

## Elements and Associated Functionalities
### requirements.txt
Contains a list of starting or extra Python packages that needs to be installed beforehead to run the project.

### Makefile
`make all` will run all of the commands specified in the Makefile. Supported commands are:
- `make install` (install all the packages in requirements.txt)
- `make format` (format all existing Python files)
- `make lint` (lint all existing Python files)
- `make test` (tests the code specified via pytest)

### .github/workflows/cicd.yml
Specifies the name of the CI/CD workflow, condition to trigger the workflow, and a list of commands that will be run by the workflow. It is currently configured to run on every `git push` automatically, which is a feature supported by GitHub Actions.

### .devcontainer/Dockerfile && .devcontainer/devcontainer.json
These 2 files specify the configurations that create a dev container, which can be regarded as a 'sandbox' or 'playground' environment with a list of pre-built settings that you can experiment your code in without worrying about version mismatches or other hiccups.

## To Set Up
1. Clone this repo
2. Navigate to the project directory
3. Install the required packages by running `make install`

## To Use
From the project folder:
- Run `pytest` to test out the function in `main.py`
- Run `make all` to initiate the entire process from installing packages to testing
