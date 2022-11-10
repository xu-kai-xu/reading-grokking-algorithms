# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 10:12:29 2022

@author: xuk11
"""
# hash table of the graph
graph = {}

graph['start'] = {}
graph['start']['a'] = 5
graph['start']['b'] = 2


graph['a'] = {}
graph['a']['d'] = 4
graph['a']['c'] = 2

graph['b'] = {}
graph['b']['a'] = 8
graph['b']['c'] = 7

graph['c'] = {}
graph['c']['fin'] = 1

graph['d'] = {}
graph['d']['c'] = 6
graph['d']['fin'] = 3

graph['fin'] = {}

# hash table of the costs
infinity = float('inf')
costs = {}
costs['a'] = 5
costs['b'] = 2
costs['c'] = infinity
costs['d'] = infinity
costs['fin'] = infinity

# hash table of the parents
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['c'] = None
parents['d'] = None
parents['fin'] = None  # 初始化的时候其实没有的

# 记录已经处理过的节点
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if (cost < lowest_cost) and (node not in processed):
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def find_path(parents_table, start, end):
    # 从parents表中反向查找，最终找到start
    # dest 表示终点节点的名字
    path = []
    path.append(end)
    site = parents_table[end]
    while True:
        if site == start:
            path.append(start)
            break
        else:
            path.append(site)
            site = parents_table[path[-1]]
    return path[::-1]


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)


res = find_path(parents, 'start', 'fin')
