# coding=utf-8
"""分治法的案例: 数组序列中逆序对个数统计
"""

def enum_count(arr):
    """暴力方法统计逆序对个数
    复杂度: O(n^2)
    """
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                count += 1

    return count


MERGE_COUNT = [0]


def merge_sort_count(arr):
    """采用分支思想 借助归并排序的过程中子数组的合并过程来统计逆序对个数
    复杂度: O(nlogn)
    """
    MERGE_COUNT[0] = 0
    merge_sort(arr, 0, len(arr) - 1)
    return MERGE_COUNT[0]

def merge_sort(arr, l, r):
    if l >= r:
        return
    mid = (l + r) // 2
    merge_sort(arr, l, mid)
    merge_sort(arr, mid + 1, r)
    # 合并
    merge(arr, l, mid, r)


def merge(arr, l, mid, r):
    i, j, k = l, mid + 1, 0
    tmp_arr = [0] * (r - l + 1)

    while i <= mid and j <= r:
        if arr[i] <= arr[j]:
            tmp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            # 存在逆序对 个数是从i -> mid的元素个数, 闭区间
            MERGE_COUNT[0] += (mid - i + 1)  # 仅增加这1行代码用于统计

            tmp_arr[k] = arr[j]
            k += 1
            j += 1

    # 处理剩余元素
    while i <= mid:
        tmp_arr[k] = arr[i]
        k += 1
        i += 1

    while j <= r:
        tmp_arr[k] = arr[j]
        k += 1
        j += 1

    # 更新原数组
    for i in range(l, r + 1):
        arr[i] = tmp_arr[i - l]


