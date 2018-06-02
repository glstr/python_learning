#!/usr/bin/python
#coding=utf-8
import httplib
import urllib
import socket
import json

'''
    brief: Some function for http request and response
'''

host = "10.100.57.125"

'''
    note: url 
'''
def make_url():
    '''
        note: Make a url useable
    '''
    default_url = 'http://host:port/path?key={"value": "hello"}'
    params = {"key": {"value":"hello"}, "name": "jim"}
    res = urllib.urlencode(params)
    print res

'''
    note: http request
'''
def json_http_request(method, parameter):
    body = json.dumps(parameter)
    print body
    headers = {"Content-type": "application/json", "Accept":"text/plain"}

    global host
    conn = httplib.HTTPConnection(host, 8135)
    
    conn.request("POST", method, body, headers)
    response = conn.getresponse()
    data = response.read()

    conn.close()
    return data 

def keyvalue_http_request(method, params):
    params = urllib.urlencode(params)
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

    print params
    global liveshow_host
    conn = httplib.HTTPConnection(host, 8135,)

    conn.request("POST", method, params, headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()

    print type(data)
    #res = json.loads(data)
   
    return data

def test_tool():
 	parameter = {"basic": "1"}
 	method = "/tool/1.0/dailytool.showBasicInfo"
 	print json_http_request(method, parameter)

def test_tool_ex():
    parameter = {"room_id": 554444}
    method = "/tool/1.0/liveshowtool.getRoomInfo"
    print json_http_request(method, parameter)

def test_replay():
    parameter = {}
    parameter["room_id"] = 1423824934
    parameter["duration"] = 1047
    parameter["replay"] = "https://p2.bdstatic.com/rtmp.liveshow.lss-user.baidubce.com/live/stream_bduid_3479035377_1423824934/recording_20180329135556.m3u8"
    method = "/tool/1.0/liveshowtool.replaceReplay"
    print keyvalue_http_request(method, parameter)

if __name__ == '__main__':
    make_url()
