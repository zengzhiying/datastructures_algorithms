#!/usr/bin/env python3
# coding=utf-8
import random

def k_largest(arr: list, k: int) -> int:
    """搜索数组中第k大的元素
    """
    # 第k大和第len(arr) - k小等价
    return quick_select(0, len(arr) - 1, arr, len(arr) - k)

def partition(l, r, arr):
    """对数组按照左端为基准进行partition
    小的在左, 大的在右
    """
    v = arr[l]
    j = l

    for i in range(l + 1, r + 1):
        if arr[i] < v:
            arr[j + 1], arr[i] = arr[i], arr[j + 1]
            j += 1

    arr[j], arr[l] = arr[l], arr[j]
    return j

def random_partition(l, r, arr):
    """对数组随机partition, 可以减少不均衡的partition
    性能提升很大
    """
    rand_idx = l + int(random.random() * (r - l + 1))
    v = arr[rand_idx]
    # 和左端进行交换
    arr[l], arr[rand_idx] = arr[rand_idx], arr[l]
    j = l
    
    for i in range(l + 1, r + 1):
        if arr[i] < v:
            arr[j + 1], arr[i] = arr[i], arr[j + 1]
            j += 1
    arr[j], arr[l] = arr[l], arr[j]
    return j



def quick_select(l, r, arr, smallest_k):
    """按照快排思想不断进行区间partition
    smallest_k为第k个小的元素, 默认排序为从小到大
    """
    if l == r:
        return arr[l]
    # p = partition(l, r, arr)
    p = random_partition(l, r, arr)
    if p == smallest_k:
        return arr[smallest_k]
    elif p > smallest_k:
        # 在左侧
        return quick_select(l, p - 1, arr, smallest_k)
    else:
        # 在右侧
        return quick_select(p + 1, r, arr, smallest_k)

if __name__ == '__main__':
    nums = [3,2,1,5,6,4]
    print(k_largest(nums, 2))
    nums = [3,2,3,1,2,4,5,5,6]
    print(k_largest(nums, 4))

