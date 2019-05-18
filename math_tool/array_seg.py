#!/usr/bin/python
# coding:utf-8


def array_seg(data, k):
    res = [[] for i in range(k)]
    for i, el in enumerate(data):
        res[i % k].append(el)                 
    return res        


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6]
    res = array_seg(data, 4)
    print res
    exit(1)
