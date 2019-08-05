# s.wallet.unlock("Safety1st")

# account = Account("memehub", steem_instance=s)

# account.transfer("aninsidejob", "0.001", "STEEM", "Beem Programing Test")

# %%
from beem.comment import Comment
from beem.discussions import Query, Discussions_by_trending, Discussions_by_created
from beem.discussions import Query, Trending_tags
from beem import Steem
from beem.account import Account
from beem.blockchain import Blockchain
from beem.instance import set_shared_steem_instance
from beem.nodelist import NodeList
import numpy as np
import json

import pandas as pd

import logging
log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

nodes = NodeList()
nodes.update_nodes()
s = Steem(node=nodes.get_nodes(), nobroadcast=True)
set_shared_steem_instance(s)
chain = Blockchain()


# %%
current_num = chain.get_current_block_num()
ops = []
df = pd.DataFrame()
current_num = chain.get_current_block_num()
for operation in chain.stream(start=current_num - 99, stop=current_num):
    if operation['type'] == 'comment':
        if operation['json_metadata']:
            if not operation['parent_author']:
                data = json.loads(operation['json_metadata'])
                if not isinstance(data, list):
                    if not isinstance(data, str):
                        if 'tags' in data.keys():
                            if 'steem' in data['tags']:
                                opdf = pd.DataFrame.from_dict(
                                    operation, orient='index')
                                transpose = opdf.transpose()
                                df = df.append(transpose, ignore_index=True)

# %%
columns = list(df)
features = [c for c in columns if df[c].notnull().any()]

for index, data in df.iterrows():
    data_json = json.loads(data['json_metadata'])
    print(data_json.keys())

# %%
# print(list(df['type']))
#df = df.loc[df['type'] == 'comment']
df.index = pd.RangeIndex(len(df.index))
df.index = range(len(df.index))

target = ['memes']
store = pd.DataFrame(columns=['author', 'permlink'])
#columns = list(df)
#features = df.columns[df.notnull().any()].tolist()
metadata = df.loc[df['json_metadata'].notnull()]
features = ['author', 'permlink', 'json_metadata']
metadata = metadata[features]

for index, data in metadata.iterrows():
    data_json = data['json_metadata']
    if data_json:
        d = json.loads(data_json)
        if not isinstance(d, list):
            if 'tags' in d.keys():
                for tags in d['tags']:
                    for tagtarg in target:
                        if tagtarg in tags:
                            #print(author, permlink)
                            store.loc[index] = data


# %%
