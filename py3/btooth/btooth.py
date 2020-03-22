#!/usr/bin/python
# coding=utf-8
import sys

import bluetooth

def discover():
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print("Found {} devices.".format(len(nearby_devices)))
    for addr, name in nearby_devices:
        print("  {} - {}".format(addr, name))
    return nearby_devices


def lookup_name(addr):
    print("lookup name")
    name = bluetooth.lookup_name(addr)
    print(name)


def usage():
    print("python *.py cmd option")
    print("support cmd") 


def execcmd(cmd, params):
    if cmd == "lookup_name":
        lookup_name(params)
    elif cmd == "dis":
        discover()
    else:
        usage()


class Btoother:
    def __init__(self):
        return 

    def connect(self, addr):
        return 

    def send(self, msg):
        return 

    def recv(self, msg):
        return 


if __name__ == '__main__':    
    print(len(sys.argv))

    if len(sys.argv) < 2:
        usage()
        exit(1)

    cmd = sys.argv[1]
    params = ""
    if len(sys.argv) == 3:
        params = sys.argv[2]
    
    execcmd(cmd, params)
