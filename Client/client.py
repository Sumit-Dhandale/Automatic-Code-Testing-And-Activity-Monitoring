import socket
import os
import subprocess
from pyautogui import *
import time
#counter file read and assign counter
'''a file read and check for total records

count=1;
'''

#if prevcounter
def myconnect():
    global s
    s = socket.socket()

    host = '127.0.0.1'
    #host='192.168.43.65'
    port = 60001

    s.connect((host, port))

def senddata():
    while True:
        data = s.recv(1024)
        data1=data.decode('utf-8')
        if(data1=='scr'):
            screenshot('screenshot.png')
            filename='screenshot.png'
            f=open(filename,'rb')
            l=f.read(1024)
            while l:
                s.send(l)
                l=f.read(1024)
            f.close()
            print("\nWHOLE FILE SENT")
        if data1=='assign' :
            filename='assignmentClient.py'
        #filename='C:\\Users\hp\Desktop\TEB\client.py'
            f=open(filename,'rb')
            l=f.read(128)
            while l:
                s.send(l)
                l=f.read(128)
            f.close()
            print("\nWHOLE FILE SENT")
        if data1=="CLOSE":
            s.close()
            return;

myconnect()
senddata()
