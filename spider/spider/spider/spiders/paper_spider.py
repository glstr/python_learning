#! /usr/bin/python 

import scrapy

class PaperSpider(scrapy.Spider):
    #spider name
    name = 'paper'
    #start point
    start_urls = ['']

    def parse(self, response):
        return 
