import sys
sys.path.append("..")
from twitter_client import get_twitter_client
import json
from mongodb import *

lists = ['hs']
api = get_twitter_client()

for list in lists:
    members = api.list_members('elizurhz', list, count=200)
    with open(list + '.json', 'w') as f:
        for member in members:
            f.write(json.dumps(member._json)+"\n")   # save a backup for users
            screen_name = member.screen_name
            id_str = member.id_str
            friends_count = member.friends_count
            new_profile = ListMembersHS(
                screen_name=screen_name,
                id_str=id_str,
                friends_count=friends_count
            )
            new_profile.save()
            print("saved: %s \n" % member.screen_name)