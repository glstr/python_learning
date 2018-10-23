#!/usr/bin/python
# coding=utf-8

import tensorflow as tf


def demo():
    hello = tf.constant("hello world")
    sess = tf.Session()
    print sess.run(hello)
    
if __name__ == '__main__':
    demo()
