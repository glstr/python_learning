#!/usr/bin/python
#coding:utf-8

'''
    brief: Some tool for sys package. 
'''

import sys

def get_sys_argv():
    print sys.argv
    for i in sys.argv:
        print i
    for j in range(4):
        print sys.argv[j]
    return 

if __name__ == '__main__':
    get_sys_argv()
