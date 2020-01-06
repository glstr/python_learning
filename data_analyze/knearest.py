#!/usr/bin/python
# coding=utf-8

import numpy as np

import array_helper as ah
def create_dataset():
    group = np.array([1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify(inx, data_set, labels, k):
    size = data_set.shape[0]
    diff_array = ah.create_array_array(inx, size) - data_set
    sq_diff_array = diff_array ** 2
    sq_distances = sq_diff_array.sum(axis = 1)
    distances = sq_distances ** 0.5
    sorted_dis_indices = distances.argsort()
    class_count = {}
    for i in range(k):
        vote_label = labels[sorted_dis_indices[i]]
        class_count[vote_label] = class_count.get(vote_lebel, 0) + 1 
    # sorted_class_count = sorted(class_count.iteritems(), 
           # key = )
    return 

