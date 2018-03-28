#!/usr/bin/python
#coding=utf-8

'''
@brief a tool for chatting in wlan
'''

import socket
import chat_tool

class ChatClient:
	def __init__(self, address, port, name):
		self.port = port
		self.name = name
		self.address = address

	def handshake(self, address, port):
		#make a connect with a frind, return a session id which can identify a session
		self.session = Session(address, port)
		return

	def break_up(self, session):
		return

	def send_msg(self, session, msg):
		return

	def get_msg(self, session):
		return

	def sessions_info(self):
		return

	def sign_in(self):
		#get online and listen connection on port
		return

	def sign_out(self):
		#get offline and stop listening
		return


	


