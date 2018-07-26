#!/usr/bin/python
#coding=utf-8
'''
    @brief: Some functions for image.
    @author: glstr
'''

import matplotlib.image as mpimg
import requests
import os

def read_data_from_image(file_url):
    data = mpimg.imread(file_url)
    print type(data)
    return data

file_path = os.getcwd() + '/img.png'
#read_data_from_image(file_path)

default_img_path = "http://img.ivsky.com/img/tupian/pre/201801/03/caihong.jpg"
'''
    @brief: Download the image and save it in current file.
    @date: 2018-04-20
'''
def down_image(file_url):
    if file_url == "":
        file_url = default_img_path

    r= requests.get(file_url)

    dir_path = os.getcwd()
    file_path=dir_path+"/img.jpg"
    try:
        f = open(file_path, "w")
    except IOError, e:
        print "error msg:", e
    else:
        f.write(r.content)
        f.close()

    return file_path

def get_file_name(file_url):
    i = 0
    for element in file_url[::-1]:
        if element == '/':
            break
        else:
            i = i + 1
    file_name = file_url[-i:]    
    return file_name
                
def get_current_dir_path():
    print "get current path"
    print os.getcwd()
    print os.path.abspath(os.path.dirname(__file__))

if __name__ == '__main__':
    return 
