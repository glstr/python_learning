#!/usr/bin/python
# coding=utf-8
'''
    @brief: image operator
    @author: glstr
'''

from PIL import Image


def divide(path):
    im = Image.open(path) 
    width = im.width
    height = im.height

    print width
    print height

    box = (0, 0, width/2, height/2)
    box_1 = (0, height/2, width/2, height)
    box_2 = (width/2, 0, width, height/2)
    box_3 = (width/2, height/2, width, height)

    _divide(box, im, "0")
    _divide(box_1, im, "1")
    _divide(box_2, im, "2")
    _divide(box_3, im, "3")


def _divide(box, image, filename):
    region = image.crop(box)
    region.save(filename+'.jpg')


if __name__ == '__main__':
    path = '/Users/pengbaojiang/pengbaojiang/code/python_src/python_learning/image_client/img.jpg'
    divide(path)

