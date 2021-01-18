# coding=utf-8

def knapsack_two_dim(weights, max_weight):
    """使用二维状态矩阵的动态规划解决背包问题
    Args:
        weights: 物品重量列表
        max_weight: 背包最大承受的重量
    """
    n = len(weights)
    states = []
    for i in range(n):
        states.append([])
        states[i] = [False] * (max_weight + 1)

    states[0][0] = True  # 哨兵
    if weights[0] <= max_weight:
        states[0][weights[0]] = True

    # 动态规划状态转移
    for i in range(1, n):
        # 不放第i个物品到背包
        for j in range(max_weight + 1):
            # 不放状态不发生变化
            if states[i - 1][j]:
                states[i][j] = states[i - 1][j]

        # 放第i个物品到背包
        for j in range(max_weight - weights[i] + 1):
            if states[i - 1][j]:
                states[i][j + weights[i]] = True

    # 最后一层结果即为符合要求的结果
    # 由后向前遍历[w, 0]
    for i in range(max_weight, -1, -1):
        if states[n - 1][i]:
            return i

    return 0

def knapsack(weights, max_weight):
    """使用一维数组实现状态转移"""
    n = len(weights)
    states = [False] * (max_weight + 1)

    states[0] = True
    if weights[0] <= max_weight:
        states[weights[0]] = True

    for i in range(1, n):
        # 不放不进行任何修改 这里只有放入的判断即可
        # 必须从大到小循环 否则会重复计算
        for j in range(max_weight - weights[i], -1, -1):
            if states[j]:
                states[j + weights[i]] = True

    # 得出结果
    for i in range(max_weight, -1, -1):
        if states[i]:
            return i

    return 0


