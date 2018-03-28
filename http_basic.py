#!/usr/bin/python
#coding=utf-8
import httplib
import urllib
import socket
import json

host = "10.100.57.125"

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

def test_tool():
 	parameter = {"basic": "1"}
 	method = "/tool/1.0/dailytool.showBasicInfo"
 	print json_http_request(method, parameter)

test_tool()