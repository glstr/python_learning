#!/usr/bin/python
#coding=utf-8

'''
    brief: some examples to control streaming
    author: glstr
    date: 20180611
'''

import librtmp

default_url = "rtmp://rtmp.liveshow.lss-user.baidubce.com/live/stream_bduid_3520888924_1529590025-L3"

def read_from_rtmp(stream_url):
    rtmp_url = stream_url
    #create a connection
    conn = librtmp.RTMP(rtmp_url)
    #attemp to connect
    conn.connect()
    #get a file-like object to access to the stream
    stream = conn.create_stream()
    #read 1024 bytes of data
    f = open("temp.flv", 'w')
    for i in range(50000):
        data = stream.read(1024)
        f.write(data) 
    conn.close() 
    f.close()

def stat(stream_url):
    return 

if __name__ == '__main__':
    read_from_rtmp(default_url)
