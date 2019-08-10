import json
import panads as pd

class Post:
    '''
    Takes in a dataframe of posts.
    
    Methods:
    - filter the dataframe by a list of voters
    - retrieve vote information on a post as json array
    - retrieve downvote information on a post as json array
    - retrieve list of downvoters on a post
    '''
    def __init__(self, dataframe):
        self.df = dataframe