#!/usr/bin/python
#coding=utf-8

# test thread in python
"""
@brief test thread in python
@date 2018-02-08 
"""

import thread
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




