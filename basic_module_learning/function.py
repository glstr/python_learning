#!/usr/bin/python
#coding:utf-8

def modify_func(func):
    def new_func(a, b):
        return 3
    return new_func

def modify_func_with_result(result):
    def func_decator(func):
        def new_func(a, b):
            return result
        return new_func
    return func_decator 

@modify_func_with_result(result=10)
def add(a, b):
    return a + b

def make_func(num):
    if num == 1:
        def add(x, y):
            return x + y
        return add
    elif num == 2:
        def return_const():
            return 3

    else:
        def re_nothing():
            print "hello world"
            return re_nothing

'''
    note: Show how to use function as a parameter.
'''
def print_sth(string):
    print string
    def print_with_hello_world():
        print "hello world", string
    
    def print_with_bye_bye():
        print "byebye", string
    
    print_with_bye_bye()
    print_with_hello_world()
    return 

if __name__ == '__main__':
    print_sth("program")


