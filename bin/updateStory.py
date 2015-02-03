#!/usr/bin/env python

"""Adds whitelisted Friends and Sends Snaps to Story

Usage:
    updateStory.py -u <username> [-p <password> -d <tmpdir> -s] WHITELIST

Options:
    -h               Show usage
    -u=<username>    Username
    -p=<password>    Password(optional, will promp if ommitted)
    -d=<tmpdir>      Where to save the snaps [default: ./]
    -s               Save the snaps permanatly in tmpdir

"""

import os.path
import sys
from getpass import getpass
from docopt import docopt
from snapchat_republisher import sendSnapToStory, addFriends
from pysnap import Snapchat

def main():
    arguments = docopt(__doc__)
    username = arguments['-u']
    if arguments['-p'] is None:
        password = getpass('Password:')
    else:
        password = arguments['-p']
    path = arguments['-d']
    save = arguments['-s']
    whiteListFile = arguments['WHITELIST']

    if not os.path.isdir(path):
        print('No such directory: {0}'.format(path))
        sys.exit(1)

    s = Snapchat()
    print(username)
    print(password)
    if not s.login(username, password).get('logged'):
        print('Invalid username or pasword')
        sys.exit(1)

    f = open(whiteListFile, 'r')
    whitelist = [line.rstrip() for line in f]
    print('would do friend things here\n');
    addFriends(s,whitelist)

    
    for snap in s.get_snaps():
        print('would send to story here\n');
        sendSnapToStory(s,snap,path,save)

    sys.exit(0)

if __name__ == '__main__':
    main()
