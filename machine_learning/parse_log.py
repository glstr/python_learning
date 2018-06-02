#!/usr/bin/python
#coding=utf-8

'''
    @brief: This file is used to extra data from log file.
'''

import string


default_log_path = "./log/basic.log"

class LogParser:
    def __init__(self, log_path):
        self.log_path = log_path
        if (log_path == ""):
            self.log_path = default_log_path
        
    def get_data(self):
        return 



def format_str():
    print '{1},{0},{3}{2}'.format('hello','world','i','love')
    print 'name={name}, age={age}'.format(name="jim", age="8")
    print string.ascii_letters

def format_str_v2(farg, *args):
    print farg
    for arg in args:
        print arg

def formatter_usage():
    formater = string.Formatter()
    formater.parse("hello world")

def split_string():
    example = "hello world"
    result = str.split(example)
    for data in result:
        print data



