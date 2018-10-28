#!/usr/bin/python
# coding=utf-8
'''
    @brief: image operator
    @author: glstr
'''
import sys

from PIL import Image


class ImageOpeor:
    def __init__(self, path):
        self.base_path = path
        return 
    
    def cut_average(self, path):
        im = Image.open(path) 
        width = im.width
        height = im.height
    
        print width
        print height
    
        box = (0, 0, width/2, height/2)
        box_1 = (0, height/2, width/2, height)
        box_2 = (width/2, 0, width, height/2)
        box_3 = (width/2, height/2, width, height)
    
        self.cut(box, im, "0")
        self.cut(box_1, im, "1")
        self.cut(box_2, im, "2")
        self.cut(box_3, im, "3")
        
    def cut(self, box, image, filename):
        region = image.crop(box)
        region.save(filename+'.jpg')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "param error"
    img_ope = ImageOpeor()       
    path = sys.argv[1] 
    img_ope.divide(path)

