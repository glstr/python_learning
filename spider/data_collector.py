#!/usr/bin/python
# coding=utf-8

import json

import requests


class DataCollector(object):
    def __init__(self):
        self.name = "default data collector"
        return 

    def grab(self, option):
        url = option["url"] 
        r = requests.get(url)
        r.json()
        return r 

    def gather(self, options):
        res = []
        for option in options:
            r = self.grab(option)
            res.append(r)
        return res

    def output(self, options):
        f = open("output.txt", "w")
        contents = self.gather(options) 
        for content in contents:
            cstr = json.dumps(content)
            f.write(cstr + '\n')
        f.close()
        return 

    def load_config(self, config_file):
        with open(config_file) as f:
            self.options = json.load(f)


if __name__ == '__main__':
    print "hello world"
