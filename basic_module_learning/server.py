#!/usr/bin/python
#coding=utf-8

'''
    note: chat tool for server
'''

import socket_func

def server_loop(host, port):
    st = socket_func.SocketTool()
    new_st = st.bind(host, port)
    new_st_tool = socket_func.SocketTool(new_st)
    while True:
        msg = new_st_tool.rev_msg()
        print "client:", msg
        msg = raw_input("server:")
        new_st_tool.send_msg(msg)


if __name__ == '__main__':
    host = "localhost"
    port = 7777
    server_loop(host, port)

