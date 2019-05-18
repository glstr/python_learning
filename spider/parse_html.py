#!/usr/bin/python
# coding:utf-8

import pprint
import sys

from bs4 import BeautifulSoup
import requests


class HtmlParser:
    def __init__(self, url):
        self.url = url
        return 

    def _get_content(self):
        r = requests.get(self.url)
        if r.status_code != requests.codes.ok:
            return ""
        return r.text

    def _get_obj_from_html(self, key, condition):
        res = []
        nameList = self.bsObj.findAll(key, condition)
        for name in nameList:
            if 'href' in name.attrs:
                link = {}
                link[name.get_text()] = name.attrs['href']
                res.append(link)
        return res

    def parse_html(self, options):
        content = self._get_content()
        parser = 'html.parser'
        self.bsObj = BeautifulSoup(content, parser)
        all_res = {}
        for key, item in options.items():
            res = self._get_obj_from_html(key, item)
            all_res[key] = res
        return all_res

    def get_all_hyperlinks(self):
        options = {"a": {}}
        return self.parse_html(options)

    def get_all_links(self):
        options = {"link": {}}
        return self.parse_html(options)
        

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "param error"
        exit(1)
    else: 
        parser = HtmlParser(sys.argv[1])
        hyperlinks = parser.get_all_hyperlinks()
        links_res = parser.get_all_links() 
        pprint.pprint(links_res)

