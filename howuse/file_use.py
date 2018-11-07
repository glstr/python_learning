#!/usr/bin/python
# coding:utf-8

'''
    brief: dir example
'''


def dir_ite():
    example = {"hello": 1, "world": 2}
    for k, v in example.items():
        print k, v


if __name__ == '__main__':
    dir_ite()

