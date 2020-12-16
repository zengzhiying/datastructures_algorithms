# coding=utf-8

class MaxHeap:
    """大顶堆"""
    def __init__(self, capacity):
        self.arr = [None] * (capacity + 1)
        self.cap = capacity
        self.count = 0

    def insert(self, data):
        """插入元素"""
        if self.count >= self.cap:
            return

        self.count += 1
        # 先把元素放完全二叉树最后位置
        self.arr[self.count] = data

        # 从下往上堆化
        i = self.count
        while i // 2 > 0 and self.arr[i] > self.arr[i // 2]:
            self.arr[i], self.arr[i // 2] = self.arr[i // 2], self.arr[i]
            i //= 2

    def remove_top(self):
        """删除堆顶元素 并返回"""

        if self.count == 0:
            return

        res = self.arr[1]
        # 直接用最后1个元素覆盖堆顶元素
        self.arr[1] = self.arr[self.count]
        self.count -= 1

        # 然后下沉堆顶元素
        a = self.arr
        i, n = 1, self.count
        while True:
            max_pos = i
            l = i << 1
            r = l + 1
            if l <= n and a[i] < a[l]:
                max_pos = l
            if r <= n and a[max_pos] < a[r]:
                max_pos = r
            if max_pos == i:
                break
            a[i], a[max_pos] = a[max_pos], a[i]
            i = max_pos

        return res

def heap_sort(arr: list):
    """堆排序 升序排序"""
    build_heap(arr)
    k = len(arr) - 1
    while k > 1:
        arr[1], arr[k] = arr[k], arr[1]
        k -= 1
        heapify(arr, k, 1)

    arr.remove(0)


def build_heap(arr: list):
    """在数组上原地创建堆"""
    n = len(arr)
    # 插入占位
    arr.insert(0, 0)
    i = n // 2
    while i >= 1:
        heapify(arr, n, i)
        i -= 1

    # arr.remove(0)
    
def heapify(arr: list, n: int, i: int):
    """堆中第i个元素下沉"""
    while True:
        max_pos = i
        l = i << 1
        r = l + 1
        if l <= n and arr[i] < arr[l]:
            max_pos = l
        if r <= n and arr[max_pos] < arr[r]:
            max_pos = r
        if max_pos == i:
            break
        arr[i], arr[max_pos] = arr[max_pos], arr[i]
        i = max_pos


