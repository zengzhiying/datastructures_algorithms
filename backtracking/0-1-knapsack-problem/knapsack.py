# coding=utf-8
from functools import lru_cache

class Knapsack:
    def __init__(self, weights, max_weight):
        """
        Args:
            weights: 当前物品的重量列表
            max_weight: 背包所能承受的最大重量
        """
        self.res_weight = 0
        self.weights = weights
        self.max_weight = max_weight
        self.num = len(weights)  # 物品个数

    @lru_cache(maxsize=128)
    def put(self, i, cw):
        """往背包放入物品
        Args:
            i: 当前物品的下标
            cw: 当前背包的重量
        """
        if cw == self.max_weight or i == self.num:
            if cw > self.res_weight:
                self.res_weight = cw
            return

        # 枚举: 不装第i个跳到下一个
        self.put(i + 1, cw)
        # 枚举: 装入第i个跳到下一个
        if cw + self.weights[i] <= self.max_weight:
            self.put(i + 1, cw + self.weights[i])
