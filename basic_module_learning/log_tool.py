#coding=utf-8

"""
    @logging function about how to use logging
"""

import logging
import datetime

def log_something():
    return 

def logging_function():
    logging.info("hello world")

    
def how_to_log_in_file():
    today = datetime.date.today()
    todayStr = today.strftime("%Y%m%d")
    
    logging.basicConfig(filename="basic.log", level=logging.DEBUG, 
    format='[%(asctime)s] [%(filename)s] [%(funcName)s] [%(message)s]') 
    logging.info("hello world")
    logging.info("date:%s", todayStr)
    logging.info("num:%d", 3)


