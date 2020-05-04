#!/usr/bin/python
# coding:utf-8

PORT = 8081

def run_file_server():
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()


if __name__ == '__main__':
    run_file_server()
    exit(1)
