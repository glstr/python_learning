#!/usr/bin/python
# coding=utf-8
import sys

import numpy as np
from scipy.stats import mode
import matplotlib as mpl
mpl.use("TkAgg")
import matplotlib.pyplot as plt


def data_display(file_path, ope_type=0):
    data_displayer = DataDisplayer(file_path)
    data_displayer.load_data()
    data_displayer.meta_info()
    data_displayer.display()


class DataDisplayer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.cal_meta = False
        self.dimenstion = 0
        return 

    def load_data(self):
        self._data_array = np.loadtxt(self.file_path)
        self.dimenstion = self._data_array.ndim
        # width = len(self._data_array.shape)
        # if width > 1 or width < 1:
        #     return False
        return True

    def meta_info(self):
        if not self.cal_meta:
            self._cal_meta() 
        self.display_meta() 
        return 

    def display(self):
        if self.dimenstion == 1:
            self._display_one_dimension()
        elif self.dimenstion == 2:
            self._display_two_dimension()
        else:
            print "not support"
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

    def _display_one_dimension(self):
        plt.hist(self._data_array, 100)
        plt.xlabel("features")
        plt.ylabel("frequency")
        plt.title("features distribution")
        plt.show()
        print "show"
        return 

    def _display_two_dimension(self):
        array1 = self._data_array[:, 0]
        array2 = self._data_array[:, 1]
        plt.plot(array1, array2, 'ro')
        # plt.plot(self._data_array)
        plt.axis([0, 1, 0, 1])
        plt.show()
        return 

    def cal_distribution(self):
        percentiles = np.array([2.5, 25, 50, 75, 97.5])
        # Compute percentiles: ptiles_vers
        ptiles_vers = np.percentile(self._data_array, percentiles)
        self.distribution = ptiles_vers      
        return 
    

def usage():
    print "usage:"
    print "python *.py file_path ope_type"
    

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
        exit(1)
        
    file_path = sys.argv[1]
    print "file_path", file_path

    flag = 0
    if len(sys.argv) == 3:
        flag = sys.argv[2]
        print "flag", flag
    data_display(file_path, flag)
        
