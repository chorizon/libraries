#!/usr/bin/python3

import argparse
import json
import os
import pwd
import grp
import sys

parser = argparse.ArgumentParser(description='Utility for add a new dir and add permissions.')

parser.add_argument('--directory', help='The dir to create', required=True)
parser.add_argument('--user', help='The user of the directory', required=True)
parser.add_argument('--group', help='The group of the directory', required=True)
#parser.add_argument('--permissions', help='Permissions on *nix format', required=True)

args = parser.parse_args()

uid=0
gid=0

try:
	os.mkdir(args.directory)
	
except:
	
	print(json.JSONEncoder().encode([0, 'CANNOT_CREATE_THE_NEW_DIRECTORY']))
	exit(1)

#Change permissions
	
try:
	
	arr_pwd=pwd.getpwnam(args.user)
	
	uid=arr_pwd.pw_uid
	
	arr_gpwd=grp.getgrnam(args.group)

	gid=arr_gpwd.gr_gid

except:
	
	print(json.JSONEncoder().encode([0, 'CANNOT_OBTAIN_UID_OR_GID']))
	exit(1)

os.chown(args.directory, uid, gid)

print(json.JSONEncoder().encode([1, 'DIR_CREATED']))