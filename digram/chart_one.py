#!/usr/bin/python
#coding=utf-8

from pyecharts import Bar

def make_char_one():
    attr = ["China", "English", "Franch"]
    attr_num = [2, 4, 5]
    bar = Bar("my first chart")
    bar.add("country", attr, attr_num)
    bar.render(r"/Users/pengbaojiang/pengbaojiang/code/python_src/python_learning/digram/new.html")


if __name__ == '__main__':
    make_char_one()




