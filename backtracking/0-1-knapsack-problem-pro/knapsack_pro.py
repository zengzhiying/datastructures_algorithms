# coding=utf-8
from functools import lru_cache

class KnapsackPro:
    """0-1背包问题升级版
    保证不超过背包承重条件下 物品总价值最大
    """
    def __init__(self, weights, values, max_weight):
        """
        Args:
            weights: 物品重量列表
            values: 物品价值列表
            max_weight: 背包最大承重
        """
        self.weights = weights
        self.values = values
        self.max_weight = max_weight
        self.num = len(weights)

        self.res_value = 0
        self.res_items = None

        self.items = []

    @lru_cache(maxsize=128)
    def put(self, i, cw, cv):
        """往背包放入物品
        Args:
            i: 当前物品的下标
            cw: 当前背包的重量
            cv: 当前背包中物品的总价值
        """
        if cw == self.max_weight or i == self.num:
            if cv > self.res_value:
                self.res_value = cv
                # print("items: {}".format(self.items))
                # 更新物品列表
                self.res_items = self.items[:]
            return

        # 不放入第i个物品
        self.put(i + 1, cw, cv)
        # 放入第i个物品
        if cw + self.weights[i] <= self.max_weight:
            # 物品入栈
            self.items.append(i)
            self.put(i + 1, cw + self.weights[i], cv + self.values[i])
            # 物品弹出
            self.items.pop()

