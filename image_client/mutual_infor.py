#!/usr/bin/python
#coding=utf-8

'''
    @brief: This file is used to caculate image mutual infomation. As we don't know it exactly that
    wether MI can represent the similarity of images, so we need try to use serious way to gather 
    enought data to get the best way.
    @author: glstr

'''
import logging
import math

class MIBase:
    '''
        @note: Base class for computing MI
    '''
    def __init__(self, log):
        self.log = log
        return 
    
    def compute_entropy(self, gray_data):
        # static each pix number 
        static_data = self._static_gray_data(gray_data)

        entropy = 0.0
        sum_num = len(gray_data)

        for i in range(sum_num):
            temp = 0.0
            if(static_data[i] == 0):
                temp = 0.0
            else:
                temp = (-static_data[i]/sum_num) * math.log(static_data[i]/sum_num)
            entropy = entropy + temp
                
        return entropy

    def compute_join_entropy(self, gray_data_a, gray_data_b):
        '''
            @note: Compute join entropy
        '''
        h_xy = [[0 for column in range(256)] for row in range(256)]
        ele_num = len(gray_data_a) 
        logging.info("[gray data number:%d]", ele_num)
        for i in range(ele_num):
            x = gray_data_a[i]
            y = gray_data_b[i]
            h_xy[x][y] = h_xy[x][y] + 1

        result = 0.0
        for i in range(256):
            for j in range(256):
                temp = 0.0
                if (h_xy[x][y] == 0):
                    temp = 0.0
                else:
                    p = float(h_xy[i][j])/ele_num
                    temp = -p * log(p)
                result = result + temp
        return result

    def compute_MI(self, gray_data_a, gray_data_b):
        '''
            @note: Compute MI 
        '''
        entropy_a = self.compute_entropy(gray_data_a)
        entropy_b = self.compute_entropy(gray_data_b)
        joint_entory = self.compute_join_entropy(gray_data_a, gray_data_b)

        result = entropy_a + entropy_b - joint_entory

        logging.info("[entroy_a:%d, entropy_b:%d, joint_entory:%d, MI:%d]", entropy_a, entropy_b, joint_entory, result)
        return result
    
    def _static_gray_data(self, gray_data):
        static_data = [0] * 256

        for element in gray_data:
            static_data[element] = static_data[element] + 1
        return static_data

'''
    @brief: Find the best image to match target.
'''


