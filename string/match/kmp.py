#!/usr/bin/env python3
# coding=utf-8
"""knuth Morris Pratt字符串匹配算法
"""

def kmp(t, p):
    """kmp算法
    Args:
        t: 主串
        p: 模式串
    """
    i, j = 0, 0
    n, m = len(t), len(p)
    next_arr = get_next(p)

    while i < n and j < m:
        if j == -1 or t[i] == p[j]:
            i += 1
            j += 1
        else:
            j = next_arr[j]

    if j == m:
        return i - j
    else:
        return -1

def get_next(p):
    next_arr = [0] * (len(p) + 1)
    next_arr[0] = -1
    i, j = 0, -1
    while i < len(p):
        if j == -1 or p[i] == p[j]:
            i += 1
            j += 1
            next_arr[i] = j
        else:
            j = next_arr[j]

    return next_arr

if __name__ == '__main__':
    # 0
    print(kmp("aaaaa", "aa"))
    # 1
    print(kmp("abcdbabcd", "bcdba"))
    # 0
    print(kmp("axbs", "axbs"))
    # -1
    print(kmp("axb", "absd"))
    # 0
    print(kmp("hello world", "h"))
    # 16
    print(kmp("hello world this is string.", " is str"))
    # 5
    print(kmp("哈哈, 好啊是吧", "啊是"))

