#!/usr/bin/python
#coding=utf-8

'''
    brief:
'''

import os
import os.path
import sys

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

if __name__ == '__main__':
    #print get_filelist("../data/map_img")
    if len(sys.argv) == 2:
        print sys.argv[1]
        print get_filelist(sys.argv[1])


