#!/usr/bin/python
#coding=utf-8


'''
    @brief: This file is used to manager image, such as downloading and get file path and so on. 
    @author: glstr
    @date: 20180507
'''


import logging
import os

class ImageManager:
    '''
        @note: Base class for image managing
    '''
    def __init__(self, main_path):
        self.main_dir = main_dir

    def get_all_img_from_dir(self):
        '''
            @note: Get all image from main dir, if main dir not exist, return empty
            list.
        '''
        if os.path.isdir(self.main_dir):
            return os.listdir(self.main_dir)
        else:
            logging.warning("[errMsg: main dir not exist]")
            return []

        


class ImageDownloader:
    '''
        @note: Base class for image downloading
    '''
    def __init__(self, dir_path="./"):
        self.dir_path = dir_path


