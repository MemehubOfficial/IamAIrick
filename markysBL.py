import urllib.request
import json

def blacklist(username):
    content = json.loads(urllib.request.urlopen("http://blacklist.usesteem.com/user/"+username).read())
    bl = content['blacklisted']
    return bl