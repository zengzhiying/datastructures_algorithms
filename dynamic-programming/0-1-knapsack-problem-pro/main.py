#!/usr/bin/env python3
# coding=utf-8
from knapsack_pro import knapsack_pro_two_dim
from knapsack_pro import knapsack_pro_list

weights = [2, 2, 4, 6, 3]
values = [3, 4, 8, 9, 6]
max_weights = 9

print("物品最大价值: %d" % knapsack_pro_two_dim(weights, values, max_weights))
print("物品最大价值: %d" % knapsack_pro_list(weights, values, max_weights))
