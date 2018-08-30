#!/usr/bin/python
#coding=utf-8

'''
    @brief: common function just for image package
'''

import os
import os.path
import sys

REDIS_ERROR = "redis error"

def write_log(log):
    print '[', log, ']' 

def get_filelist(dir_path, file_format='.png'):
    allfiles = []
    with open(dir_path+"index.txt") as f:
        for line in f:
            newline = line.rstrip('\n')
            allfiles.append(newline)
    file_list = [] 
    for path in allfiles:
        #if path.endswith(file_format):
        if path.find(file_format) != -1:
            path = os.path.join(dir_path + path)
            path = os.path.abspath(path)
            file_list.append(path)
    return file_list


