#!/usr/bin/python
#coding=utf-8


'''
    @brief: The main file to process image 
    @author: glstr
    @date: 20180504
'''


import logging

import image_tool
import mutual_infor

def process_init():
    logging.basicConfig(filename="./log/basic.log", level=logging.DEBUG, 
    format='[%(asctime)s] [%(filename)s] [%(funcName)s] [%(message)s]') 

def process_mutual_info(file_a, file_b):
    '''
        @note: Compute mutual infor for pic a and pic b.
    '''
    gray_data_a = image_tool.get_gray_data_from_img(file_a)
    gray_data_b = image_tool.get_gray_data_from_img(file_b)

    mi_base = mutual_infor.MIBase()
    mi = mi_base.compute_mi(gray_data_a, gray_data_b)
    
    return mi 

def process_entropy(file_a):
    '''
        @note: Compute entropy
    '''
    #get gray data from image
    gray_data = image_tool.get_gray_data_from_img(file_a) 
    print gray_data
    logging.info("[gray_data len:%d]", len(gray_data))

    #compute entropy
    mi_base = mutual_infor.MIBase()
    entropy = mi_base.compute_entropy(gray_data)
    logging.info("[entropy:%d]", entropy)
    return entropy 

def auto_find_target_img(dir_path, img_path):
    logging.info("[dir:%s, img_path:%s]", dir_path, img_path)



#excute
if __name__ == '__main__':
    process_init()
    file_path = "./image_client/img.jpg"
    logging.info("[hello]")
    print process_entropy(file_path)
    print process_mutual_info(file_path, file_path)
