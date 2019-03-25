#!/usr/bin/python
# #encoding=utf-8

import os
import signal
import socket
import threading

import chat_utils as utils

def init_server():
    host = ""
    port = 8345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    conn, addr = s.accept()
    return conn, s

if __name__ == "__main__":
    conn, s = init_server()
    t_rec = threading.Thread(None, utils.rev_msg, "rec", (conn,), None, None)
    t_rec.start()
    t_play = threading.Thread(None, utils.display_msg, "play", ("snow",), None, None)
    t_play.start()
    t_input = threading.Thread(None, utils.input_msg, "input", (conn, "glstr"), None, None)
    t_input.start()
    t_list = []
    t_list.append(t_rec)            
    t_list.append(t_play)
    t_list.append(t_input)
    for t in t_list:
        t.join()
    print "exit"
    conn.close()
    s.close()
