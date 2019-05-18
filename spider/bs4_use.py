#!/usr/bin/python
# coding:utf-8

from bs4 import BeautifulSoup


def bs4_usage_show(path):
    content = ''
    with open(path) as f:
        content = f.read()
    parser = 'html.parser'
    bsObj = BeautifulSoup(content, parser)
    for tag in bsObj.find_all(True):
        print tag.name, tag.string
    return 


if __name__ == '__main__':
    bs4_usage_show('test.html')
    exit(1)
