# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 20:47:30 2022

@author: xuk11

grokking algorithm 算法书
chp4 quick sort
用递归的方法算加法
"""

inputs = [3, 5, 6, 3, 35, 56]
bis = [0, 1, 1, 3, 4, 9, 12, 15, 25]

def rec_sums(nums):
    # 输入为一个数的列表
    num_lst = nums.copy()
    if len(num_lst) == 0:
        return 0
    elif len(num_lst) == 1:
        return num_lst[0]
    else:
        pick = num_lst.pop()
        return pick + rec_sums(num_lst)


def count_list(nums):
    # 数列表中有多少个元素
    num_lst = nums.copy()
    if num_lst:
        num_lst.pop()
        return 1 + count_list(num_lst)
    else:
        return 0


def max_in_list(nums, tmp=0):
    # 找到列表中的最大数
    # 第二个参数初始值为0
    num_lst = nums.copy()
    if num_lst:
        tmp0 = tmp
        tmp1 = num_lst.pop()
        if tmp0 > tmp1:
            return max_in_list(num_lst, tmp0)
        else:
            return max_in_list(num_lst, tmp1)
    else:
        return tmp


def rec_binsearch(nums, target):
    num_lst = nums.copy()
    left = 0
    right = len(num_lst)
    mid = left + int((right - left) / 2)
    if num_lst[mid] > target:
        return rec_binsearch(nums[:mid], target)
    elif num_lst[mid] < target:
        return mid + 1 + rec_binsearch(nums[mid+1:], target)
    elif num_lst[mid] == target:
        return mid
    else:
        return -1



#t = rec_sums(inputs)
#s = count_list(inputs)
#m = max_in_list(inputs)
b = rec_binsearch(bis, 12)
