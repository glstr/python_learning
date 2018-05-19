#!/usr/bin/python
#coding:utf-8


'''
    brief: Some tools for daily days
'''


import os
import os.path

def ping_url(url):
    print url
    target = "ping "+url
    print target

    os.system(target)
    fp = os.popen("ping"+url+"-t")
    fpread = fp.read()
    print type(fpread)
    print len(fpread)

def get_ip_config():
    command = "ipconfig"
    os.system(command)

def exe_command(command):
    os.system(command)


def how_to_open_file():
    file_path = "example"
    with open(file_path) as f:
        for line in f:
            print line

def get_all_file_from_dir(dir_path):
    if os.path.isdir(dir_path):    
        files = os.listdir(dir_path)
    else:
        print dir
    print files

get_all_file_from_dir("/usr/")





