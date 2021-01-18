#!/usr/bin/env python3
# coding=utf-8

from knapsack import Knapsack

if __name__ == '__main__':
    weights = [2,2,4,6,3]
    max_weight = 9
    k = Knapsack(weights, max_weight)
    k.put(0, 0)
    print("背包最大重量为: %d" % k.res_weight)
