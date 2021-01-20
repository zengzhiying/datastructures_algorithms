#!/usr/bin/env python3
# coding=utf-8
from knapsack_pro import KnapsackPro

weights = [2, 2, 4, 6, 3]
values = [3, 4, 8, 9, 6]
max_weights = 9

k = KnapsackPro(weights, values, max_weights)
k.put(0, 0, 0)

print("背包中物品最大价值为: %d" % k.res_value)
print("物品列表: {}".format(k.res_items))
