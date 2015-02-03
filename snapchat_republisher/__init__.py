import os.path
import sys
from pysnap import get_file_extension, get_media_type, Snapchat, _map_keys

def sendSnapToStory(s, snap, path, saveImg,verbose):
    filename = '{0}.{1}'.format(snap['id'], get_file_extension(snap['media_type']))
    abspath = os.path.abspath(os.path.join(path,filename))
    if os.path.isfile(abspath):
        return
    data = s.get_blob(snap['id'])
    if data is None:
        return
    if verbose:
        print('Valid, moving forward')
        print('Marking snap viewed')
    #s.mark_viewed(snap['id'])
    with open(abspath, 'wb') as f:
        f.write(data)

    if verbose:
        print('Sending snap to story')
    #s.send_to_story(s.upload(abspath),5,get_media_type(data))

    if not saveImg:
        if verbose:
            print('Removing tmp file')
        os.remove(abspath)
    return

def addFriends(s,whitelist,verbose):
    updates = s.get_updates(0)
    currentFriends = [friend.get('name') for friend in updates['friends']]
    if verbose:
        for friend in updates['added_friends']:
            print('Friend: {0}'.format(friend.get('name'))) 
            print('\tIs in the whitelist: {0}'.format(friend.get('name') in whitelist))
            print('\tHas already been approved: {0}'.format(friend.get('name') not in currentFriends))
    friends = [friend.get('name') for friend in updates['added_friends'] if (friend.get('name') in whitelist and friend.get('name') not in currentFriends)]
    for user in friends:
        if verbose:
            print('Attempting to approve friendship with {0}'.format(user))
        #s.add_friend(user)

    return
