#!/usr/bin/python
# coding=utf-8

import socket


class Client:
    def __init__(self):
        return 

    
def send_data():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = ("10.100.57.125", 8882)
    s.connect(address)
    s.sendall("hello")
     

send_data()
