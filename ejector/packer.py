#!/usr/bin/python
# coding=utf-8

import struct
import sys


class Packer:
    def __init__(self):
        return
    
    def pack_num(self, number):
        return struct.pack('h', number) 


if __name__ == '__main__':
    packer = Packer()
    input = int(sys.argv[1])
    ret = struct.pack('i', 34)
    print ret.decode()
