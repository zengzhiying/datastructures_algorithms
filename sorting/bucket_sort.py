#!/usr/bin/env python3
# coding=utf-8

def bucket_sort(arr: list, bucket_size: int) -> None:
    """桶排序算法
    Args:
        arr: 待排序的列表, 其中元素只能为整数, 而且建议分布不要太分散
        bucket_size: 每个桶能容纳不同的元素个数, 要根据数组做合理设置
    """
    maximum, minimum = max(arr), min(arr)

    # 桶个数
    number_bucket = (maximum - minimum) // bucket_size + 1

    # 分配桶
    buckets = [[] for _ in range(number_bucket)]

    # 放置元素
    for v in arr:
        i = (v - minimum) // bucket_size
        buckets[i].append(v)

    # 单独对每个桶内数据排序
    i = 0
    for bucket in buckets:
        bucket.sort()
        for v in bucket:
            arr[i] = v
            i += 1

if __name__ == '__main__':
    arr = [-7, 51, 3, 121, -3, 32, 21, 43, 4, 25, 56, 77, 16, 22, 87, 56, -10, 68, 99, 70]
    print(arr)
    bucket_sort(arr, 10)
    print(arr)

