#!/usr/bin/python
#coding=utf-8

'''
    @brief: some tool for proability
'''

import math

def log2(num):
    return math.log(num, 2)    

'''
    Some basic conception of probability theory.
'''
def query_p(num, result):
    '''
        If p ** num == result, query p. 
        log(result, p) == num
        log(result, 2)/log(p, 2) == num
        log(p, 2) == log(result, 2)/num
        p = 2 ** (log(result, 2)/num)
    '''
    return 2 ** (math.log(result, 2)/num)

def caculate_entropy(p_array):
    '''
        note: Caculate entropy of a array num.
        param: array of p(x)
        return: entropy of probability distribution
    '''
    sum = 0.0
        
#excute
if __name__ == '__main__':
    print query_p(10.0, 0.99)
