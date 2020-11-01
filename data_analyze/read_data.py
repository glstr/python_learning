#!/usr/bin/python
# coding=utf-8


def read_data(file_path):
    with open(file_path) as f:
        for line in f:
            line = line.rstrip('\n')
            data_array = line.split(" ")
            print data_array

read_data("pd.txt")

