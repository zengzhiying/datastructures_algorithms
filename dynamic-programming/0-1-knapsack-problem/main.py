#!/usr/bin/env python3
# coding=utf-8
from knapsack import knapsack_two_dim
from knapsack import knapsack

if __name__ == '__main__':
    weights = [2,2,4,6,3]
    max_weight = 9
    w = knapsack_two_dim(weights, max_weight)
    print("背包最大重量为: %d" % w)

    w = knapsack(weights, max_weight)
    print("背包最大重量为: %d" % w)

