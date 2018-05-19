#!/usr/bin/python
#coding=utf-8

'''
    @brief: Function for image download.
    @author: glstr
    @date: 20180515 
'''
from os import path
import requests

class Downloader:
    def __init__(self, basic_dir):
        '''
        '''
        # set basic dir for saving image 
        if path.exists(basic_dir): 
            self.basic_dir = basic_dir
        else:
            return 
        self.num = 0

    def download_all_img(target_url, target_ext):
        return 
    
    def _parse_content(file_content):
        return 
    
    def _get_image_url_list(file_content):
        return 

def download_target(target_url, num):
    r = requests.get(target_url)
    f = open(str(num) + ".html", "w")
    f.write(r.content)
    f.close()


#url_path ="http://img.ivsky.com/img/tupian/pre/201801/02/bingtianxuedi.jpg"
#url_path_ext = "http://www.ivsky.com/tupian/bingtianxuedi_v45721/pic_727663.html#al_tit"
#download_target(url_path_ext, 2)
