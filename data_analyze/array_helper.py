#!/usr/bin/python
# coding=utf-8

import numpy as np 

def create_array_array(inx, k):
    temp = np.tile(inx, (k, 1))
    return temp

if __name__ == '__main__':
    inx = np.array([1, 2])
    print create_array_array(inx, 4)
    exit(0)

