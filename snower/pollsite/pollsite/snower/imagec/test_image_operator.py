#!/usr/bin/python
# coding=utf-8
'''
    @brief: test for image operator
    @author: glstr
'''
import unittest

import image_operator as ip

img_path = "/Users/pengbaojiang/pengbaojiang/code/python_src/python_learning/snower/pollsite/pollsite/snower/imagec/img.jpg"


class TestImageOperator(unittest.TestCase):
    '''
        @brief: Test case
    '''
    def test_divide(self):
        print "hello world"

    def test_cut(self):
        imgop = ip.ImageOpeor(img_path)
        box = [100, 100, 200, 200]
        imgop.cut(box, "test.img")


if __name__ == '__main__':
    unittest.main()
