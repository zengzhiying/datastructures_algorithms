# coding=utf-8

def knapsack_pro_two_dim(weights, values, max_weight):
    """基于二维数组动态规划解决背包问题升级版, 计算背包所能装入物品的最大价值
    Args:
        weights: 物品重量列表
        values: 物品价值列表
        max_weight: 背包最大承重
    Returns:
        物品的最大价值
    """
    n = len(weights)

    states = []
    for i in range(n):
        states.append([])
        for j in range(max_weight + 1):
            states[i].append(-1)

    states[0][0] = 0
    if weights[0] <= max_weight:
        states[0][weights[0]] = values[0]

    for i in range(1, n):
        for j in range(max_weight + 1):
            # 不放入第i个物品
            if states[i - 1][j] >= 0:
                states[i][j] = states[i - 1][j]

        for j in range(max_weight - weights[i] + 1):
            # 放入第i个物品
            if states[i - 1][j] >= 0:
                v = states[i - 1][j] + values[i]
                if v > states[i][j + weights[i]]:
                    states[i][j + weights[i]] = v

    # 找出最大值
    return max(states[n - 1])

def knapsack_pro_list(weights, values, max_weight):
    """一维数组动态规划解决背包问题升级版
    """
    n = len(weights)

    states = [-1] * (max_weight + 1)
    
    states[0] = 0
    if weights[0] <= max_weight:
        states[weights[0]] = values[0]

    for i in range(1, n):
        # 只有放入状态即可 不放入不做任何变化
        for j in range(max_weight - weights[i], -1, -1):
            if states[j] >= 0:
                v = states[j] + values[i]
                if v > states[j + weights[i]]:
                    states[j + weights[i]] = v
                    

    return max(states)

