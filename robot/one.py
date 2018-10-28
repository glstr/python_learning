#! /usr/bin/python
# coding=utf-8

class Robot:
    def __init__(self):
        self.name = 'one'
        self.age = 0
        self.day = '20180714'

    def chat(self):
        return

    def listen(self):
        return 

    def do(self):
        return 

    def introduce(self):
        print self.name
        print self.age
        print self.day

if __name__ == '__main__':
    robot = Robot()    
    robot.introduce()


