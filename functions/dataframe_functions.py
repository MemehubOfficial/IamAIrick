import json


def filter_by_voter(dataframe, voters):
    #assembles an array of indexes of posts
    #with 
    arr = []
    for i in range(len(dataframe.index)):
        for voter in voters:
            if dataframe['votes'][i].find(voter) != -1:
                arr.append(i)

    #filter dataframe by index array
    dataframe = dataframe.iloc[arr]
    dataframe = dataframe.reset_index(drop=True)
    return dataframe

def extract_downvoter_list(dataframe):
    #search and compile list of down voters
    down_voters = []
    dic = dataframe['votes'].to_dict()
    for i in range(len(dic)):
        print(i)
        dic_votes = json.loads(dic[i])
        for j in range(len(dic_votes)):
            if dic_votes[j]['percent']<0:
                down_voters.append(dic_votes[j]['voter'])
    #%%
    #remove duplicates
    down_voters = list(dict.fromkeys(down_voters))
    return down_voters