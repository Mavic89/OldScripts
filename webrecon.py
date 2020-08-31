#!/usr/bin/python
import sys
import time
import os
from socket import *
from threading import Thread

def pscan(host):
	try:
		print "Checking if nmap is installed for faster/better results."
		os.system(nmap)
		time.sleep(1)
		print "Scanning...."
		time.sleep(1)
		os.system("nmap -sV "+host)
	except:
		print "Nmap not installed. Moving to default."
		time.sleep(1)
		print "Scanning for open tcp ports 0-2000"
		h=gethostbyname(host)
		for port in(0,2000):
			try:
				s=socket(AF_INET,SOCK_STREAM)
				s.connect(h,port)
				s.send("Hello.")
				s.recv(12)
				print "-Port "+port+" is open."
			except:
				print ""

			
def webrecon():
	host=raw_input("Website:")
	print "Gathering information for ",host
	time.sleep(1)
	print "Checking if "+host+" is online....."
	try:
		ip=gethostbyname(host)
		time.sleep(1)
		print host+" is online!"
	except:
		time.sleep(1)
		print "Cannot resolve ",host
		sys.exit(0)
	time.sleep(1)
	print "Finding i.p. adress of ",host
	time.sleep(1)
	print "I.p. Adress for "+host+" is "+ip
	time.sleep(1)
	print "Finding other Dns servers for ", host
	time.sleep(1)
	os.system("nslookup "+host)
	time.sleep(1)
	print "Finding whois information for ",host
	time.sleep(1)
	try:	
		import whois
		whois.whois(host)
	except:
		print "Python whois module not found. Trying through the command line."
		os.system("whois "+host)
	else:
		print "No whois tool found on system. Skipping this step. Do it yourself at http://whois.net"
	time.sleep(3)
	print "Scanning "+host+" for open ports. This may take a while....."
	time.sleep(1)
	pscan(host)
		
def main():
	print """
	 _    _ _________________ _____ _____ _____ _   _ 
	| |  | |  ___| ___ \ ___ \  ___/  __ \  _  | \ | |
	| |  | | |__ | |_/ / |_/ / |__ | /  \/ | | |  \| |
	| |/\| |  __|| ___ \    /|  __|| |   | | | | . ` |
	\  /\  / |___| |_/ / |\ \| |___| \__/\ \_/ / |\  |
	 \/  \/\____/\____/\_| \_\____/ \____/\___/\_| \_/

	-Website reconnaissance tool
	

	"""
	t=Thread(target=webrecon)
	t.start()
main()
