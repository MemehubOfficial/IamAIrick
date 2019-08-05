import pandas as pd

def update_bidbots():
    dataframe = pd.read_json('https://steembottracker.net/bid_bots')
    dataframe.name.to_csv('bidbots.cvs', encoding='utf-8', index=False)
    return print("update complete")