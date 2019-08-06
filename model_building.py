# %%
#package imports
import numpy as np
import json
import pprint
import pandas as pd

#custom file imports
from functions.query_functions import query_steemsql
from constants.queries import posts_cleaner_downvote
from constants.bidbots import update_bidbots
from functions.dataframe_functions import filter_by_voter
from functions.dataframe_functions import extract_downvoter_list

#updates array of bidbot acct names and loads it
update_bidbots()
bidbots = pd.read_csv('bidbots.csv')

# %%
# Queries steemsql and Updates the saved CSV file

df = query_steemsql(posts_cleaner_downvote())
df.to_csv('comments.csv', encoding='utf-8', index=False)

# %%
# reads in the saved CSV file if needed

df = pd.read_csv('comments.csv')

#%%

suspects = list(dict.fromkeys(df[df['rep']<25]['author']))

#%%
print(suspects)

#%%
