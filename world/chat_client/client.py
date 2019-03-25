#!/usr/bin/python
#coding=utf-8

import socket
import threading

import chat_utils as utils


def init_client():
    host = "localhost"
    port = 8345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s
    

if __name__ == "__main__":
    s = init_client()
    t_rec = threading.Thread(None, utils.rev_msg, "rec", (s,), None, None)
    t_rec.start()
    t_play = threading.Thread(None, utils.display_msg, "play", ("glstr",), None, None)
    t_play.start()
    t_input = threading.Thread(None, utils.input_msg, "input", (s, "snow"), None, None)
    t_input.start()
    t_list = []
    t_list.append(t_rec)
    t_list.append(t_play)
    t_list.append(t_input)
    for t in t_list:
        t.join()
    utils.input_msg(s, "snow")
    s.close()
