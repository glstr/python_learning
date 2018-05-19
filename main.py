#!/usr/bin/python
#coding=utf-8
import thread 

from image_client import image_tool
from basic_module_learning import thread_tool

def print_hello():
    print "hello world"

if __name__ == '__main__':
    #thread_tool.excute_in_thread()
    thread.start_new_thread(print_hello(), ())
    print type(print_hello())
    print type(print_hello)



