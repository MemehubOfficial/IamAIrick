#%%
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

#query for posts with votes by memestagram
df = steemsql.query(q.memes_bidbotted())
memes = Posts(df)
#memes.df.to_csv('comments.csv', encoding='utf-8', index=False)



#%%
print(df.head())

#%%
