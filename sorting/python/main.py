#!/usr/bin/env python3
# coding=utf-8
import random
import copy
import time

from merge_sort import merge_sort
from quick_sort import quick_sort

if __name__ == '__main__':
    arr = [1, 6, 2, 7, 5, 9, 8]
    merge_sort(arr)
    print(arr)

    arr = [1, 6, 2, 7, 5, 9, 8]
    quick_sort(arr)
    print(arr)

    arr = []
    for i in range(100000):
        arr.append(random.randint(1, 1000000))
    arr1 = copy.copy(arr)

    t1 = time.time()
    merge_sort(arr)
    t2 = time.time()
    print("merge sort: %.2fs" % (t2 - t1))
    tmp = arr[0]
    for v in arr[1:]:
        assert v >= tmp
        tmp = v

    assert arr != arr1

    t1 = time.time()
    quick_sort(arr1)
    t2 = time.time()
    print("quick sort: %.2fs" % (t2 - t1))
    tmp = arr1[0]
    for v in arr1[1:]:
        assert v >= tmp
        tmp = v


