#! /usr/bin/python
# coding=utf-8

'''
    @brief: Base function for redis operation
'''

import redis

key_pcloud_metainfo = "pcloud:metainfo:snow"
key_pcloud_all = "pcloud:allimages:snow"


def get_client():
    pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
    r = redis.Redis(connection_pool=pool)
    return r 


def image_info():
    r = get_client()
    res = r.hgetall(key_pcloud_metainfo)
    return res


def get_all_images():
    r = get_client()
    res = r.smembers(key_pcloud_all)
    return res



