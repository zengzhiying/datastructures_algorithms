#!/usr/bin/env python3
# coding=utf-8

def counting_sort(arr: list) -> None:
    """计数排序算法
    arr数组的范围不要太大, 且都是正整数或0(对于负整数要通过变换转换到正整数范围)
    计数排序是桶排序的一种特殊情况
    """
    maximum = max(arr)

    c = [0 for _ in range(maximum + 1)]

    # 计算元素个数放入c中
    for v in arr:
        c[v] += 1

    # 依次累加
    for i in range(1, maximum + 1):
        c[i] += c[i - 1]

    # 临时数组存储排序之后的结果
    r = arr[:]

    for i in range(len(arr) - 1, -1, -1):
        index = c[arr[i]] - 1
        r[index] = arr[i]
        c[arr[i]] -= 1

    # 拷贝结果r到arr
    arr[:] = r[:]

class Score(object):
    """学生和分数类"""
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f"name: {self.name} and score: {self.score}"
        

def score_counting_sort(arr: list) -> None:
    """使用计数排序对学生分数进行排序
    要点: 相同分数的学生 排序后仍保持原有顺序
    """
    maximum = arr[0].score
    n = len(arr)
    for i in range(1, n):
        if maximum < arr[i].score:
            maximum = arr[i].score

    c = [0 for _ in range(maximum + 1)]
    for v in arr:
        c[v.score] += 1

    # 累加
    for i in range(1, maximum + 1):
        c[i] += c[i - 1]

    r = arr[:]

    # 排序关键步骤
    for i in range(n - 1, -1, -1):
        index = c[arr[i].score] - 1
        r[index] = arr[i]
        c[arr[i].score] -= 1

    # 拷贝结果回去
    arr[:] = r[:]



if __name__ == '__main__':
    arr = [5,3,2,1,8,9,6,3,1,0,9,10,1]
    print(arr)
    counting_sort(arr)
    print(arr)

    scores = [
        Score("小明", 8),
        Score("小华", 6),
        Score("小颖", 9),
        Score("小丽", 7),
        Score("小花", 5),
        Score("小米", 6),
        Score("小橙", 7)
    ]
    print([str(v) for v in scores])
    score_counting_sort(scores)
    print([str(v) for v in scores])

