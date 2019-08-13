#imports to interactive with steem
from beem import Steem
from beem.account import Account
import steem.start as start
import time
from memes import meme_cortex

stm, account = start.steem()

def main():
    while True:
        meme_cortex(stm, account)
        time.sleep(3*60*60)

if __name__ == '__main__':
    main()