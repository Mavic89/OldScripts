#!/usr/bin/python
#NetMessage Client
from socket import *
import string

def main():
	host=raw_input("Host:")
	port=input("Port:")
	s=socket(AF_INET,SOCK_STREAM)
	s.connect((host,port))
	print "Connected!"
	def nm():
		eformula=string.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890","badcfehgjilknmporqtsvuxwzyBADCFEHGJILKNMPORQTSVUXWZY!@#$%^&*/+")
		dformula=string.maketrans("badcfehgjilknmporqtsvuxwzyBADCFEHGJILKNMPORQTSVUXWZY!@#$%^&*/+","abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
		st=raw_input("Client@NetMessage>")
		print st
		enc=string.translate(st,eformula)
		if st=="exit":
			s.close()
			print "Connection closed"
		else:
			s.send(enc)
			st=None
			enc=None
			print "Waiting for server to respond...."
			encdata=s.recv(1024)
			data=string.translate(encdata,dformula)
			print "Server says ", repr(data)
			data=None
			encdata=None
			nm()
	nm()



