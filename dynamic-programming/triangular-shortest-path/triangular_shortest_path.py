# coding=utf-8

def shortest_path(triangle):
    """计算三角形从上到下移动的最短路径
    Args:
        triangle: 三角形数组, 格式如: [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14, 15]]
    Returns:
        移动的最小节点值之和
    """
    n = len(triangle)
    dp = [[0] * (n + 1)] * (n + 1)

    # 动态规划反向递推: 最小(i, j) => (i + 1, j)和(i + i, j + 1)的最小值 + i, j节点值
    for i in range(n - 1, -1, -1):
        for j in range(i + 1):
            dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]

    return dp[0][0]
