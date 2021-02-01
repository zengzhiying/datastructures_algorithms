#!/usr/bin/env python3
# coding=utf-8
"""Robin-Karp算法
"""

def _hash(s):
    res = 0
    m = len(s)
    for i, c in enumerate(s):
        num = ord(c) - 97
        res += num * 26 ** (m - i - 1)

    return res


def rk(text, pattern):
    """Robin-Karp算法
    Args: 
        text: text和hash选择相关, 这里选择26进制结果作为hash, text只能为26个小写字母
        pattern: 模式串
    """
    n, m = len(text), len(pattern)
    if n < m:
        return -1

    p_hash = _hash(pattern)

    # 构建m次幂数组
    pw = []
    for i in range(m):
        pw.append(26 ** i)

    # hash值共用
    h = [0] * (n - m + 1)
    h[0] = _hash(text[:m])
    if h[0] == p_hash and text[:m] == pattern:
        return 0

    for i in range(1, n - m + 1):
        h[i] = 26 * (h[i - 1] - pw[m - 1] * (ord(text[i - 1]) - 97)) + ord(text[i + m - 1]) - 97
        if h[i] == p_hash and text[i:i + m] == pattern:
            return i

    return -1


if __name__ == '__main__':
    # 0
    print(rk("aaaaa", "aa"))
    # 1
    print(rk("abcdbabcd", "bcdba"))
    # 0
    print(rk("axbs", "axbs"))
    # -1
    print(rk("axb", "absd"))
    # 0
    print(rk("hello world", "h"))
    # 16
    print(rk("hello world this is string.", " is str"))

