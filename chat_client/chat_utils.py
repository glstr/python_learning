#!/usr/bin/python
#coding=utf-8

'''
@brief a tool for chatting in wlan
'''

import Queue
import socket
import time

msg = Queue.Queue()
exit = False

def input_msg(s, name):
    while True:
        text = raw_input(name+":")
        text = text.lstrip(name+":")
        s.sendall(text)
        if text == "end":
            print "input exit"
            return 

def rev_msg(conn):
    while True:
        data = conn.recv(1024)
        if not data: break
        msg.put(data)
        time.sleep(1)
        if data == "end":
            print "rev exit"
            return 


def display_msg(name):
    global msg
    while True:
        data = msg.get()
        if data == "end":
            print '\n'
            print "display exit"
            return 
        print name, ":", data
        


