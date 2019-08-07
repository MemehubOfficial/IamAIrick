import json

def filter_by_voter(dataframe, voters):
    #assembles an array of indexes of posts
    #where there are votes from the voters
    #then filters the dataframe by those indexs
    #returns modified dataframe

    #assemble array
    arr = []
    for i in range(len(dataframe.index)):
        for voter in voters:
            if dataframe['votes'][i].find(voter) != -1:
                arr.append(i)

    #filter dataframe
    dataframe = dataframe.iloc[arr]
    dataframe = dataframe.reset_index(drop=True)
    
    return dataframe

def extract_downvoter_list(dataframe):
    #search, compile, and return list of down voter usernames
    down_voters = []
    dic = dataframe['votes'].to_dict()
    for i in range(len(dic)):
        dic_votes = json.loads(dic[i])
        for j in range(len(dic_votes)):
            if dic_votes[j]['percent']<0:
                down_voters.append(dic_votes[j]['voter'])
    #remove duplicates
    down_voters = list(dict.fromkeys(down_voters))

    return down_voters

def downvoted_index(dataframe):
    idx = []
    posts_votes = dataframe['votes'].to_dict()
    for i in range(len(posts_votes)):
        post_votes = json.loads(posts_votes[i])
        for j in range(len(post_votes)):
            if post_votes[j]['percent'] < 0:
                idx.append(i)
            #post_vote = post_votes[j]['voter']
    return list(dict.fromkeys(idx))