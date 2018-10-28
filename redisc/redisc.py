#! /usr/bin/python
# coding=utf-8

'''
    @brief: Base function for redis operation
'''

import redis


def redis_operation_first():
    pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
    r = redis.Redis(connection_pool=pool)
    r.set('bing', 'baz')
    

def try_operation():
    try:
        a = 3/0
        print a
    except ZeroDivisionError, e:
        print "error:", e
    print "hello world"
