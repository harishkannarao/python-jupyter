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

If running jupyter notebook on a cloud machine, then use `--system` to install the depedencies in the host machines python, instead of using virtual environment

    pipenv install --dev --system

For CI environments, use `--deploy` to strictly adhere to the current `Pipfile.lock` without update it

    pipenv install --dev --system --deploy

### Run jupyter notebook

    pipenv run jupyter notebook

Open `main_notebook.py` and save it, it will auto generate `main_notebook.ipynb` file

### Run jupyter lab

    pipenv run jupyter lab

`Right Click` on `main_notebook.py` and `Open With -> Jupyter Notebook` and save it, it will auto generate `main_notebook.ipynb` file

### Run jupyter notebook as script with default arguments

    pipenv run python main_notebook.py

### Run jupyter notebook as script with arguments

    pipenv run python main_notebook.py --input 'Hello World' --number 800

### Jupytext Pairing a new Notebook

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
