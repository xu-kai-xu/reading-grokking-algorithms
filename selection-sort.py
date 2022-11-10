# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 22:07:33 2022

@author: xuk11
"""
import numpy as np

nums = (np.random.random(100) * 100).tolist()

def findSmallest(nums):
    tmp = nums[0]
    tmp_idx = 0
    for i in range(1, len(nums)):  # 这里开头是1，因为0已经在开头给赋值了
        if tmp > nums[i]:
            tmp = nums[i]
            tmp_idx = i

    return tmp_idx

def selectionSort(nums):
    tmp = nums.copy()
    res = []
    while len(tmp) != 0:
        smallest_idx = findSmallest(tmp)
        res.append(tmp.pop(smallest_idx))

    return res

res = selectionSort(nums)

