# %%
#package imports
import numpy as np
import json
import pprint
import pandas as pd
import time

#custom file imports
import functions.steemsql as steemsql
import constants.query as q
from classes.Posts import Posts
import functions.func as func

#Specific custom imports
from constants.bidbots import update_bidbots

#updates array of bidbot acct names and loads it
update_bidbots()
bidbots = pd.read_csv('bidbots.csv')

# %%
# Queries steemsql and Updates the saved CSV file
# approx 7min query time
df = steemsql.query(q.posts_by_voter('steemflagrewards'))
sfr_voted = Posts(df)
sfr_voted.df.to_csv('comments.csv', encoding='utf-8', index=False)
#%%
sfr_voted = Posts(pd.read_csv('comments.csv'))

#%%
sfr_voted.preprocessing()
sfr_voted.df.to_csv('comments.csv', encoding='utf-8', index=False)

#%%
sfr_voted.df.head()

#%%
# for 5k posts takes about 3hrs to query
# all comments by cleaners
now = time.time()
comments = pd.DataFrame()
for i in range(len(downvoted.index)):
    comments = comments.append(steemsql.query(q.cleaner_comments_on_post(downvoted['author'][i], downvoted['permlink'][i])))
comments = comments.reset_index(drop=True)


query_time = time.time() - now
print("Query Time was: "+func.stopWatch(query_time))
print("The number of entries found: "+str(len(comments.index)))
