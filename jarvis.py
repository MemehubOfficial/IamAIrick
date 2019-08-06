# %%
#package imports
import numpy as np
import json
import pprint
import pandas as pd

#custom file imports
from functions.query_functions import query_steemsql
from constants.queries import query_posts
from constants.bidbots import update_bidbots
from constants.cleaners import *
from functions.dataframe_functions import filter_by_voter
from functions.dataframe_functions import extract_downvoter_list

# %%
# Queries steemsql and Updates the saved CSV file

df = query_steemsql(query_posts())
df.to_csv('comments.csv', encoding='utf-8', index=False)

# %%
# reads in the saved CSV file if needed

df = pd.read_csv('comments.csv')
print(len(df))

# %%
#updates array of bidbot acct names if needed

update_bidbots()
bidbots = pd.read_csv('bidbots.csv')

#%%
print(extract_downvoter_list(df))

#%%
