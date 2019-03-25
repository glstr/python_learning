#!/usr/bin/python
#coding=utf-8

'''
    note: send data with socket
'''

import socket
import threading

def send_msg(host, port, data):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        address = (host, port)
	s.connect(address)
	s.sendall(data)
	data = s.recv(1024)
	s.close()
	print "received", repr(data)

def send_to_rd():
    host = "cp01-ocean-749.epc.baidu.com"
    port = 9301
    data = "hello world"
    param = (host, port, data)
    new_thread = threading.Thread(None, send_msg, 'send', param, None, None)
    new_thread.start()
    print "done"
    return new_thread

def getaddrinfo(host, port):
	print socket.getaddrinfo(host, port)

if __name__ == '__main__':
    new_thread = send_to_rd()
    new_thread.join()







        


