#!/usr/bin/env python3
# coding=utf-8


def binary_search(arr: list, value: int) -> int:
    """简单二分查找, 对升序的数组进行查找
    返回要查找元素的下标, 对于重复元素的下标返回不固定, 需要看数组长度的奇偶
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        # mid = (left + right) // 2
        mid = left + ((right - left) >> 1)
        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def binary_search_recursive(arr: list, left: int, right: int, value: int) -> int:
    """二分搜索递归方式"""
    if left > right:
        return -1

    mid = left + ((right - left) >> 1)
    if arr[mid] == value:
        return mid
    elif arr[mid] < value:
        return binary_search_recursive(arr, mid + 1, right, value)
    else:
        return binary_search_recursive(arr, left, mid - 1, value)

def binary_search_first(arr: list, value: int) -> int:
    """查找第一个等于给定值元素的下标
    高级写法, 非常精炼, 但是不容易读懂
    """
    n = len(arr)
    left, right = 0, n - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if arr[mid] >= value:
            right = mid - 1
        else:
            left = mid + 1

    if left < n and arr[left] == value:
        return left
    return -1

def binary_search_first2(arr: list, value: int) -> int:
    """查找第一个等于给定值元素的下标
    通俗的写法, 比较容易懂
    """
    n = len(arr)
    l, r = 0, n - 1
    while l <= r:
        mid = l + ((r - l) >> 1)
        if arr[mid] > value:
            r = mid - 1
        elif arr[mid] < value:
            l = mid + 1
        else:
            if mid == 0 or arr[mid - 1] != value:
                return mid
            # 不是第一个 继续缩小区间
            r = mid - 1

    return -1

def binary_search_last(arr: list, value: int) -> int:
    """查找最后一个等于给定值元素的下标
    """
    n = len(arr)
    l, r = 0, n - 1
    while l <= r:
        mid = l + ((r - l) >> 1)
        if arr[mid] > value:
            r = mid - 1
        elif arr[mid] < value:
            l = mid + 1
        else:
            if mid == n - 1 or arr[mid + 1] != value:
                return mid
            # 不是最后一个 继续缩小区间
            l = mid + 1

    return -1

def binary_search_first_gte(arr: list, value: int) -> int:
    """查找第一个大于或等于给定值元素的下标
    即优先等于, 没有的就选大于的
    """
    n = len(arr)
    l, r = 0, n - 1
    while l <= r:
        mid = l + ((r - l) >> 1)
        if arr[mid] >= value:
            # 一定是第一个
            if mid == 0 or arr[mid - 1] < value:
                return mid
            r = mid - 1
        else:
            l = mid + 1

    return -1

def binary_search_last_lte(arr: list, value: int) -> int:
    """查找最后一个小于或等于给定值元素的下标
    即优先等于, 没有就选小于的
    """
    n = len(arr)
    l, r = 0, n - 1
    while l <= r:
        mid = l + ((r - l) >> 1)
        if arr[mid] > value:
            r = mid - 1
        else:
            # 一定是最后一个
            if mid == n - 1 or arr[mid + 1] > value:
                return mid
            l = mid + 1

    return -1



if __name__ == '__main__':
    arr = [2,4,5,7,7,8,9,10,11,11,18,19,20,23,26]
    print(binary_search(arr, 11))

    print(binary_search_recursive(arr, 0, len(arr) - 1, 11))

    # 3
    print(binary_search_first(arr, 7))
    print(binary_search_first2(arr, 7))
    # 4
    print(binary_search_last(arr, 7))

    # 下面这两种带有不等关系的近似查找在平常业务用的更频繁
    arr = [2, 3, 6, 8, 9, 10]
    # 3
    print(binary_search_first_gte(arr, 7))
    # 1
    print(binary_search_last_lte(arr, 5))
    # 0
    print(binary_search_first_gte(arr, 1))
    # 5
    print(binary_search_last_lte(arr, 100))

