# %%
#package imports
import numpy as np
import json
import pprint
import pandas as pd
import time


#custom file imports
from functions.steemsql import steemsql
import constants.query as query
from constants.bidbots import update_bidbots
import functions.post as post
import functions.func as func
from markysBL import blacklist

#updates array of bidbot acct names and loads it
update_bidbots()
bidbots = pd.read_csv('bidbots.csv')

# %%
# Queries steemsql and Updates the saved CSV file
# approx 7min query time
df = steemsql(query.posts_cleaner_vote())
df.to_csv('comments.csv', encoding='utf-8', index=False)

# %%
# reads in the saved CSV file if needed

df = pd.read_csv('comments.csv')

# %%
downvoted = df.iloc[post.get_downvoted_index(df)]
downvoted = downvoted.reset_index(drop=True)

#%%
print(blacklist(downvoted['author'][1]))

#%%
idx = []
for i in range(len(downvoted)):
    bl = blacklist(downvoted['author'][i])
    print(bl)
    if bl == []:
        idx.append(i)
print(downvoted['author'].iloc[idx])
#%%
# for 5k posts takes about 3hrs to query
# all comments by cleaners
now = time.time()
comments = pd.DataFrame()
for i in range(len(downvoted.index)):
    comments = comments.append(steemsql(query.cleaner_comments_on_post(downvoted['author'][i], downvoted['permlink'][i])))
comments = comments.reset_index(drop=True)


query_time = time.time() - now
print("Query Time was: "+func.stopWatch(query_time))
print("The number of entries found: "+str(len(comments.index)))

#%%

pprint.pprint(comments.index)
#%%
from constants.cleaners import *

# %%
pprint.pprint(list(dict.fromkeys(comments['author'])))

#%%
cleaner_comments = pd.DataFrame()
for cleaner in cleaners:
    tmp = comments.loc[comments['author'] == cleaner]
    cleaner_comments.append(tmp)

pprint.pprint(str(len(comments)-len(cleaner_comments)))


#%%
