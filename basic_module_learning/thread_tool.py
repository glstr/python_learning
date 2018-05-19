#!/usr/bin/python
#coding=utf-8

# test thread in python
"""
@brief test thread in python
@date 2018-02-08 
"""

import thread
import threading
import time

def printNum(numbers, a_lock):
    if a_lock.acquire():
        for i in range(numbers):
            print str(i)+"\n"
	    a_lock.release()


def print_num_in_multi_thread():
    a_lock = thread.allocate_lock()
    thread.start_new_thread(printNum, (3,a_lock))
    thread.start_new_thread(printNum, (4,a_lock))


def how_to_use_sleep():
    while 1:
        print "hello"
        time.sleep(10)
    return 

def excute_in_thread():
    #param = ()
    #it = thread.start_new_thread(how_to_use_sleep, ())
    #print it
    t = threading.Thread(target=how_to_use_sleep)
    t.start()
    t.join()
    return 


#excute_in_thread()

