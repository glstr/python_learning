#!/usr/bin/python
#coding=utf-8

'''
    note: python tips
'''

import ast
from pprint import pprint

def get_in_dir():
    '''
        brief: how to use enumerate
    '''
    items = ["hello", "world", "byebye"]
    #for item in items:
    #    print item
    #for i, item in enumerate(items):
    #    print i, item
    
    items_static = {"hello":3, "world":4, "byebye":5}
    #for item in items:
        #print item
    for i, item in enumerate(items_static):
        print i, item

def make_set():
    '''
        brief: make set and dir
    '''
    my_set= {i * 15 for i in xrange(15) }
    my_list = [i * 15 for i in xrange(15)]
    my_dict = {i: i * i for i in xrange(15)}
    print my_dict, my_list, my_set

def SimpleServer():
    print 'python -m SimpleHTTPServer'
    return 

def use_eval():
    '''
        brief: str to expression
    '''

    add_str = "1 + 2"
    complex_str = "2*2 + 3-4"
    list_str = "[1, 2, 3]"
    print eval(list_str)
    print ast.literal_eval(list_str)
    res = eval(complex_str)
    return res

def analyze_shell():
    print 'python -m cProfile my_script.py'
    return 

def set_break():
    print 'import pdb'
    print 'pdb.set_trace()'
    return 

def reverse_list():
    num_list = [1, 2, 3, 4, 5]
    print num_list[::-1]

def use_pprint():
    my_dict = {i:i*i for i in xrange(14)}
    pprint(my_dict)    

def x_or_y():
    a = 3
    b = 4 
    small = a if a < b else b  
    print small

if __name__ == '__main__':
    use_pprint()
