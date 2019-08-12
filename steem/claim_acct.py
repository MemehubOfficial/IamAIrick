from beem import Steem
from beem.account import Account
from beem.rc import RC
from beem.instance import set_shared_steem_instance
from beem.nodelist import NodeList
import steem.start as start
import time

def claim_acct_rc(steem_instance, steem_account):
    rc = RC(steem_instance=steem_instance)
    current_costs = steem_instance.get_rc_cost(rc.get_resource_count(tx_size=250, execution_time_count = 10000, new_account_op_count=1))
    current_mana = steem_account.get_rc_manabar()["current_mana"]
    last_mana = current_mana
    print("Current costs %.2f G RC - current mana %.2f G RC" % (current_costs / 1e9, current_mana / 1e9))
    if current_costs + 10 < current_mana:
        steem_instance.claim_account(steem_account)
        time.sleep(10)
        steem_account.refresh()
        current_mana = steem_account.get_rc_manabar()["current_mana"]
        print("Account claimed and %.2f G RC paid." % ((last_mana - current_mana) / 1e9))
        last_mana = current_mana
    else:
        print("Not enough RC for a claim!")

def create_acct_rc(new_acct_name, new_acct_password, test = False):
    stm, account = start.steem()
    stm.create_claimed_account(new_acct_name, creator=account, password=new_acct_password)