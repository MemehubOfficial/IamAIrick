from beem import Steem
from beem.account import Account
from beem.instance import set_shared_steem_instance
from beem.nodelist import NodeList
import config

def steem(test = False):
    nodes = NodeList()
    nodes.update_nodes()
    stm = Steem(node=nodes.get_nodes(), nobroadcast = test)
    set_shared_steem_instance(stm)
    stm.wallet.unlock(config.memehub_passphrase)
    account = Account('memehub', steem_instance=stm)
    return stm, account