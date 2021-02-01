#!/usr/bin/env python3
# coding=utf-8
"""Boyer-Moore算法
"""

def generate_bc(pattern: str) -> dict:
    """构建坏字符hash
    Args:
        pattern: 模式串
    Returns:
        dict key: char value: index
    """
    bc = {}
    for i, c in enumerate(pattern):
        bc[c] = i

    return bc

def generate_gs(pattern, suffix, prefix):
    """计算得到suffix和prefix数组
    """
    m = len(pattern)
    # for i in range(m):
    #     suffix[i] = -1
    #     prefix[i] = False

    for i in range(m - 1):
        # b[0, i]
        j, k = i, 0  # k为公共后缀子串长度
        while j >= 0 and pattern[j] == pattern[m - 1 - k]:
            # 和b[0, m - 1]求公共后缀子串
            j -= 1
            k += 1
            # 公共后缀子串在b[0, i]的起始下标
            suffix[k] = j + 1

        if j == -1:
            # 公共后缀子串是模式串的前缀子串
            prefix[k] = True

def move_by_gs(j, m, suffix, prefix):
    """计算好后缀移动距离
    """
    # 好后缀长度
    k = m - 1 - j
    if suffix[k] != -1:
        return j - suffix[k] + 1

    r = j + 2
    while r <= m - 1:
        if prefix[m - r]:
            return r
        r += 1

    return m


def bm(text, pattern):
    """bm匹配算法
    Args:
        text: 主串
        pattern: 模式串
    """
    n, m = len(text), len(pattern)
    if n < m:
        return -1

    bc = generate_bc(pattern)

    suffix = [-1] * m
    prefix = [False] * m
    generate_gs(pattern, suffix, prefix)

    i = 0
    while i <= n - m:
        # j表示主串和模式串匹配的第一个字符下标
        j = m - 1
        while j >= 0:
            if text[i + j] != pattern[j]:
                # 坏字符模式串下标: j
                break
            j -= 1

        if j < 0:
            # 匹配成功
            return i

        x = j - bc.get(text[i + j], -1)
        y = 0
        if j < m - 1:
            y = move_by_gs(j, m, suffix, prefix)

        i += max(x, y)

    return -1


if __name__ == '__main__':
    # 0
    print(bm("aaaaa", "aa"))
    # 1
    print(bm("abcdbabcd", "bcdba"))
    # 0
    print(bm("axbs", "axbs"))
    # -1
    print(bm("axb", "absd"))
    # 0
    print(bm("hello world", "h"))
    # 16
    print(bm("hello world this is string.", " is str"))
    # 5
    print(bm("哈哈, 好啊是吧", "啊是"))


