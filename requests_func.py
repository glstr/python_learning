#!/usr/bin/python
#coding=utf-8

import requests

local_host = "http://cp01-pengbaojiang.epc.baidu.com:8882/api/1.0/rooms.info"
def test_liveshow_info(room_id):
	parameter = {"room_id": room_id}
	r = requests.post(local_host, parameter)
	data =  r.json()
	print data["info"]
test_liveshow_info(554110)