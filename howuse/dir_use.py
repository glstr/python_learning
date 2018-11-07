#!/usr/bin/python
# coding=utf-8


def keyvaidir():
    d = {"hello": 1}
    for key, value in d.items():
        print key, 'corresponds to', value
    for key in d:
        print key, 'corresponds to', d[key]

