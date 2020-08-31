#!/usr/bin/python
#Zip file password cracker
import zipfile
from threading import Thread


def extractfile(zfile, password):
    try:
        zfile.extractall(pwd=password)
        print '[+] Found password: ' + password + '\n'
    except:
        pass


def main():
	zname=raw_input("Zipfile:")
	dname=raw_input("Dictionary:")
	zfile = zipfile.ZipFile(zname)
	passfile = open(dname)
	for line in passfile.readlines():
		password = line.strip('\n')
		t = Thread(target=extractfile, args=(zfile, password))
		t.start()
