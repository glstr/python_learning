#!/usr/bin/python
# coding=utf-8

'''
    @brief: Save image info in redis
'''

import redis

'''
    @brief: operation of set  
'''

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)


def sadd(key, *value):
    r.sadd(key, *value)
    return 


def smembers(key):
    return r.smembers(key)

def sismember(key, value):
    return r.sismember(key, value)

'''
    @brief: operation of hash
'''


def hmset(key, mapping):
    '''
        @brief: operation of hash
    '''
    r.hmset(key, mapping)
    return 


def hgetall(key):
    return r.hgetall(key)


'''
    @brief: operation of zset
'''


def zadd(key, *value, **score):
    r.zadd(key, *value, **score)
    return 


def zrange(key, start, end):
    return r.zrange(key, start, end)
