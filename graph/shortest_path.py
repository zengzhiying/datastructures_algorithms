#!/usr/bin/env python3
# coding=utf-8
from collections import deque

"""使用广度优先搜索寻找邻接字典表构建的图中的两点的一条最短路径
"""

# 1 - 2 - 5 - 7
# 1 - 9 - 5 - 7
graph = {
    1: set([2, 3, 9]),
    2: set([1, 4, 5]),
    3: set([1]),
    4: set([2]),
    5: set([2, 6, 7, 8,9]),
    6: set([5]),
    7: set([5]),
    8: set([5]),
    9: set([1, 5])
}

# 137
# graph = {
#     1: set([2, 3, 9]),
#     2: set([1, 4, 5]),
#     3: set([1, 7]),
#     4: set([2]),
#     5: set([2, 6, 7, 8,9]),
#     6: set([5]),
#     7: set([5,3]),
#     8: set([5]),
#     9: set([1, 5])
# }

def shortest_path(graph, start, end):
    d = deque()
    d.append(start)
    prev_nodes = {start:None}
    is_end = False
    while d:
        cur = d.popleft()
        if cur in graph:
            next_nodes = graph[cur]
            for node in next_nodes:
                if node in prev_nodes:
                    continue
                d.append(node)
                prev_nodes[node] = cur
                if node == end:
                    is_end = True
                    break
        if is_end:
            break

    if is_end:
        path = [end]
        prev = end
        while prev != start:
            prev = prev_nodes[prev]
            path.append(prev)
        return path[::-1]


if __name__ == '__main__':
    print(shortest_path(graph, 1, 7))

