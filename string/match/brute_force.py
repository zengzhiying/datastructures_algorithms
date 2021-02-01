#!/usr/bin/env python3
# coding=utf-8
"""暴力匹配字符串算法
"""

def bf(text, pattern):
    """brute force算法
    Args:
        text: 文本字符串
        pattern: 模式字符串
    Returns:
        匹配到返回第一次匹配的下标
        匹配不到返回-1
    """
    n, m = len(text), len(pattern)
    if n < m:
        return -1

    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            return i

    return -1



if __name__ == '__main__':
    # 0
    print(bf("aaaaa", "aa"))
    # 1
    print(bf("abcdbabcd", "bcdba"))
    # 0
    print(bf("axbs", "axbs"))
    # -1
    print(bf("axb", "absd"))
    # 11
    print(bf("2891sbs01b2211", "211"))
    # 0
    print(bf("hello world", "h"))

