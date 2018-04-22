#!/usr/bin/python
#coding=utf-8
'''
    @brief: This file is used to operate image file, which includes 
    read and write file, make color image to gray imaga and so on.

    @date: 20180422
    @author: glstr
'''

from PIL import Image

default_img_path = 'img.jpg'

def open_image(path):
    try:
        im = Image.open(path)
    except IOError, e:
        print "error msg:", e
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

open_image(default_img_path)
color_img_to_gray_img(default_img_path, "")
