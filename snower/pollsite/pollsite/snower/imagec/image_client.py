#!/usr/bin/python
# coding=utf-8

'''
    @brief: Service for image operation and tool of make experiment.
'''

import common
import imager 
import image_manager as img_mar
import img_redisc as redisc
import mutual_infor as mi


class ImageClient():
    def __init__(self):
        return 

    def load_config(self):
        name = 'snow'
        self.img_mana = img_mar.ImageManager(name)
        self.img_mana.load()
        self.mi_base = mi.MIBase() 
        return 

    def case_one(self):
        # get img path        
        files_path = self._get_files_path()
        # caculate entropy
        key = 'pcloud:entropy'
        entropy_dir = {}
        for file_path in files_path:
            gray_data = self._get_graydata(file_path)
            entropy = self.mi_base.compute_entropy(gray_data)                               
            file_name = common.get_filename(file_path)
            entropy_dir[file_name] = entropy
        redisc.hmset(key, entropy_dir)
        return  

    def case_two(self):
        # get img path
        files_path = self._get_files_path()  
        # files_num = len(files_path)
        # random_num = common.random_num(0, files_num-1)
        # caculate entropy
        file_path = files_path.pop()
        data_a = self._get_graydata(file_path)
        file_name = common.get_filename(file_path)
        key = 'pcloud:mi:' + file_name
        mi_dir = {}
        for file_path in files_path:
            file_name = common.get_filename(file_path)
            data_b = self._get_graydata(file_path)
            img_mi = self.mi_base.compute_mi(data_a, data_b)
            mi_dir[file_name] = img_mi
        redisc.hmset(key, mi_dir)
        return 

    def case_three(self):
        files_path = self._get_files_path()
        for file_path in files_path:
            gray_data = self._get_graydata(file_path)
            for new_file_path in files_path:
                gray_data = _get_graydata(new_file_path)
                img_mi = self.mi_base.compute_mi(data_a, data_b) 
        return 

    def _get_graydata(self, file_path):
        img = imager.Imager(file_path)
        return img.get_graydata()

    def _get_files_path(self):
        return self.img_mana.get_allimages_path()

    def start(self):
        return 


if __name__ == '__main__':
    image_client = ImageClient()
    image_client.load_config()
    image_client.case_two()
    print 'hello world'


