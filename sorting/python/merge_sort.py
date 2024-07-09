# coding=utf-8

def merge_sort(arr):
    __merge_sort(arr, 0, len(arr) - 1)

def __merge_sort(arr, l, r):
    if l >= r:
        return
    m = (l + r) // 2
    __merge_sort(arr, l, m)
    __merge_sort(arr, m + 1, r)

    # 合并子数组
    __merge(arr, l, r)

def __merge(arr, l, r):
    m = (l + r) // 2
    i, j = l, m + 1
    tmp = []
    while i <= m and j <= r:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
    for p in range(i, m + 1):
        tmp.append(arr[p])
    for p in range(j, r + 1):
        tmp.append(arr[p])
    arr[l:r + 1] = tmp
