#!/usr/bin/python
#coding=utf-8

from PIL import Image

def open_image(path):
    im = Image.open(path)
    #im.show()
    a = im.getdata()
    width = im.width
    height = im.height
    print width, height
    print width * height
    print type(a)
    b = list(a)
    print len(b)


