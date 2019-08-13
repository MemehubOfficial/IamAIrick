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

#steem libraries
from beem import Steem
from beem.account import Account
from beem.rc import RC
from beem.instance import set_shared_steem_instance
from beem.nodelist import NodeList
from beem.comment import Comment
from beem.vote import Vote
import steem.start as start

#logging
import logging
log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def meme_engine(stm, account):
    memes = steemsql.query(q.memes_bidbotted())

    found = False
    j=-1
    i=0
    while (i < len(memes.index) and found == False):
        try:
            v = Vote('rick.c137','@'+memes['author'][i]+'/'+memes['permlink'][i], steem_instance=stm)
        except:
            found = True
            j=i
    if j>-1:
        c = Comment('@'+memes['author'][j]+'/'+memes['permlink'][j])
        comment_content = 'Look Morty, another bidbotted meme morty. Lets downvote it Morty. Morty look, I am AI Rick!!'
        c.reply(comment_content, title='Wubba Lubba Dub Dub', author = account, meta=None)
        c.downvote(voter = account)
        print('@'+memes['author'][j]+'/'+memes['permlink'][j])
