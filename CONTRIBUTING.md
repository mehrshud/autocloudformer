# Contributing to AutoCloudFormer
Thank you for considering contributing to AutoCloudFormer, the AI-Driven Cloud Resource Optimization and Automation Platform. This document outlines the steps and guidelines for contributing to the project.

## Setup Steps
To start contributing, follow these steps:
1. **Fork** the repository to your GitHub account.
2. **Clone** the forked repository to your local machine.
3. **Install** the required dependencies using `pip install -r requirements.txt`.
4. **Configure** your AWS and Google Cloud credentials.

## Branching and Committing
### Branch Naming Convention
We use the following branch naming convention:
* `feat/` for new features
* `fix/` for bug fixes
* `docs/` for documentation changes

### Conventional Commits
We follow the Conventional Commits specification. Please format your commit messages as follows:
type(scope): brief description

body
Where `type` is one of:
* `feat` for new features
* `fix` for bug fixes
* `docs` for documentation changes
* `style` for code style changes
* `refactor` for code refactoring
* `perf` for performance improvements
* `test` for test additions or changes
* `build` for build system changes
* `ci` for continuous integration changes
* `chore` for other changes

## Pull Request Checklist
Before submitting a pull request, please ensure:
* You have followed the branching and committing guidelines
* Your code is formatted according to our code style guidelines (see below)
* You have run the tests and they pass
* You have updated the documentation if necessary
* You have included a clear and concise description of the changes

## Code Style
We use the following code styles:
* **Python**: PEP 8 with 4-space indentation
* **TensorFlow**: Follow the TensorFlow style guide
* **AWS SDK**: Follow the AWS SDK style guide
* **Google Cloud SDK**: Follow the Google Cloud SDK style guide

## Running Tests
To run the tests, use the following command:
python -m unittest discover -s tests
Make sure to install the required test dependencies using `pip install -r test_requirements.txt`.

## Reporting Bugs
To report a bug, please open an issue on the GitHub issue tracker. Please include:
* A clear and concise description of the bug
* Steps to reproduce the bug
* Any relevant error messages or logs

By following these guidelines, you can help ensure that your contributions are welcomed and integrated into the project efficiently. Thank you for your contributions to AutoCloudFormer!