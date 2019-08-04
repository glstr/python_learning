#!/usr/bin/python
# coding=utf-8
import sys

import numpy as np
from scipy.stats import mode
import matplotlib as mpl
mpl.use("TkAgg")
import matplotlib.pyplot as plt


class DataDisplay:
    def __init__(self, file_path):
        self.file_path = file_path
        self.cal_meta = False
        return 

    def load_data(self):
        self._data_array = np.loadtxt(self.file_path)
        width = len(self._data_array.shape)
        if width > 1 or width < 1:
            return False
        return True

    def meta_info(self):
        if not self.cal_meta:
            self._cal_meta() 
        self.display_meta() 
        return 

    def _cal_meta(self):
        self.length = len(self._data_array)
        self.max = self._data_array.max()
        self.min = self._data_array.min()
        self.mean = np.mean(self._data_array)
        self.median = np.median(self._data_array)
        self.mode = mode(self._data_array)
        self.cal_distribution()
        self.cal_meta = True
        return 

    def display_meta(self):
        print "len:", self.length
        print "max:", self.max
        print "min:", self.min
        print "mean:", self.mean
        print "median:", self.median
        print "mode:", self.mode
        print "distribution:", self.distribution
        return 

    def show(self):
        plt.hist(self._data_array, 100)
        plt.xlabel("features")
        plt.ylabel("frequency")
        plt.title("features distribution")
        plt.show()
        print "show"
        return 

    def cal_distribution(self):
        percentiles = np.array([2.5, 25, 50, 75, 97.5])
        # Compute percentiles: ptiles_vers
        ptiles_vers = np.percentile(self._data_array, percentiles)
        self.distribution = ptiles_vers      
        return 
    


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        exit(1)
    
    file_path = sys.argv[1]
    print file_path
    data_display = DataDisplay(file_path)
    data_display.load_data()
    data_display.meta_info()
    data_display.show()
    exit(0)
