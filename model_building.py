# %%
#package imports
import numpy as np
import json
import pprint
import pandas as pd
import time


#custom file imports
from functions.query_functions import query_steemsql, open_connection
from constants.queries import query_cleaner_comments, posts_cleaner_downvote
from constants.bidbots import update_bidbots
from functions.dataframe_functions import filter_by_voter, downvoted_index, extract_downvoter_list
from functions.stopWatch import stopWatch

#updates array of bidbot acct names and loads it
update_bidbots()
bidbots = pd.read_csv('bidbots.csv')

# %%
# Queries steemsql and Updates the saved CSV file
# approx 7min query time
df = query_steemsql(posts_cleaner_downvote())
df.to_csv('comments.csv', encoding='utf-8', index=False)

# %%
# reads in the saved CSV file if needed

df = pd.read_csv('comments.csv')

# %%
downvoted = df.iloc[downvoted_index(df)]
downvoted = downvoted.reset_index(drop=True)

#$$
pprint.pprint(downvoted)
#%%
# for 5k posts takes about 3hrs to query
# all comments by cleaners
now = time.time()
comments = pd.DataFrame()
for i in range(len(downvoted.index)):
    comments = comments.append(query_steemsql(query_cleaner_comments(downvoted['author'][i], downvoted['permlink'][i])))
comments = comments.reset_index(drop=True)


query_time = time.time() - now
print("Query Time was: "+stopWatch(query_time))
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
