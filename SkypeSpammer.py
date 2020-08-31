#!/usr/bin/python
#Skype Spammer
#3rd Party Modules Needed:Tkinter, Skype4Py
from Tkinter import *
from threading import Thread
import Skype4Py
import time
import sys


def spammer(name,msg,delay):
	time.sleep(2)
	print "hello"
	spammer(name,msg,delay)


def spam():
	spammsg.config(fg="white")
	spambutton.config(state="disabled")
	stop.config(state="active")
	t.start()
	
		
def stop():
	bspam=False
	spambutton.config(state="active")
	stop.config(state="disabled")
	spammsg.config(fg="blue")
	
def exit0():
	sys.exit(0)
	


window=Tk()
window.wm_title("Skype Spammer")
window.resizable(width=FALSE, height=FALSE)
window.geometry("350x250")
window.configure(background="blue")
	
title=Label(text="SkypeSpammer 1.0",fg="white",bg="blue",font = "Verdana 13 bold")
title.grid(row=0,column=1)

namelabel=Label(text="Name:",fg="white",bg="blue")
namelabel.grid(row=1,column=1,sticky=W)	
nameentry=Entry(fg="blue")
nameentry.grid(row=1,column=2,sticky=E)

msglabel=Label(text="Message:",fg="white",bg="blue")
msglabel.grid(row=2,column=1,sticky=W)
msgentry=Entry(fg="blue")
msgentry.grid(row=2,column=2,sticky=E)

delaylabel=Label(text="Time Delay:",fg="white",bg="blue")
delaylabel.grid(row=3,column=1,sticky=W)
delayentry=Entry(fg="blue",)
delayentry.grid(row=3,column=2,sticky=E)
	

spambutton=Button(text="Spam!", command=lambda:spam())
spambutton.grid(row=4,column=1,sticky=W)

exitbutton=Button(text="Exit",command=exit0)
exitbutton.grid(row=4,column=2,sticky=SE)

stop=Button(text="stop",command=stop)
stop.grid(row=5,column=1,sticky=W)
stop.config(state="disabled")

spammsg=Label(text="Spamming...",fg="blue",bg="blue",font="Arial 15 bold")
spammsg.grid(row=5,column=2,sticky=E)

name=nameentry.get()
msg=msgentry.get()
delay=delayentry.get()

t=Thread(target=spammer,args=(name,msg,delay))

window.mainloop()
