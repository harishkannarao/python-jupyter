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

Open `main_notebook.py` and save it, it will auto generate `main_notebook.ipynb` file

### Run jupyter lab

    pipenv run jupyter lab

`Right Click` on `main_notebook.py` and `Open With -> Jupyter Notebook` and save it, it will auto generate `main_notebook.ipynb` file

### Jupytext Pairing

#### With Jupyter Notebook

* Create a new notebook with `ipynb` extension and give a name
* File -> Jupytext -> Tick Pair Notebook with percent Script
* File -> Jupytext -> Tick Autosave Notebook
* Click Save
* Now the Notebook is paired with Jupytext plugin

#### With Jupyter Lab

* Create a new notebook with `ipynb` extension and give a name
* View -> Active Command Palette
* Search Pair Notebook with percent Script
* Select or Tick Pair Notebook with percent Script
* Click Save
* Now the Notebook is paired with Jupytext plugin

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
