#!/usr/bin/python3

# First, check that dont exists the user.

# Second, check that dont exists the domain

# Format of the maildir is: /home/user/domain.com/Maildir/test@email.com/

# Format of the httpdocs is : /home/user/domain.com/htdocs/

#check if exists the user

#create the user

import argparse
import json
import pwd
import crypt
import os
import sys
import subprocess
import crypt
import random
import re

parser = argparse.ArgumentParser(description='Create a new unix email account.')

parser.add_argument('--user', help='The new username using how prefix the domain', required=True)
parser.add_argument('--password', help='Password for the new account', required=False)
parser.add_argument('--directory', help='directory for the new account', required=False)
parser.add_argument('--group', help='Group for the new account', required=False)

args = parser.parse_args()

if os.geteuid()==0:

	try:
		user_check=pwd.getpwnam(args.user)
		
		print(json.JSONEncoder().encode([1, 'USER_EXISTS']))
		exit(1)
		
	except KeyError:

		try:
			directory_user="/home/"+args.user
			
			if args.directory != None:
				directory_user=args.directory
			
			group_user='' #args.user
			
			if args.group != None:
				group_user="-g "+args.group
				
			enc_passwd=''
			
			if args.password !=None:
				#enc_passwd=crypt.crypt(args.password, crypt.mksalt(crypt.METHOD_SHA512))
				ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
				chars=[]
				for i in range(16):
					chars.append(random.choice(ALPHABET))
				salt="".join(chars)
				
				enc_passwd='-p "'+crypt.crypt(args.password, '$6$'+salt+'$').replace( '$', '\$' )+'"'
				# print(enc_passwd)
			
			retcode = subprocess.call("useradd" + " -m -d "+directory_user+" "+enc_passwd+" "+group_user+" -s /usr/sbin/nologin "+args.user, shell=True)
			
			if retcode == 0:
				print(json.JSONEncoder().encode([1, 'USER_ADDED']))
				exit(0)
			elif retcode == 6:
			
				print(json.JSONEncoder().encode([0, 'NO_EXISTS_GROUP']))
				exit(1)
			
			elif retcode == 9:
				print(json.JSONEncoder().encode([0, 'USER_EXISTS']))
				exit(1)
			else:
				print(json.JSONEncoder().encode([0, 'UNKNOWN_EROR']))
				exit(1)
			
		except OSError as e:
			print(json.JSONEncoder().encode([0, 'CANNOT_ADD_USER']))
			exit(1)
			
			# pass
else:
	
	print('Need root permissions')
	exit(1)
