#!/usr/bin/python
# coding:utf-8

import unittest
import solution


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = solution.Solution()
        return 

    def test_add_two(self):
        nums = [2, 7, 11, 15]
        target = 9
        res = self.solution.two_sum(nums, target)
        expect = [0, 1]
        self.assertEqual(res, expect)

    def test_add_two_numbers(self):
        l1 = solution.make_list([5])
        l2 = solution.make_list([5])
        res = self.solution.add_two_numbers(l1, l2)
        array = solution.list_to_array(res)
        self.assertEqual(array, [0, 1])


if __name__ == '__main__':
    unittest.main()

