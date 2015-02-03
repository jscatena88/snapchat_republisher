import os.path
import sys
from pysnap import get_file_extension, get_media_type, Snapchat, _map_keys

def sendSnapToStory(s, snap, path, saveImg):
    filename = '{0}.{1}'.format(snap['id'], get_file_extension(snap['media_type']))
    abspath = os.path.abspath(os.path.join(path,filename))
    if os.path.isfile(abspath):
        return
    data = s.get_blob(snap['id'])
    if data is None:
        print('well thats fucked')
        return
    s.mark_viewed(snap['id'])
    with open(abspath, 'wb') as f:
        f.write(data)

    s.send_to_story(s.upload(abspath),5,get_media_type(data))

    #if not saveImg:
        #os.remove(abspath)
    return

def addFriends(s,whitelist):
    print(whitelist)
    updates = s.get_updates(0)
    currentFriends = [friend.get('name') for friend in updates['friends']]
    print(currentFriends)
    print(updates['added_friends'])
    for friend in updates['added_friends']:
        print(friend.get('name')) 
        print(friend.get('name') in whitelist)
        print(friend.get('name') not in currentFriends)
    friends = [friend.get('name') for friend in updates['added_friends'] if (friend.get('name') in whitelist and friend.get('name') not in currentFriends)]
    for user in friends:
        print(user)
        s.add_friend(user)

    return
