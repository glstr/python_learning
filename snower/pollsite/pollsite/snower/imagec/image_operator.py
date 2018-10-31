#!/usr/bin/python
# coding=utf-8
'''
    @brief: image operator
    @author: glstr
'''
import sys

from PIL import Image


class ImageOpeor:
    def __init__(self):
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
    
        self.cut_f(box, im, "0")
        self.cut_f(box_1, im, "1")
        self.cut_f(box_2, im, "2")
        self.cut_f(box_3, im, "3")
        
    def cut_f(self, box, filename):
        im = Image.open(self.base_path)
        region = im.crop(box)
        region.save(filename+'.jpg')

    def divide_to_four(self, path):
        im = Image.open(path) 
        width = im.width
        height = im.height

        box_0 = (0, 0, width/2, height/2)
        box_1 = (0, height/2, width/2, height)
        box_2 = (width/2, 0, width, height/2)
        box_3 = (width/2, height/2, width, height)
        boxes = [box_0, box_1, box_2, box_3]
        imgs = []
        for box in boxes:
            c_img = im.crop(box)
            imgs.append(c_img)
        return imgs


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "param error"
    img_ope = ImageOpeor()       
    path = sys.argv[1] 
    img_ope.divide(path)

