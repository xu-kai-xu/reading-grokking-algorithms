# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 13:20:37 2022

@author: xuk11

grokking algorithm
chap 4 quick sort
"""

nums = [1, 5, 6, 4, 23, 23, 124, 7, 0, 78, 9]

def quicksort(num_list):
    num_lst = num_list.copy()
    if len(num_lst) < 2:
        return num_lst
    else:
        pivot = num_lst[int(len(num_lst) / 2)]
        num_lst.remove(pivot)
        less = [i for i in num_lst if i <= pivot]
        greater = [i for i in num_lst if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


quicksort(nums)
