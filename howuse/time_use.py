#!/usr/bin/python
# coding:utf-8


'''
    @brief: Some tools for date package.
'''

import datetime
import time

midnight = "00:00:00"


def get_ts():
    return time.time()


def get_today():
    '''
        @note: Get today.
    '''
    today = datetime.datetime.today()
    date_str = today.strftime("%Y%m%d")
    return date_str


def get_last_day():
    '''
        @note: Get last day date as YMD.
    '''
    today = datetime.datetime.today()
    yesterday = today - datetime.timedelta(1)
    date_str = yesterday.strftime("%Y%m%d") 
    return date_str


def get_date_from_ts(format):
    now = time.time()
    tl = time.gmtime(int(now))
    format_time = time.strftime("%Y-%m-%dT%H:%M:%SZ", tl)
    print format_time
    return format_time


def get_ts_from_date(date_str):
    '''
        @note: Get timestamp from date as 2018051300.
        @input: date as 2018051300.
        @output: timestamp.
    '''
    st = time.strptime(date_str, "%Y%m%d%H")
    ts = int(time.mktime(st))
    return str(ts)


def second_of_a_day():
    '''
        @note: Get second of a day.
    ''' 
    return 24 * 60 * 60


def second_of_30_day():
    '''
        #note: Get second of 30 days
    '''
    return 30 * second_of_a_day()


if __name__ == '__main__':
    get_date_from_ts("")
