#!/usr/bin/python3
#REDIS ENUM

import subprocess
import sys

try:
	host = sys.argv[1]
	parent = sys.argv[2]
	wordlist = sys.argv[3]
except:
	print ("Usage: python3 redisEnum.py host_address parent_directory wordlist")
	print ("\nEg:")
	print ("       python3 redisEnum.py 192.168.144.42 /home /usr/share/wordlists/names.txt")
	sys.exit()

with open(wordlist) as f:
    words = [line.rstrip() for line in f]

print ("Searching for valid directories in...\n")
print ("Host: " + host)
print ("Parent directory: " + parent)
print ("Using wordlist: " + wordlist)
print ("---------------------------\n")
print ("Valid directories:")
print ("---------------------------")

curr = 0;

for i in words:
	curr = curr + 1;
	progress = (1.0*curr/len(words))*100.0
	
	i = i.replace("\"", "")
	i = i.replace('\'', "")
	i = i.replace(';', "")
	i = i.replace('$', "")

	if i.startswith('/') or i.startswith('\\'):
		path = parent + i;
	else:
		path = parent + '/' + i;
		
	print (path + " [Progress: " + str(round(progress, 2)) + "%]", end='')
	command = "redis-cli -h " + host + " config set dir " + path
	out = subprocess.check_output(command, shell=True);
	
	if "OK" not in out.decode("utf-8"):
		print (' '*100,end='\r')
	else:
		print (""); 
		
print ("---------------------------")
print ("Finished.")
