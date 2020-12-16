#!/usr/bin/env python3
# coding=utf-8

"""网上摘录的基于的bfs实现的图的最短路径和全部路径搜索的代码
来源页面: https://blog.csdn.net/brightzelool/article/details/73730152
下面的算法需要记录所有已经走的路径追加进去，因此占用的空间比较大, 性能不好, 这里仅作为参考
"""

graph = {
    '1': ['2', '3', '4'],
    '2': ['5', '6'],
    '5': ['9', '10'],
    '4': ['7', '8'],
    '7': ['11', '12']
}

def bfs_shortest_path(graph, start, end):
    """单条最短路径搜索"""
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

print(bfs_shortest_path(graph, '1', '11'))

graph = {
    1: [2, 3, 4],
    2: [5, 6],
    3: [4,11],
    5: [9, 10],
    4: [7, 8],
    7: [11, 12]
}
 
def bfs_all_paths(graph, start, end):
    """所有的路径搜索"""
    # maintain a queue of paths
    queue = []
    allpath = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            allpath.append(path)
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)
    return allpath
 
print(bfs_all_paths(graph, 1, 11))
 
