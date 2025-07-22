# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
#
# # Using argparse in Jupyter
#
# Developing in Jupyter with intention to use in cmd line script later
#

# %%
import sys
print(sys.argv)

if 'kernel' in ' '.join(sys.argv):
    sys.argv = ['']   # important to put '' when executed from Jupyter otherwise it will complain

# %%
import argparse

# %%
parser = argparse.ArgumentParser()

parser.add_argument("--input", type=str, help="input helper", default='sometext')
parser.add_argument("--number", type=int, help="some number", default=600)
parser.add_argument("--boolean", type=bool, help="some boolean", default=False)
args = parser.parse_args()

# %%
# convert the parsed arguments as python dictionary dict()
dict_args = vars(args)

# %%
print("Args input, number and boolean:", dict_args['input'], " ", dict_args['number'], dict_args['boolean'])

# %%
dict_args['input'] = "a new input text!!"
print("arguments has changed: ", dict_args)

# %%
