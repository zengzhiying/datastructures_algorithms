# coding=utf-8

def distance(s1, s2):
    n, m = len(s1), len(s2)

    # 存在拷贝问题
    # dp = [[0] * m] * n
    dp = []
    for i in range(n):
        dp.append([0 for _ in range(m)])


    # init行
    for i in range(m):
        if s1[0] == s2[i]:
            dp[0][i] = i
        elif i != 0:
            dp[0][i] = dp[0][i - 1] + 1
        else:
            dp[0][i] = 1

    # init列
    for i in range(n):
        if s1[i] == s2[0]:
            dp[i][0] = i
        elif i != 0:
            dp[i][0] = dp[i - 1][0] + 1
        else:
            dp[i][0] = 1


    # 按行填表
    for i in range(1, n):
        for j in range(1, m):
            if s1[i] == s2[j]:
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1])
            else:
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)

    return dp[n - 1][m - 1]
