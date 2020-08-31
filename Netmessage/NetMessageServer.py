#!/usr/bin/python
#NetMessage server
import socket
import sys
import string

def nm(connection,server):
	eformula=string.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890","badcfehgjilknmporqtsvuxwzyBADCFEHGJILKNMPORQTSVUXWZY!@#$%^&*/+")
	dformula=string.maketrans("badcfehgjilknmporqtsvuxwzyBADCFEHGJILKNMPORQTSVUXWZY!@#$%^&*/+","abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
	print "Waiting for message from client...."
	encdata=connection.recv(4096)
	data=string.translate(encdata,dformula)
	print "Client says ", repr(data)
	data=None
	encdata=None
	xn=raw_input("Server@NetMessage>") 
	enc=string.translate(xn,eformula)
	if xn=="exit":
		connection.shutdown(socket.SHUT_RD | socket.SHUT_WR)
		connection.close()
		print "Connection closed."	
		server.close()
	else:
		connection.send(enc)
		xn=None
		nm(connection,server)	
		
def main():
	server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	address=raw_input("Server address:")
	port=input("Server port:")
	server_address=(address,port)
	print "Starting server on ", server_address
	server.bind(server_address)
	server.listen(5)
	connection, client_address =  server.accept()
	print "Connection from ", connection.getpeername()
	nm(connection,server)	

