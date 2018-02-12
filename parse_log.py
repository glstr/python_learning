#coding=utf-8
import string
'''
@brief string function
'''
def format_str():
    print '{1},{0},{3}{2}'.format('hello','world','i','love')
    print 'name={name}, age={age}'.format(name="jim", age="8")
    print string.ascii_letters

def format_str_v2(farg, *args):
    print farg
    for arg in args:
        print arg

def formatter_usage():
    formater = string.Formatter()
    formater.parse("hello world")

def split_string():
    example = "hello world"
    result = str.split(example)
    for data in result:
        print data

def

'''
@brief re function
'''