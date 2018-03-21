#coding=utf-8

'''
@brief a tool for chatting in wlan
'''

import socket

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

	def send_msg(self, session, msg):

	def get_msg(self, session):

	def sessions_info(self):

	def sign_in():
		#get online and listen connection on port

	def sign_out():
		#get offline and stop listening

''' 
封装数据包的打包和拆分,数据格式,二进制格式
head（8）+ msgid(8)+ data（str，json字符串）

'''
class Session:
	def __init__(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(address, port)
		self.session = s

	


