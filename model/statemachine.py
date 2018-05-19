#!/usr/bin/python
#coding=utf-8

'''
    @brief: Example of state machine.
'''

from string import upper

class StateMachine:
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endState = []

    def add_state(self, name, handler, end_state=0):
        name = upper(name)
        self.handlers[name] = handler
        if end_state:
            self.endState.append(name)

    def set_start(self, name):
        self.startState = upper(name)

    def run(self, cargo):
        try:
            handler = self.handlers[self.startState]
        except:
            raise "InitializationError", "must call .set_start before .run()"

        if not self.endState:
            raise "InitializationError", "at least one state must be an end_state"

        while 1:
            (newState, cargo) = handler(cargo)
            if upper(newState) in self.endState:
                break
            else:
                handler = self.handlers[upper(newState)]


        
