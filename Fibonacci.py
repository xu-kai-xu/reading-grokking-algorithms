# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 09:42:39 2022

@author: xuk11
"""
def feb(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return feb(n-1) + feb(n-2)

t = feb(20)