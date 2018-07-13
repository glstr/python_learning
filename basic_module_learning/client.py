#!/usr/bin/python
#coding=utf-8

'''
    note: chat tool for client
'''

import socket_func

def client_loop(host, port):
    st = socket_func.SocketTool() 
    st.connect(host, port)
    while True:
        message = raw_input("client:")
        st.send_msg(message)
        message = st.rev_msg()
        print "server:", message

if __name__ == '__main__':
    host = "localhost"
    port = 7777
    client_loop(host, port)

           

