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

# %%
# Queries steemsql and Updates the saved CSV file
# approx 7min query time
df = steemsql.query(q.memes_bidbotted())
cleaner_downvoted = Posts(df)
cleaner_downvoted.df.to_csv('csv/comments.csv', encoding='utf-8', index=False)
#%%
cleaner_downvoted = Posts(pd.read_csv('csv/comments.csv'))

#%%
cleaner_downvoted.df.head()

#%%
for i in range(len(cleaner_downvoted.df.index)):
    if cleaner_downvoted.df['replies'][i] != '[]':
        pprint.pprint(cleaner_downvoted.df['replies'][i])

#%%
cleaner_downvoted.preprocessing()
cleaner_downvoted.df.to_csv('csv/comments.csv', encoding='utf-8', index=False)

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
