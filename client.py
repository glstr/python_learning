#coding=utf-8

import socket

def init_client():
    host = "localhost"
    port = 8345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall('hello world')
    data = s.recv(1024)
    s.close()
    print repr(data)

if __name__ == "__main__":
    init_client()

