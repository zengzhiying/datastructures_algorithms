# coding=utf-8

def length(s1, s2):
    n, m = len(s1), len(s2)

    dp = []
    for _ in range(n):
        dp.append([0 for _ in range(m)])

    # init 第一行和列
    for j in range(m):
        if s1[0] == s2[j]:
            dp[0][j] = 1
        elif j != 0:
            dp[0][j] = dp[0][j - 1]
        else:
            dp[0][j] = 0


    for i in range(n):
        if s1[i] == s2[0]:
            dp[i][0] = 1
        elif i != 0:
            dp[i][0] = dp[i - 1][0]
        else:
            dp[i][0] = 0

    for i in range(1, n):
        for j in range(1, m):
            if s1[i] == s2[j]:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + 1)
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[n - 1][m - 1]

def get_str(s1, s2):
    """返回最长公共子串之一"""
    n, m = len(s1), len(s2)

    lcs = []

    dp = []
    # 第一行和第一列作为哨兵
    for _ in range(n + 1):
        dp.append([0 for _ in range(m + 1)])

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # dp[i - 1][j - 1]是最小的
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # length
    # dp[n][m]

    while n > 0 and m > 0:
        if s1[n - 1] == s2[m - 1]:
            lcs.append(s1[n - 1])
            n -= 1
            m -= 1
        elif dp[n - 1][m] >= dp[n][m - 1]:
            n -= 1
        else:
            m -= 1

    return ''.join(reversed(lcs))

