#!/usr/bin/python
#coding=utf-8

'''
    @brief: This file is used to extra data from html file.
'''

from bs4 import BeautifulSoup

default_path = "./2.html"
def parse_html():
    soup = BeautifulSoup(open(default_path), "html.parser")
    print soup.dl
    print soup.dl.name
    return 

class HtmlParser:
    def __init__(self):
        return 



if __name__ == "__main__":
    print "parse logfile"
