#!/usr/bin/python
# coding=utf-8

'''
    @brief: tool of function test for package
'''

import sys

from pyecharts import Bar
from pyecharts import Line

import common
import image_manager as ima
import imager
import mutual_infor 

dir_path = ""


def _caculate_mi_list(source, targat_list):
    imgs = imager.Imager(source) 
    imgs_data = imgs.get_graydata()
    res = []
    i = 0
    for f in targat_list:
        temp = []
        img = imager.Imager(f) 
        img_data = img.get_graydata() 
        mi_base = mutual_infor.MIBase()
        mi = mi_base.compute_mi(imgs_data, img_data)
        temp = (i, mi)
        res.append(temp)
        i = i + 1
    return res


def caculate_mi_list(dir_path):
    files = common.get_filelist(dir_path)
    res = _caculate_mi_list(files[3], files[0:10])
    data_a, data_b = Bar.cast(res)
    print data_a
    print data_b
    bar = Line("甜甜的实验", "二哥出品")
    bar.use_theme('vintage')
    bar.add("数据", data_a, data_b)
    bar.render()
    return 


if __name__ == '__main__':
    # dir_path = "/home/snow/pengbaojiang/data/map_img/"
    if len(sys.argv) != 2:
        print "param error"
        
    dir_path = sys.argv[1]
    manager = ima.ImageManager("snow")
    manager.add_dir(dir_path)
    manager.load()
    file_path = manager.get_allimages_path()
    num = len(file_path)    
    print num


