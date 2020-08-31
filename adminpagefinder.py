#!/usr/bin/python
#Admin Finder Script
#By:Jacob Shumate
import socket
from urllib import urlopen
import time

pages=["/html/Adminlogin.html","/html/adminlogin.html","/html/administratorlogin.html","/html/administrator.html","/html/admin.html","/adminlogin.php","/admin.php","/administrator.php","/administratorlogin.php","/admin1.php","/adminlogin.cfm","/adminlogin.asp"]

def main():
	website=raw_input("Url(don't forget to add 'http://'):")
	socket.setdefaulttimeout(3)
	try:
		urlopen(website+pages[0])
		print "[+]Admin page found!"+website+pages[0]
	except:
		print "[-]No admin page found."
	try:
		urlopen(website+pages[1])
		print "[+]Admin page found!"+website+pages[1]
	except:
		print "[-]No admin page found."
	try:
		urlopen(website+pages[2])
		print "[+]Admin page found!"+website+pages[2]
	except:
		print "[-]No admin page found."
	try:
		urlopen(website+pages[3])
		print "[+]Admin page found!"+website+pages[3]
	except:
		print "[-]No admin page found."
	try:
		urlopen(website+pages[4])
		print "[+]Admin page found!"+website+pages[4]
	except:
		print "[-]No admin page found."
	try:
		urlopen(website+pages[5])
		print "[+]Admin page found!"+website+pages[5]
	except:
		print "[-]No admin page found."
	try:
		urlopen(website+pages[6])
		print "[+]Admin page found!"+website+pages[6]
	except:
		print "[-]No admin page found."
	try:
		urlopen(website+pages[7])
		print "[+]Admin page found!"+website+pages[7]
	except:
		print "[-]No admin page found."
	try:
		urlopen(website+pages[8])
		print "[+]Admin page found!"+website+pages[8]
	except:
		print "[-]No admin page found."
	try:
		urlopen(website+pages[9])
		print "[+]Admin page found!"+website+pages[9]
	except:
		print "[-]No admin page found."
	try:
		urlopen(website+pages[10])
		print "[+]Admin page found!"+website+pages[10]
	except:
		print "[-]No admin page found."
	try:
		urlopen(website+pages[11])
		print "[+]Admin page found!"+website+pages[11]
	except:
		print "[-]No admin page found."






