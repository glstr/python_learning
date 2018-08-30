#!/usr/bin/python
#coding=utf-8

'''
    @brief: tool of function test for package
'''

import image_manager as ima

if __name__ == '__main__':
    #dir_path = '/Users/pengbaojiang/pengbaojiang/code/python_src/python_learning/data/map_img/'
    manager = ima.ImageManager("snow")
    #manager.add_dir(dir_path)
    manager.load()
    file_path = manager.get_allimages_path()
    num = len(file_path)    
    print num


