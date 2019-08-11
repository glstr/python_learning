import unittest 
import numpy as np

class TestNumpyNarray(unittest.TestCase):
    
    def test_make_array(self):
        temp = np.arange(15).reshape(3, 5)
        print temp
        print temp.ndim
        print temp.shape 
        print temp.size 

        temp = np.array([1, 2, 3, 4])
        print temp 

        temp = np.zeros((3, 4))
        print temp

        temp = np.ones((4, 5), dtype = np.int16)
        print temp 

        temp = np.empty((4, 5))
        print temp 

        temp = np.arange(0, 100, 2)
        print temp 

    def test_operation_array(self):
        temp = np.arange(8).reshape(4, 2)
        print temp 
        array1 = temp[:, 0]
        print array1 

if __name__ == '__main__':
    unittest.main()
