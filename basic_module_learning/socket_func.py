#!/usr/bin/python
#coding=utf-8

'''
    note: socket tool 
'''

import socket

request = '''POST /api/1.0/rooms.info HTTP/1.1
Host: .com:8882
content-length: 14
Content-Type: application/x-www-form-urlencoded

room_id=151237'''

HOST = "cp01-pengbaojiang.epc.baidu.com"
PORT = 8882

class SocketTool:
    '''
        socket tool for message sending and reciving
    '''
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                    socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
    
    def connect(self, host, port):
        self.sock.connect((host, port))

    def bind(self, host, port):
        self.sock.bind((host, port))
        self.sock.listen(1)
        conn, addr = self.sock.accept()
        return conn

    def send_msg(self, msg):
        msg = msg + '\r\n'
        msg_len = len(msg)
        totalsent = 0
        while totalsent < msg_len:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                print "socket broken"
                return 
            totalsent = totalsent + sent

    def rev_msg(self):
        chunks = []
        byte_recd = 0
        MSG_LEN = 4096
        while byte_recd < MSG_LEN:
            chunk = self.sock.recv(min(MSG_LEN-byte_recd, 2048))
            if chunk == '':
                print "socket broken"
            chunks.append(chunk)
            byte_recd = byte_recd + len(chunk)
            if '\r\n' in chunk:
                break

        return "".join(chunks)      

def send_liveshow_request():
   socket_tool = SocketTool() 
   socket_tool.connect(HOST, PORT)
   socket_tool.send_msg(request)
   msg = socket_tool.rev_msg()
   print msg


def init_socket():
    st = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    st.connect(("cp01-pengbaojiang.epc.baidu.com", 8882))
    st.sendall(request)
    result = st.recv(4096)
    st.close()
    print result



if __name__ == '__main__':
    send_liveshow_request()
