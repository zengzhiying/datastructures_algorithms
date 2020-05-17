#!/usr/bin/env python3
# coding=utf-8

def radix_sort(arr: list, digits: int) -> None:
    """基数排序算法,
    给定数组和位数进行排序, 传入参数时要保证位数是相等的
    """
    for i in range(1, digits + 1):
        counting_sort(arr, digits - i)


def counting_sort(arr: list, idx: int) -> None:
    """计数排序算法
    idx进行排序的下标, 至于下标如何控制在调用的时候进行传递
    """
    maximum = max(arr, key=lambda x: x[idx])[idx]
    n = len(arr)

    c = [0 for _ in range(maximum + 1)]

    # 统计个数
    for v in arr:
        c[v[idx]] += 1

    # 累加
    for i in range(1, maximum + 1):
        c[i] += c[i - 1]

    r = [0] * n

    for i in range(n - 1, -1, -1):
        index = c[arr[i][idx]] - 1
        r[index] = arr[i]
        c[arr[i][idx]] -= 1

    arr[:] = r[:]



def get_digit_number(num, n):
    """获取数字的倒数第n位的值
    """
    # for _ in range(n - 1):
    #     num //= 10
    num //= 10 ** (n - 1)
    return num % 10

if __name__ == '__main__':
    arr = [
        15782819210,
        15798921098,
        16635492010,
        17890291092,
        17890291093,
        17990291093,
        17890291092,
        18809298192,
        19829817202,
        13809287162,
        18278386191,
        17468462582,
        16367352973,
        13639627392,
    ]
    # 数据源排序之前要整理成基数位的tuple结果, 这样避免排序时现做转换, 排序后再统一进行合并
    # 用在正式的环境中效率比较好
    arr_by_radix = []
    for v in arr:
        tmp = [0] * 11
        for i in range(1, 12):
            tmp[11 - i] = get_digit_number(v, i)
        arr_by_radix.append(tmp)

    radix_sort(arr_by_radix, 11)
    for v in arr_by_radix:
        print(int(''.join([str(x) for x in v])))



