# coding=utf-8
"""双十一购物车最佳凑单满减
"""

def shopping(items, condition):
    """
    Args:
        items: 商品列表
        condition: 满减金额条件
    """
    # 购买商品最大金额不超过满减的2倍, 否则就认为不划算了
    n = len(items)
    max_amount = 2 * condition

    states = [[False] * (max_amount + 1) for _ in range(n)]

    states[0][0] = True
    if items[0] <= max_amount:
        states[0][items[0]] = True

    for i in range(1, n):
        # 不购买第i个商品
        for j in range(max_amount + 1):
            if states[i - 1][j]:
                states[i][j] = states[i - 1][j]

        # 购买第i个商品
        for j in range(max_amount - items[i] + 1):
            if states[i - 1][j]:
                states[i][j + items[i]] = True

    j = condition
    while j < max_amount + 1:
        if states[n - 1][j]:
            break
        j += 1

    # 循环到最后没有break 即没有可行解
    if j == max_amount + 1:
        return

    # 要购买的商品列表
    shop_items = []
    for i in range(n - 1, 0, -1):
        if j - items[i] >= 0 and states[i - 1][j - items[i]]:
            shop_items.append((i, items[i]))
            j = j - items[i]

    if j != 0:
        shop_items.append((0, items[0]))

    return shop_items


