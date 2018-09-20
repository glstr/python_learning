#! /usr/bin/python
#coding=utf-8

'''
    @brief: Base function for mongo operation
'''

from pymongo import MongoClient


def _get_client():
    conn = MongoClient('127.0.0.1', 27017)
    return conn


def insert_data(data):
    conn = _get_client()
    db = conn.img_db
    img_info = db.img_info
    img_info.insert({"name": "1.png", "size": 20})
    conn.close()


def query_data():
    conn = _get_client()
    db = conn.img_db
    img_info = db.img_info
    for i in img_info.find({"name": "1.png"}):
        print i
    conn.close()    


if __name__ == '__main__':
    insert_data("hello world")
    query_data()
    

