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
    
def str_to_byte():
    str_example = "hello world"
    #byte_example = bytes(str_example, encoding='utf-8')
    byte_example = str.encode(str_example)

    print type(byte_example)

def str_to_int():
    num_str = '123'
    num = int(num_str)
    print num

if __name__ == '__main__':
    str_to_int()



