# %%
#imports to interactive with steem
from beem import Steem
from beem.account import Account
from beem.blockchain import Blockchain
from beem.instance import set_shared_steem_instance
from beem.nodelist import NodeList

def main():
    #instaniate steem and blockchain from nodes
    #nobroadcast=True means on testnet and not live
    nodes = NodeList()
    nodes.update_nodes()
    s = Steem(node=nodes.get_nodes(), nobroadcast=True)
    set_shared_steem_instance(s)
    chain = Blockchain()

    #example of using acct to transfer to another account
    s.wallet.unlock("password_here")

    account = Account("account_name_here", steem_instance=s)

    account.transfer("receiving_account_name_here", "0.001", "STEEM", "Beem Programing Test")


    # example of querying the blockchain directly
    current_num = chain.get_current_block_num()
    current_num = chain.get_current_block_num()
    for operation in chain.stream(start=current_num - 99, stop=current_num):
        print(operation)

if __name__ == '__main__':
    main()