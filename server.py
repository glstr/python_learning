#!/usr/bin/python
# #encoding=utf-8

import socket
import sys

def init_server():
    host = ""
    port = 8345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    conn, addr = s.accept()
    print 'Connect by', addr
    while 1:
        data = conn.recv(1024)
        if not data: break
        conn.sendall(data)
        print data
    conn.close()

if __name__ == "__main__":
    init_server()
