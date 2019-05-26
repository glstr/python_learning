#!/usr/bin/python
# coding:utf-8

import requests


def get_html(url):
    try: 
        r = requests.get(url)
    except requests.exceptions.RequestException, e:
        print e
        return ""
    if r.status_code != requests.codes.ok:
        return ""
    else: 
        return r.text


if __name__ == '__main__':
    exit(1)
