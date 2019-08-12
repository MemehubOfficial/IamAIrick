from beem import Steem
from beem.account import Account
from beem.comment import Comment
from beem.rc import RC
from beem.instance import set_shared_steem_instance
from beem.nodelist import NodeList
import steem.start as start
import config
import time

def comment_on_post(url, comment_content, comment_title, comment_author):
    c = Comment(url)
    c.reply(comment_content, title=comment_title, author = comment_author, meta=None)