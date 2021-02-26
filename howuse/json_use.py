#!/usr/bin/python
# coding=utf-8
import json


def unicode_convert(input_data):
    if isinstance(input_data, dict):
        return {unicode_convert(key): unicode_convert(value) for key, value in input_data.iteritems()}
    elif isinstance(input_data, list):
        return [unicode_convert(element) for element in input_data]
    elif isinstance(input_data, unicode):
        return input_data.encode('utf-8')
    else:
        return input_data


def unmarshal(json_str):
    return unicode_convert(json.loads(json_str))

