#!/usr/bin/python
#coding=utf-8

'''
    @brief: some examples of random num.
    @author: glstr
    @date: 20180602
'''

import random
import matplotlib.pyplot as plt

def gen_rand_array():
    a = []
    for i in range(100000):
        a.append(random.randint(0, 10))
    return a

# random distribution 
def gen_rand_array_ex():
    return 

def display_array(array):
    p_static = {}
    for ele in array:
        if p_static.has_key(ele):
            p_static[ele] = p_static[ele] + 1
        else:
            p_static[ele] = 0
    return p_static

def show_digram(p_static):
    x = p_static.keys()
    y = p_static.values()
    y_p = []
    for ele in y:
        ele_p = ele/100000.0
        y_p.append(ele_p)


    plt.figure(figsize=(8,4))
    plt.plot(x, y_p ,label="p", linewidth=2)
    plt.xlabel("key")
    plt.ylabel("value")
    plt.title("probability distribution")
    plt.legend()
    plt.show()
    return 

if __name__ == "__main__":
    #a = gen_rand_array()
    #p_static = display_array(a)
    #show_digram(p_static)
    print 1527575231 - 1527575193
        

