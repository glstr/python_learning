#!/usr/bin/python
# coding=utf-8

'''
    @brief: Service for image operation and tool of make experiment.
'''
import os
from pprint import pprint
import sys

from pyecharts import Line 

import common
import imager 
import image_operator as img_ope
import mutual_infor as mi


funcs = {}


def img_info(param):
    im = imager.Imager(param)    
    im.load()
    info = im.get_image_info()
    print info


def mutual_info(param):
    params = common.parse_param(param)
    path_a = params[0]
    ids = []
    mis = []
    i = 0
    for path in params:
        res = _mutual_info(path, path_a)
        print res
        if i != 0:
            ids.append(i)
            mis.append(res["mi_r"]/0.6)
        i = i + 1
    bar = Line("我的第一个图表", "这里是副标题")
    bar.add("mi", ids, mis, is_more_utils=True)
    bar.render()
    return 


def mutual_info_f(param):
    dir_path = "range/" 
    all_path = ""
    with open(param) as f:
        for line in f.readlines():
            path = dir_path + line
            path = path.rstrip('\n')
            if all_path == "":
                all_path = path
            else:
                all_path = all_path + "," + path
    print all_path
    return mutual_info(all_path)


def mutual_info_ex(param):
    params = common.parse_param(param)    
    path_a = params[0]
    ids = []
    mis = []
    for i in range(5):
        mis.append([])
    j = 0
    for path in params:
        res = _mutual_info_ex(path, path_a)
        if j != 0:
            ids.append(j)
            for i in range(5):
                mis[i].append(res[i])
        pprint(res)
        j = j + 1
    bar = Line("我的第一个图表", "这里是副标题")
    num_mis = len(mis)
    for index in range(num_mis):
        num_ele = len(mis[index])
        max_n = max(mis[index])
        for ele_i in range(num_ele):
            mis[index][ele_i] = mis[index][ele_i]/max_n
            
    for i in range(5):
        bar.add("mi"+str(i), ids, mis[i], is_more_utils=True)
    bar.render()
    pprint(mis)        
    return 


def mutual_info_ex_f(param):
    dir_path = os.path.dirname(param)
    all_path = ""
    with open(param) as f:
        for line in f.readlines():
            path = dir_path + line
            path = path.rstrip('\n')
            if all_path == "":
                all_path = path
            else:
                all_path = all_path + "," + path
    print all_path
    return mutual_info_ex(all_path)


def _mutual_info(path_a, path_b):
    img_a = imager.Imager(path_a)
    data_a = img_a.get_graydata()
    img_b = imager.Imager(path_b)
    data_b = img_b.get_graydata()
    mi_o = mi.MIBase()
    en_a = mi_o.compute_entropy(data_a)
    en_b = mi_o.compute_entropy(data_b)
    join_e = mi_o.compute_join_entropy(data_a, data_b)
    mi_r = mi_o.compute_mi(data_a, data_b)
    res = {path_a: en_a, path_b: en_b, "join_e": join_e, "mi_r": mi_r}
    return res


def _mutual_info_ex(path_a, path_b):

    mi_o = mi.MIBase()

    img_o = img_ope.ImageOpeor()
    img_as = img_o.divide_to_four(path_a)
    img_bs = img_o.divide_to_four(path_b)

    img = imager.Imager(path_a)  
    data_o = img.get_graydata()
    en_o = mi_o.compute_entropy(data_o)

    res = []
    mi_all = 0.0
    for i in range(len(img_as)):

        data_a = img_as[i].convert("L").getdata()
        data_b = img_bs[i].convert("L").getdata()
        en_a = mi_o.compute_entropy(data_a)
        # en_b = mi_o.compute_entropy(data_b)
        weight = en_a / en_o

        # join_e = mi_o.compute_join_entropy(data_a, data_b)

        mir_o = mi_o.compute_mi(data_a, data_a)
        mir_r = mi_o.compute_mi(data_a, data_b)
        mi_i = mir_r / mir_o
        mi_temp = mi_i * weight
        mi_all = mi_all + mi_temp
        res.append(mir_r)
    res.append(mi_all)        
    return res


def load():
    funcs['info'] = img_info
    funcs['m_info'] = mutual_info
    funcs['m_info_f'] = mutual_info_f
    funcs['m_info_ex'] = mutual_info_ex
    funcs['m_info_ex_f'] = mutual_info_ex_f
    

def usage():
    print "usage:"
    print "python *.py [action] [param]"
    print "support method"
    for i in funcs.keys():
        print i
    print "example:"
    print "python image_case.py m_info_f 'range/index.txt'"


if __name__ == '__main__':
    load()
    if len(sys.argv) < 2:
        usage()
    if len(sys.argv) == 3:
        method = sys.argv[1]
        param = sys.argv[2]
        if funcs.has_key(method):
            funcs[method](param)
        else:
            usage()


