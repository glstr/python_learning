#!/usr/bin/python
# coding=utf-8


def make_list():
    return ["123", 12, [1, 2], [3, 4], [[4, 5], [5, 6]]]


def tranverse():
    t_l = make_list()
    for ele in t_l:
        print ele


def list_example():
    tranverse()


if __name__ == '__main__':
    list_example()


