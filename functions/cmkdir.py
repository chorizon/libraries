#!/usr/bin/python3

import os

def cmkdir(directory, user, group):
	
	uid=0
	gid=0

	try:
		os.mkdir(directory)
		
	except:

		return False

	#Change permissions
		
	try:
		
		arr_pwd=pwd.getpwnam(args.user)
		
		uid=arr_pwd.pw_uid
		
		arr_gpwd=grp.getgrnam(args.group)

		gid=arr_gpwd.gr_gid

	except:
		
		return False

	try:
	
		os.chown(directory, uid, gid)
		
	except: 
	
		return False
