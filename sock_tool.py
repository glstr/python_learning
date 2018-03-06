#coding=utf-8

"""
@brief send data with socket
"""
import socket

def send_msg(host, port, data):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(host, port)
	s.sendall("hello world")
	data = s.recv(1024)
	s.close()
	print "received", repr(data)

def send_func():

        


