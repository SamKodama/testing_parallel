# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.3
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import numpy as np
import os
os.chdir('..')
import src.util as util
import joblib

# %%
fnames = np.loadtxt('inputs/readMe.txt')

# %%
# joblib.Parallel(n_jobs=4)(joblib.delayed(image_flipper)(f) for f in file_list)

# %%
joblib.Parallel(n_jobs=4)(joblib.delayed(util.my_save)(f) for f in fnames)

# %%
