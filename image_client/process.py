#!/usr/bin/python
#coding=utf-8
'''
    @brief: The main file to process image 
    @author: glstr
    @date: 20180504
'''

import logging

import image_tool
import mutual_info

def process_init():
    logging.basicConfig(filename="basic.log", level=logging.DEBUG, 
    format='[%(asctime)s] [%(filename)s] [%(funcName)s] [%(message)s]') 

def process_mutual_info(file_a, file_b):
    '''
        @note: Compute mutual infor for pic a and pic b.
    '''
    gray_data_a = image_tool.get_gray_data_from_img(file_a)
    gray_data_b = image_tool.get_gray_data_from_img(file_b)

    mi_base = mutual_info.MIBase()
    mi = mi_base.compute_entropy(gray_data_a, gray_data_b)
    
    return mi 

def process_entropy(file_a):
    '''
        @note: Compute entropy
    '''
    #get gray data from image
    gray_data = image_tool.get_gray_data_from_img() 
    logging.Info("[gray_data len:%d]", len(gray_data))

    #compute entropy
    mi_base = mutual_info.MIBase()
    entroy = mi_base.compute_entropy(gray_data)
    logging.Info("[entroy:%d]", entroy)
    return 



