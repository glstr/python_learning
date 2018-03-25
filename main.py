#!/usr/bin/python
#coding=utf-8
import chat_tool

#if __name__ == '__main__':
print 'hello world'
client2 = chat_tool.Session("", 8348)
client2.connect("localhost", 8345)
client2.send_msg("hello")




