#!/usr/bin/python
# coding:utf-8


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def make_list(input_data):
    node_array = []
    for val in input_data:
        node = ListNode(val)
        node_array.append(node)
    for i in range(0, len(node_array)-1):
        node_array[i].next = node_array[i+1]
    return node_array[0]


def list_to_array(list_node):
    array = []
    while list_node is not None:
        array.append(list_node.val)
        list_node = list_node.next
    return array


class Solution(object):
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(0, length-1):
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [0, 0]                

    def add_two_numbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_array = list_to_array(l1)
        l2_array = list_to_array(l2)
        l1_length = len(l1_array)
        l2_length = len(l2_array)
        array = []
        last = 0
        for i in range(0, max(l1_length, l2_length)):
            a = 0
            if i <= l1_length - 1:
                a = l1_array[i]
            b = 0
            if i <= l2_length - 1:
                b = l2_array[i]
            temp = a + b + last
            last = temp / 10
            array.append(temp % 10)

        if last != 0:
            array.append(last)

        return make_list(array)

    def length_of_longest_substring(self, s):
        """
        :type s: str
        :rtype: int
        """
        

if __name__ == '__main__':
    exit(1)
