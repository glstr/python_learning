#!/usr/bin/python
# coding:utf-8

import urllib
from bs4 import BeautifulSoup


def open_url():
    html = urllib.urlopen("http://pythonscraping.com/pages/page1.html")
    bsObj = BeautifulSoup(html.read(), 'features="lxml"')
    print bsObj.h1
    return 


if __name__ == '__main__':
    open_url()
    exit(1)
