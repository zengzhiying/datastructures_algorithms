#!/usr/bin/env python3
# coding=utf-8

def bubble_sort(arr: list) -> None:
    """冒泡排序 升序排序
    原地排序, 空间复杂度: O(1)
    稳定排序
    时间复杂度: 最好O(n), 最坏O(n^2), 平均O(n^2)
    """
    n = len(arr)
    if n <= 1:
        return

    for i in range(n):
        flag = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
        # 没有任何交换时提前退出循环
        if not flag:
            break


if __name__ == '__main__':
    l = [2,3,6,1,5,8,9,9,7,6,8,10,5,11,7,19,12,16]
    bubble_sort(l)
    print(l)
