#!/usr/bin/env python

"""Adds whitelisted Friends and Sends Snaps to Story

Usage:
    updateStory.py -u <username> [-p <password> -d <tmpdir> -sv] WHITELIST

Options:
    -h               Show usage
    -u=<username>    Username
    -p=<password>    Password(optional, will promp if ommitted)
    -d=<tmpdir>      Where to save the snaps [default: ./]
    -s               Save the snaps permanatly in tmpdir
    -v               Verbose

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
    verbose = arguments['-v']
    whiteListFile = arguments['WHITELIST']

    if not os.path.isdir(path):
        print('No such directory: {0}'.format(path))
        sys.exit(1)

    s = Snapchat()
    if verbose:
        print('Attempting to log in as {0}.'.format(username))
    if not s.login(username, password).get('logged'):
        print('Invalid username or pasword')
        sys.exit(1)

    if verbose:
        print('Attempting to open whitelist file at {0}.'.format(whiteListFile))
    with open(whiteListFile, 'r') as f:
        whitelist = [line.rstrip() for line in f]
        if verbose:
            print('Succesfully read whitelist and extracted {0} lines. Attempting to handle friends'.format(len(whitelist)))
        #sys.exit(0)
        addFriends(s,whitelist,verbose)

    
    for snap in s.get_snaps():
        if verbose:
            print('Working with snap')
        sendSnapToStory(s,snap,path,save,verbose)

    sys.exit(0)

if __name__ == '__main__':
    main()
