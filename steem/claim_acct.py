from beem import Steem
from beem.account import Account
from beem.rc import RC
from beem.instance import set_shared_steem_instance
from beem.nodelist import NodeList
import steem.start as start
import time

def claim_acct_rc(test = False):
    stm, account = start.steem(test)
    rc = RC(steem_instance=stm)
    current_costs = stm.get_rc_cost(rc.get_resource_count(tx_size=250, execution_time_count = 10000, new_account_op_count=1))
    current_mana = account.get_rc_manabar()["current_mana"]
    last_mana = current_mana
    print("Current costs %.2f G RC - current mana %.2f G RC" % (current_costs / 1e9, current_mana / 1e9))
    if current_costs + 10 < current_mana:
        stm.claim_account(account)
        time.sleep(10)
        account.refresh()
        current_mana = account.get_rc_manabar()["current_mana"]
        print("Account claimed and %.2f G RC paid." % ((last_mana - current_mana) / 1e9))
        last_mana = current_mana
    else:
        print("Not enough RC for a claim!")

def create_acct_rc(new_acct_name, new_acct_password, test = False):
    stm, account = start.steem(test)
    stm.create_claimed_account(new_acct_name, creator=account, password=new_acct_password)