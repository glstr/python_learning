#!/usr/bin/python
# coding:utf-8

import pprint
import sys

from parse_html import HtmlParser


class LinkSelector(object):
    def __init__(self, origin_url):
        self.origin_url = origin_url
        return 

    def get_all_in_domain_urls(self, input_urls):
        object_urls = []
        for url in input_urls:
            url = str(url)
            # start at / 
            if url.startswith('/w/cpp/') and url.find('#') == -1:
                object_urls.append(self.origin_url + url)
            # elif url.startswith(self.origin_url):
            #     object_urls.append(url)
            else:
                pass
            # start at 'origin_url'
        return object_urls

    def get_all_out_domain_urls(self, input_urls):
        object_urls = []
        return object_urls
    

class SizeDownloader(object):
    def __init__(self, origin_url):
        self.origin_url = origin_url
        return 

    def urls_gather(self):
        urls_not_search = set()
        urls_searched = set() 

        urls_not_search.add(self.origin_url)
        # for url in urls_not_search:
        while(len(urls_not_search) > 0):
            url = urls_not_search.pop()
            new_urls = self._urls_gather(url)
            urls_searched.add(url)
            for new_url in new_urls:
                if new_url not in urls_searched:
                    urls_not_search.add(new_url) 
            print len(urls_not_search), len(urls_searched), url
        return urls_searched
        
    def _urls_gather(self, url):
        parser = HtmlParser(url)
        urls = parser.get_all_hyperlinks()
        input_urls = []
        for url in urls.values():
            input_urls.append(url)
        lselector = LinkSelector(self.origin_url)
        object_urls = lselector.get_all_in_domain_urls(input_urls)
        return object_urls


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "param error"
        exit(1)
    else: 
        sd = SizeDownloader(sys.argv[1])
        object_urls = sd.urls_gather()
        pprint.pprint(object_urls)
