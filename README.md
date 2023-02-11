# python jupyter

Repository to explore python with jupyter 

## Tools Required

* python `3.7.13`
* git `latest`
* pycharm `latest`

## Commands

### Install dependencies

    pip install pipenv --upgrade

	pipenv install --dev

### Run jupyter notebook

    pipenv run jupyter notebook

### Run jupyter lab

    pipenv run jupyter lab

### Update packages to latest

    pipenv update
    
### Run tests

    pipenv run python -m pytest --html=report.html --self-contained-html
    
### Verify flake8

    pipenv run flake8 --ignore=E501 --exclude=.venv,.git # ignore max line length
    
### Create requirements.txt

    pipenv requirements > requirements.txt 

### Create requirements.txt including dev packages

    pipenv requirements --dev > requirements.txt