#!/usr/bin/python
# coding:utf-8

import pprint
import sys

from bs4 import BeautifulSoup

import utils


class HtmlParser:
    def __init__(self, url):
        self.url = url
        return 

    def _get_content(self):
        return utils.get_html(self.url)
        
    def _get_obj_from_html(self, key):
        res = {}
        nameList = self.bsObj.findAll(key)
        for name in nameList:
            if 'href' in name.attrs:
                res[name.get_text()] = name.attrs['href']
        return res

    def parse_html(self, option):
        content = self._get_content()
        parser = 'html.parser'
        self.bsObj = BeautifulSoup(content, parser)
        return self._get_obj_from_html(option)
        
    def get_all_hyperlinks(self):
        return self.parse_html('a')

    def get_all_links(self):
        return self.parse_html('link')
        

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "param error"
        exit(1)
    else: 
        parser = HtmlParser(sys.argv[1])
        hyperlinks = parser.get_all_hyperlinks()
        links_res = parser.get_all_links() 
        pprint.pprint(links_res)

