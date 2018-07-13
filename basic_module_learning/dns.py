#!/usr/bin/python
#coding=utf-8

import socket
import sys

def get_ip_by_name(url):
    return socket.gethostbyname(url)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "parameter error"
    else:
        print get_ip_by_name(sys.argv[1])


