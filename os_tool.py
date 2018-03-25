#!/usr/bin/python
#coding:utf-8
'''
Some tools for daily days
'''
import os

def ping_url(url):
    print url
    target = "ping "+url
    print target

    os.system(target)
    fp = os.popen("ping"+url+"-t")
    fpread = fp.read()
    print type(fpread)
    print len(fpread)

def get_ip_config():
    command = "ipconfig"
    os.system(command)

def exe_command(command):
    os.system(command)

command = "netsh interface set interface wlan enabled"
exe_command(command)




