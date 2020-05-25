#!/usr/bin/python
# coding:utf-8

import BaseHTTPServer
import SocketServer

import smart_car 

PORT = 8882
car = smart_car.SmartCar()

#directions path
directions = {
        "smartcar/run": smart_car.FORWARD, 
        "smartcar/back": smart_car.BACK,
        "smartcar/left": smart_car.LEFT,
        "smartcar/right": smart_car.RIGHT,
        "smartcar/brake": smart_car.BRAKE,
        "smartcar/spin_left": smart_car.SPIN_LEFT,
        "smartcar/spin_right": smart_car.SPIN_LEFT,
        }

def control_car(path):
    global car
    status = car.info()
    if status != 1:
        car.load()

    if path == "/check":
        car.check("")
        return 
    
    if path in directions:
        car.run(directions[path], 1)

class SmartServerHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type',
                         'text/plain; charset=utf-8')
        print "path:", self.path
        control_car(self.path)
        self.end_headers()
        self.wfile.write("hello world".encode('utf-8'))

    def get_method_from_path(self, path):
        return 


def run_smartcar_server():
    Handler = SmartServerHandler
    httpd =  SocketServer.TCPServer(("", PORT), Handler) 
    print "port:", PORT
    httpd.serve_forever()


if __name__ == '__main__':
    run_smartcar_server()
    exit(1)
