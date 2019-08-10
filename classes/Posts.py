import json
import numpy as np
from markysBL import blacklist
import pandas as pd

class Posts:
    '''
   
    '''
    def __init__(self, dataframe):
        self.df = dataframe
        self.downvoted = 0
    
    def preprocessing(self):
        '''

        '''
        idx=[]
        self.df['blacklisted'] = pd.Series()
        for i in range(len(self.df.index)):

            #add a blacklist column of json string data 
            author = self.df.at[i,'author']
            bl = np.asarray(blacklist(author))
            self.df.loc[i,'blacklist'] = str(bl)

            #adds a tags column of json string data
            data = self.df['json_metadata'][i]
            json_metadata = json.loads(data)
            tags = json_metadata['tags']
            self.df.at[i, 'tags'] = str(tags)

            #convert votes json string to json
            s = self.df['votes'][i]
            json_acceptable_string = s.replace("'", "\"")
            votes = json.loads(json_acceptable_string)
            self.df.at[i, 'votes'] = votes

            #Check if post has a downvote
            dvFound = False
            j = 0
            while j < max(range(len(votes))) and not dvFound:
                if votes[j]['percent']<0:
                    dvFound = True
                    self.downvoted+=1
                    idx.append(i)
                j+=1
            
            #add bool column for if post has a downvote
            if dvFound:
                self.df.at[i, 'downvoted'] = True
            else:
                self.df.at[i, 'downvoted'] = False

        #set instance variable for index array of post with downvotes
        self.downvotedIndex = idx

    def filter_by_voters(self, voters):
        '''

        '''

        #assemble index array
        arr = []
        for i in range(len(self.df.index)):
            for voter in voters:
                if self.df['votes'][i].find(voter) != -1:
                    arr.append(i)

        #filter dataframe by index array
        dataframe = self.df.iloc[arr]
        dataframe = dataframe.reset_index(drop=True)
        
        return dataframe

    def get_downvotes(self, author, permlink):
        '''

        '''
        votes = self.get_votes(author, permlink)
        downvotes = []
        for i in range(len(votes)):
            if votes[i]['percent']<0:
                downvotes.append(votes[i])
        return downvotes

    def get_downvoters(self, author, permlink):
        '''

        '''
        downvotes = self.get_downvotes(author, permlink)
        downvoters = []
        for i in range(len(downvotes)):
            if downvotes[i]['percent']<0:
                downvoters.append(downvotes[i]['voter'])
        downvoters = list(dict.fromkeys(downvoters))
        return downvoters