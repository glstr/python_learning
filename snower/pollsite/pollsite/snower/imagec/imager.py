#!/usr/bin/python
# coding=utf-8

import json
import sys

from PIL import Image
from pprint import pprint

import logging
import mutual_infor as mi


'''
    note: Imager 
'''

default_img_path = "img.jpg"
data_dir = "data/map_img/"


class Imager:
    def __init__(self, path):
        self.path = path        
        self.entropy = 0.0
        self.width = 0
        self.height = 0
        self.is_process = False

    def load(self):
        try:
            im = Image.open(self.path)
        except IOError, e:
            print "error msg:", e
            return 
        self.data = im.getdata()
        self.width = im.width
        self.height = im.height
        im.close()

    def display(self):
        data = {}        
        data["path"] = self.path
        data["entropy"] = self.entropy
        data["width"] = self.width
        data["height"] = self.height
        res = json.dumps(data)
        return res


    def get_image_info():
        image_info = {}
        if not self.is_process:
            self.process()
        image_info["width"] = self.width
        image_info["height"] = self.height
        image_info["entropy"] = self.entropy
        return image_info

    def process(self):
        try:
            im = Image.open(self.path).convert("L")
        except IOError as e:
            print e    

        self.width = im.width
        self.height = im.height
        # get entropy 
        self.data = im.getdata()
        mi_base = mi.MIBase()
        self.entropy = mi_base.compute_entropy(self.data)
        im.close()

    def get_graydata(self):
        try:
            im = Image.open(self.path).convert("L")
        except IOError as e:
            print e
            return 
        else:
            data = im.getdata()
            im.close() 
            return data

   
if __name__ == '__main__':
    if len(sys.argv) == 2:
        image = Imager(sys.argv[1])
        image.process()
        data = image.display()
        print data
    else:
        print "param error"
