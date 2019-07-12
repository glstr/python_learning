#!/usr/bin/python
# coding=utf-8

import sys

import numpy as np


class DataGenerator:
    def __init__(self, path):
        self.path = path

    def set_para(self, height, width):
        self.height = height
        self.width = width

    def make(self):
        data_buffer = np.random.uniform(-1, 1, (height, width))
        print data_buffer
        np.savetxt(self.path, data_buffer, fmt='%f')
        return      

def usage():
    print "usage:hello world"
    print "python *.py height width file_name"

if __name__ == '__main__':
    if len(sys.argv) < 3:
        usage()
        exit()

    height = int(sys.argv[1])
    width = int(sys.argv[2])
    file_name = "output.txt"
    if len(sys.argv) == 4:
        file_name = sys.argv[3]
    data_generator = DataGenerator(file_name) 
    data_generator.set_para(height, width)
    data_generator.make()
