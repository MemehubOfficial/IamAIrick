import pandas as pd

#creates an array of bidbot names
def bidbots():
    dataframe = pd.read_json('https://steembottracker.net/bid_bots')
    return dataframe["name"].tolist()