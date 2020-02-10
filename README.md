# Flake8 Problem Matcher/Annotations

Adds error and warning problem matchers for [flake8](https://flake8.pycqa.org/) checks on Python projects.
This action only generates [Github Annotations](https://developer.github.com/v3/checks/runs/#annotations-object) from flake8 output, it does *not* run flake8.

## Inputs

No inputs needed.

## Outputs

Only Github Annotations are generated from the Checks output, no other output is generated.

## Example usage

Add the following section to your Github workflow YAML in the step running flake8 before executing flake8:

```yaml
    - name: Setup flake8 annotations
      uses: rbialon/flake8-annotations
```

Example usage with [Githubs Python starter workflow](https://github.com/actions/starter-workflows/blob/master/ci/python-app.yml):

```yaml
name: Python application

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.8
      uses: actions/setup-python@v1
      with:
        python-version: 3.8
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Setup flake8 annotations
      uses: rbialon/flake8-annotations
    - name: Lint with flake8
      run: |
        pip install flake8
        # stop the build if there are Python syntax errors or undefined names
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    - name: Test with pytest
      run: |
        pip install pytest
        pytest
```
