#!/usr/bin/env python3
# coding=utf-8
import random

import max_heap
from max_heap import MaxHeap

def is_order(arr: list, asc=True):
    """判断数组是否有序"""
    if asc:
        p = arr[0]
        for v in arr[1:]:
            if v < p:
                return False
            p = v
        return True
    p = arr[0]
    for v in arr[1:]:
        if v > p:
            return False
        p = v
    return True


if __name__ == '__main__':
    a = [9, 4, 8, 6, 1, 23, 9, 91, 18, 7, 6, 10]
    heap = MaxHeap(len(a))
    for v in a:
        heap.insert(v)
    b = []
    v = heap.remove_top()
    while v is not None:
        b.append(v)
        v = heap.remove_top()

    print(b)

    # 原地堆排序
    print(a)
    max_heap.heap_sort(a)
    print(a)

    a.clear()

    for _ in range(100):
        a.append(random.randint(1, 1000))

    print(a)
    max_heap.heap_sort(a)
    print(a)
    assert(is_order(a))

