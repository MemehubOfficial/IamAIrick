import pandas as pd

#creates an array of bidbot names
def bidbots():
    dataframe = pd.read_json('https://steembottracker.net/bid_bots')
    bots = dataframe["name"].tolist()
    bots.append('smartmarket')
    return bots