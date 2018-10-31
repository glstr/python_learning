#!/usr/bin/python
# coding=utf-8

'''
    @brief: common function just for image package
'''

import logging
import os
import os.path
import random

REDIS_ERROR = "redis error"
READ_DATA_ERROR = "read data error"


def write_log(log):
    print '[', log, ']' 


def loging_init():
    logging.basicConfig(
            filename="./log/basic.log", level=logging.DEBUG, 
            format='[%(asctime)s] [%(filename)s] [%(funcName)s] %(message)s') 


def get_filelist(dir_path, file_format='.png'):
    allfiles = []
    with open(dir_path+"index.txt") as f:
        for line in f:
            newline = line.rstrip('\n')
            allfiles.append(newline)
    file_list = [] 
    for path in allfiles:
        # if path.endswith(file_format):
        if path.find(file_format) != -1:
            path = os.path.join(dir_path + path)
            path = os.path.abspath(path)
            file_list.append(path)
    return file_list


def get_filename(file_path):
    strs = file_path.split('/')
    return strs[-1] 


def random_num(min_num, max_num):
    return random.randint(min_num, max_num)


def parse_param(param):
    return param.split(",")
