#!/usr/bin/python
# coding:utf-8

import unittest

import download_cppdoc


class TestDataSaver(unittest.TestCase):
    def setUp(self):
        return 

    def test_save_data(self):
        data = "hello world"
        path = "example/test.html"
        saver = download_cppdoc.DataSaver()
        saver.save_data(data, path)
        return 
    

if __name__ == '__main__':
    unittest.main()
    exit(1)
