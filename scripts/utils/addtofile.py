#!/usr/bin/python3

import argparse
import json

parser = argparse.ArgumentParser(description='Utility for add a new line on a text file.')

parser.add_argument('--file', help='The file to open', required=True)
parser.add_argument('--line', help='The new line added to the file', required=True)

args = parser.parse_args()

args.line=args.line.strip()

line_exists=0

try:

	file=open(args.file, 'r')

except:
	
	print(json.JSONEncoder().encode([0, 'CANNOT_OPEN_FILE_FOR_READ']))
	exit(1)

for line in file:
	line=line.strip()
	
	if line == args.line:
		line_exists=1

file.close()

if line_exists==0:
	
	try:
	
		file=open(args.file, 'a')
		
		file.write(args.line+"\n")

		file.close()
	
	except:
		
		print(json.JSONEncoder().encode([0, 'CANNOT_OPEN_FILE_FOR_WRITE']))
		
		exit(1)
		
print(json.JSONEncoder().encode([1, 'LINE_WRITED']))

