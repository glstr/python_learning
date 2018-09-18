#!/usr/bin/python
#coding=utf-8

'''
    @brief: Save import infor in mongo
'''

from pymongo import MongoClient

def load():
    client = MongoClient('localhost', 27017)
    db = client['img_db']
    collection = db['img_info']
    doc = {'name': '2.png', 'size': 40}
    collection.insert_one(doc).inserted_id
    return 

def get_instance(db, collection):
    client = MongoClient('localhost', 27017)
    return client[db][collection]

def insert(db, collection, data):
    instance = get_instance(db, collection)
    _id = instance.insert_one(data).inserted_id
    print _id
    return 

def query(db, collection, query_param):
    instance = get_instance(db, collection)
    res = instance.find_one(query_param)
    return res

if __name__ == '__main__':
    db = 'img_db'
    collection = 'img_info'
    #doc = {'name': '2.png', 'size': 40}
    #insert(db, collection, doc)
    query_param = {'name': '2.png'}
    print query(db, collection, query_param)
    


