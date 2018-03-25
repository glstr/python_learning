#!/usr/bin/python
# #encoding=utf-8
''' 
封装数据包的打包和拆分,数据格式,二进制格式
head（8）+ msgid(8)+ data（str，json字符串）

'''
import socket

class Session:
    buffer_size = 1024

    def __init__(self, address, port):
        self.local = (address, port)
        print self.local
        return

    def get_online(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(self.local)
        self.s.listen(1)
        self.remote_socket, address = self.s.accept()
        print "new socket: " + str(address)

    def connect(self, address, port):
        remote = (address, port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(remote)
        self.remote_socket = s
        return

    def disconnect(self):
        if self.remote_socket is None:
            return
        else:
            num = self.remote_socket.close(Session.buffer_size)


    def send_msg(self, msg):
       if self.remote_socket is None:
           print "no remote socket"
       else:
           num = self.remote_socket.send(msg)
           print str(num) + " bytes have been sent"

    def receive_msg(self):
        if self.remote_socket is None:
            print "no remote socket"
        else:

            str = self.remote_socket.recv(Session.buffer_size)
            print "message:" + str






