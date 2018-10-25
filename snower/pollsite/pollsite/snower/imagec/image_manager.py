#!/usr/bin/python
# coding=utf-8


'''
    @brief: This file is used to manager image, 
    such as downloading and get file path and so on. 
    @author: glstr
    @date: 20180507
'''

import common
import img_redisc as redisc

PCLOUD_ALLIMAGES = "pcloud:allimages:"
PCLOUD_METAINFO = "pcloud:metainfo:"


class ImageManager:
    '''
        @note: Base class for image managing
    '''
    def __init__(self, name):
        self.name = name
        self.metainfo = {}

    def load(self):
        metainfo = self._get_metainfo()
        if metainfo is None:
            common.write_log("get metainfo fail")
        else:
            self.metainfo = metainfo

    def add_dir(self, dir_path):
        '''
            note: Only support one dir at same time.
        '''
        # get image info from dir
        file_list = common.get_filelist(dir_path)
        # update image info in redis
        res = self._insert_images(file_list)
        if res is not None:
            common.write_log(common.REDIS_ERROR)
            return
        num = len(file_list)
        # update metainfo in object and redis
        self.metainfo["dir_path"] = dir_path
        self.metainfo["img_num"] = num
        self._update_metainfo()
        return 
    
    def get_num(self):
        return self.metainfo["img_num"]

    def get_allimages_path(self):
        res = []
        if self.metainfo.has_key('db_key'):
            db_key = self.metainfo['db_key']
            return redisc.zrange(db_key, 0, -1)
        else:
            common.write_log("no infor")
        return res

    def get_image_path(self, img_id):
        img_path = self.metainfo["dir_path"] + str(img_id) + ".png"
        return img_path

    def _get_metainfo(self):
        key = PCLOUD_METAINFO + self.name
        return redisc.hgetall(key)

    def _update_metainfo(self):
        key = PCLOUD_METAINFO + self.name
        redisc.hmset(key, self.metainfo)
        return 

    def _insert_images(self, file_list):
        key = PCLOUD_ALLIMAGES + self.name
        self.metainfo["db_key"] = key
        score = {}
        temp = []
        for ele in file_list:
            score[ele] = self._get_score(ele)
        return redisc.zadd(key, *temp, **score)
    
    def _get_score(self, img):
        temp = img.split('/')    
        img_str = temp[-1].rstrip('png')
        return float(img_str)

        
if __name__ == '__main__':
    print 'hello world'


