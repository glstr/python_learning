#!/usr/bin/python
#coding=utf-8


'''
    Brief: This file is used to operate image file, which includes 
    read and write file, make color image to gray imaga and so on.

    @date: 20180422
    @author: glstr
'''


from PIL import Image
import logging
import os

default_img_path = "img.jpg"
data_dir = "data/map_img/"

def open_image(path):
    dir = os.getcwd()
    path = dir + '/' + path
    try:
        im = Image.open(path)
    except IOError, e:
        print "error msg:", e
        return 
    else:
        im.show()
    a = im.getdata()
    width = im.width
    height = im.height
    print width, height
    print width * height
    print type(a)
    b = list(a)
    print type(b)
    print len(b)
    print type(b[0])
    print a[0]
    im.close()

def color_img_to_gray_img(file_input, file_output):
    try:
        im = Image.open(file_input).convert("L") 
    except IOError, e:
        print "err_msg:", e
    else:
        data = im.getdata()
        print "pixel number:", len(data)
        print "data type:", type(data)
        print data[0]
        im.close()
        return data

def get_gray_data_from_img(img_file):
    try:
        im = Image.open(img_file).convert("L")
    except IOError, e:
        print e
        logging.warning("[err_msg:%s]", e)
        return "hello"
    else:
        data = im.getdata()
        #im.close() 
        return data

if __name__ == '__main__':
    img_path = data_dir + "1.png"
    open_image(img_path)
