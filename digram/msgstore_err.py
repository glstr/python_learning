#!/usr/bin/python
# coding=utf-8

from pyecharts import Bar


def make_chart(file_path):
    attr = []
    attr_num = []
    with open(file_path) as f:
        for line in f:
            data = line.split(" ")
            attr_num.append(int(data[0]))
            attr.append(data[1])
    bar = Bar("msgstore err")
    bar.add("err", attr, attr_num)
    bar.render() 


if __name__ == '__main__':
    make_chart("data.txt")
