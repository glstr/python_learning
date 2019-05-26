#!/usr/bin/python
# coding:utf-8

import os
import os.path
import pprint
import sys
import urllib

from parse_html import HtmlParser


class DataSaver(object):
    def __init__(self):
        return 

    def save_data(self, data, path):
        path = urllib.unquote(path)
        path = path.lstrip('/')
        dir_path = os.path.dirname(path)
        print "dir_path:", dir_path
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        
        with open(path+".html", 'w') as f:
            f.write(data.encode('utf-8'))
        f.close()
        return 
            

class LinkSelector(object):
    def __init__(self, origin_url):
        self.origin_url = origin_url
        return 

    def get_all_in_domain_urls(self, input_urls):
        object_urls = []
        for url in input_urls:
            url = str(url)
            if url.startswith('/w/cpp/') and url.find('#') == -1:
                object_urls.append(url)
            else:
                pass
        return object_urls

    def get_all_out_domain_urls(self, input_urls):
        object_urls = []
        return object_urls
    

class SiteDownloader(object):
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

    def _save_data(self, content, url):
        if not url.startswith(self.origin_url):
            saver = DataSaver()
            saver.save_data(content, url)
        return 

    def _check_url(self, url):
        if not url.startswith("http"):
            return self.origin_url + url
        else:
            return url
        
    def _urls_gather(self, url):
        real_url = self._check_url(url)
        parser = HtmlParser(real_url)
        urls = parser.get_all_hyperlinks()
        self._save_data(parser.content, url)
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
        sd = SiteDownloader(sys.argv[1])
        object_urls = sd.urls_gather()
        pprint.pprint(object_urls)
