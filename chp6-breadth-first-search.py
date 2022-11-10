# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 18:03:41 2022

@author: xuk11
"""
from collections import deque

graph = {}
graph['you'] = ['Bob', 'Alice', 'Claire']
graph['Bob'] = ['Anuj', 'Peggy']
graph['Alice'] = ['Peggy']
graph['Claire'] = ['Thom', 'Jonny']
graph['Anuj'] = []
graph['Peggy'] = []
graph['Thom'] = []
graph['Jonny'] = []

search_queue = deque()
search_queue += graph['you']


def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    checked_list = []  # 检查过的名字
    search_queue = deque()
    search_queue += graph[name]
    while search_queue:
        person = search_queue.popleft()  # 队列首拉出一个元素
        if person in checked_list:
            print(person + ' is searched!')
            continue
        else:
            checked_list.append(person)

        if person_is_seller(person):
            print(person + ' is a mango seller!')
            return True
        else:
            search_queue += graph[person]
            # 如果某个人不是卖芒果的，把他的朋友加入队列

    return False


search('you')




