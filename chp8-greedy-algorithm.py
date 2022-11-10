# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 18:00:51 2022

@author: xuk11

所谓贪心，就是每次都选最大的、最多的、最好的、最贵的。
"""

states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()

while states_needed:
    best_station = None  # 最佳广播站
    states_covered = set()  # 已经覆盖的广播站

    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)


print(final_stations)












