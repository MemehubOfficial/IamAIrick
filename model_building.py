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
memes = Posts(df)
memes.df.to_csv('csv/comments.csv', encoding='utf-8', index=False)
#%%
memes = Posts(pd.read_csv('csv/comments.csv'))

#%%
memes.df.head()
