# coding=utf-8
"""力扣题目: 放置盒子, 计算最小占地面积
https://leetcode-cn.com/problems/building-boxes/
"""

def get_min_area(n):
    """时间复杂度最优算法
    """
    if n < 4:
        return n

    l = 2
    S = 3
    n -= 4
    while n > 0:
        l += 1
        S = l*(l + 1) // 2
        n -= S

    if n == 0:
        return S

    l -= 1
    n += S
    S = l*(l + 1) // 2

    delta = 1
    while n > 0:
        S += 1
        n -= delta
        delta += 1

    return S

def padding(n: int) -> int:
    """模拟填充方法计算, 复杂度高
    """
    if n < 4:
        return n

    l = 2
    S = 3
    n -= 4
    while n > 0:
        l += 1
        S = l*(l + 1) // 2
        n -= S

    if n == 0:
        return S

    l -= 1
    n += S
    S = l*(l + 1) // 2

    num = l + 1

    arr = []
    for i in range(l + 1, 0, -1):
        arr.append([0] * i)

    arr[0][0] = 1
    S += 1
    n -= 1
    if n == 0:
        return S

    index = 0
    for index in range(1, l + 1):
        arr[0][index] = 1
        S += 1
        n -= 1
        if n == 0:
            return S
        for i in range(1, l + 1):
            for j in range(0, l + 1 - i):
                if arr[i - 1][j] == 1 and arr[i - 1][j + 1] == 1 and arr[i][j] == 0:
                    arr[i][j] = 1
                    n -= 1
                    if n == 0:
                        return S
                    break
        


if __name__ == '__main__':
    print(get_min_area(51), padding(51))
    print(get_min_area(15), padding(15))
    print(get_min_area(103368013))
    # print(padding(103368013))

