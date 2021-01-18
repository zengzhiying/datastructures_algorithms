#!/usr/bin/env python3
# coding=utf-8
import random

import reverse_pair_counter as counter

if __name__ == '__main__':
    arr = [2, 4, 3, 1, 5, 6]
    arr1 = []
    for i in range(1000):
        arr1.append(random.randint(0, 100000))

    print(counter.enum_count(arr))
    print(counter.merge_sort_count(arr))
    print(arr)

    print(counter.enum_count(arr1))
    print(counter.merge_sort_count(arr1))
    a = arr1[0]
    for v in arr1[1:]:
        if v < a:
            print("Unordered array!")
            break

        a = v
    else:
        print("Array ordered!")
        
