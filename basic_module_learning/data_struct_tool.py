#!/usr/bin/python
#coding:utf-8
'''
    @brief: basic example for data struct
'''

def how_to_use_list():
    example = range(10)
    print example

    example_b = [0] * 10
    print example_b

    a = 2
    example_c = [a for i in range(5)]
    print example_c

    example_c = [[0 for col in range(5)] for row in range(6)]
    print example_c
    



