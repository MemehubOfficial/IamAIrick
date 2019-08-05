# %%
import numpy as np
import json
import pprint
import pandas as pd
from functions.query_functions import query_steemsql
from constants.queries import *
from constants.bidbots import update_bidbots
from constants.cleaners import *

# %%
# Queries Updates the saved CSV file
df = query_steemsql(query_posts)
df.to_csv('comments.cvs', encoding='utf-8', index=False)

# %%
# reads in the saved CSV file
df = pd.read_csv('comments.cvs')
print(len(df))

# %%
#updates bidbot array if needed
update_bidbots()
bidbots = pd.read_csv('bidbots.cvs')

#%%
#assembles an array of indexes by bidbot votes
arr = []
for i in range(len(df.index)):
    for bot in bidbots:
        if df['votes'][i].find(bot) != -1:
            arr.append(i)

print(arr)

#%%
#filter dataframe by bidbot index array
df = df.iloc[arr]
df = df.reset_index(drop=True)
print(df.head())

#%%
#assemble array of indexes by cleaner votes
arr = []
for i in range(len(df.index)):
    for cleaner in cleaners:
        if df['votes'][i].find(cleaner) != -1:
            arr.append(i)

print(arr)

#%%
#filter dataframe by cleaner index array
df = df.iloc[arr]
df = df.reset_index(drop=True)
print(df.head())

#%%

print(df['votes'])

#%%
#search downvoters
down_voters = []
dic = df['votes'].to_dict()
print(dic[2334])
idx = []
for i in range(len(dic)):
    print(i)
    dic_votes = json.loads(dic[i])
    for j in range(len(dic_votes)):
        if dic_votes[j]['percent']<0:
            down_voters.append(dic_votes[j]['voter'])
            idx.append(i)
#%%
#remove duplicates
dv = list(dict.fromkeys(down_voters))
indices = list(dict.fromkeys(idx))
pprint.pprint(dv)
pprint.pprint(indices)


#%%
