# coding=utf-8
import random

def quick_sort(arr):
    __quick_sort(arr, 0, len(arr) - 1)

def __quick_sort(arr, l, r):
    if l >= r:
        return
    p = __partition(arr, l, r)
    __quick_sort(arr, l, p - 1)
    __quick_sort(arr, p + 1, r)

def __partition(arr, l, r):
    p = random.randint(l, r)
    arr[r], arr[p] = arr[p], arr[r]

    # 原地分区
    i = l
    for j in range(l, r):
        if arr[j] < arr[r]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    # 交换 i 和 r
    arr[i], arr[r] = arr[r], arr[i]
    return i
