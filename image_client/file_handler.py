#!/usr/bin/python
#coding=utf-8

'''
    brief:
'''

import os
import os.path

def get_filelist(dir_path, file_format='.png'):
    allfiles = os.listdir(dir_path)
    file_list = [] 
    for path in allfiles:
        #if path.endswith(file_format):
        if path.find(file_format) != -1:
            path = os.path.join(dir_path + path)
            file_list.append(path)
    return file_list

if __name__ == '__main__':
    #print len(get_filelist("../data/map_img"))
    print get_filelist("../data/map_img")


