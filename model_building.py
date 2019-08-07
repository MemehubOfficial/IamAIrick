# %%
#package imports
import numpy as np
import json
import pprint
import pandas as pd

#custom file imports
from functions.query_functions import query_steemsql
from constants.queries import posts_cleaner_downvote
from constants.queries import comment_comments
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
idx = []
posts_votes = df['votes'].to_dict()
for i in range(len(posts_votes)):
    post_votes = json.loads(posts_votes[i])
    for j in range(len(post_votes)):
        if post_votes[j]['percent'] < 0:
            idx.append(i)
        post_vote = post_votes[j]['voter']
    
pprint.pprint(list(idx))

#%%
print(len(df))

#%%
comments = pd.DataFrame()
for i in range(len(df.index)):
    comments = comments.append(query_steemsql(comment_comments(df['author'][i], df['permlink'][i])))


#%%
pprint.pprint(comments['body'])
#%%
from constants.cleaners import *

#%%
cleaner_comments = pd.DataFrame()
for cleaner in cleaners:
    tmp = comments.loc[comments['author'] == cleaner]
    cleaner_comments.append(tmp)

pprint.pprint(cleaner_comments.head())


#%%
