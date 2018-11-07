#!/usr/bin/python
# coding:utf-8


'''
    brief: Examples of math
'''
import random


def rand_use(a, b):
    print random.randint(a, b)
    print random.randrange(a, b, 1)
    

if __name__ == '__main__':
    rand_use(3, 4)
