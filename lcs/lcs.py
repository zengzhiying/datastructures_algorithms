# coding=utf-8

import numpy as np

def __get_lcs_length_and_mark(x, y):
    """获取两个待比较序列的打分和标记矩阵
    Args:
        x: 待比对序列1
        y: 待比对序列2
    Returns:
        返回dp和mark两个矩阵所组成的元组
        其中dp[len(x), len(y)]为lcs的长度
        mark为存放标记的矩阵，用于后面计算序列本身使用
    """
    dp = np.zeros((len(x) + 1, len(y) + 1))
    mark = np.zeros((len(x) + 1, len(y) + 1))
    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            if x[i - 1] == y[j - 1]:
                dp[i, j] = dp[i - 1, j - 1] + 1
                mark[i, j] = 1
            else:
                if dp[i - 1, j] >= dp[i, j - 1]:
                    dp[i, j] = dp[i - 1, j]
                    mark[i, j] = 2
                else:
                    dp[i, j] = dp[i, j - 1]
                    mark[i, j] = 3

    return dp, mark

def get_lcs(x, y):
    """通过矩阵回溯计算x和y的最长公共子序列
    参数和上述函数一致
    Returns:
        返回两个序列的最长公共子序列, 类型: list
    """
    dp, mark = __get_lcs_length_and_mark(x, y)
    x_length = len(x)
    y_length = len(y)
    lcs = []
    while x_length > 0 and y_length > 0:
        if mark[x_length, y_length] == 1:
            lcs.insert(0, x[x_length - 1])
            x_length -= 1
            y_length -= 1
        elif mark[x_length, y_length] == 2:
            x_length -= 1
        elif mark[x_length, y_length] == 3:
            y_length -= 1
        else:
            break
    return lcs

if __name__ == '__main__':
    # x = np.array([1,2,3,5,6])
    # y = np.array([2,3,5,7,6,9,8])
    x = [0,2,5,7,8,10]
    y = [0,3,5,7,9,10,11]
    rs = get_lcs(x, y)
    print(rs)
