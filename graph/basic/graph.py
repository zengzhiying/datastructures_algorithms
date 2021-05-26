# coding=utf-8
from collections import deque

class Graph:
    """无向图类"""

    def __init__(self):
        self.adj = {}

    def add_vertex(self, v):
        """添加顶点"""
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, f, t):
        """每条边存两次"""
        self.adj[f].append(t)
        self.adj[t].append(f)

    def bfs(self, s, t):
        """Breadth-First-Search: 广度优先搜索
        搜索s -> t的路径
        """
        if s == t:
            return

        # 顶点遍历缓存
        visited = {s}
        # 前驱顶点缓存
        prev = {}

        queue = deque()
        queue.append(s)

        while queue:
            w = queue.popleft()
            for q in self.adj[w]:
                if q not in visited:
                    prev[q] = w
                    if q == t:
                        self.path = []
                        self.get_path(prev, s, t)
                        print('->'.join(self.path))
                        return
                    visited.add(q)
                    queue.append(q)

    def get_path(self, prev, s, t):
        """打印路径"""
        if t != s:
            self.get_path(prev, s, prev[t])

        self.path.append(t)

    def dfs(self, s, t):
        """Depth-First-Search: 深度优先搜索
        搜索s -> t的一条路径, 不一定最短
        """
        self.is_found = False

        visited = set()
        prev = {}

        # 统计回溯次数
        # self.cnum = 0

        self.backtrack(s, t, visited, prev)

        self.path = []
        self.get_path(prev, s, t)
        print('->'.join(self.path))
        # print(self.cnum)

    def backtrack(self, w, t, visited, prev):
        """dfs回溯
        w为当前的节点
        """
        # self.cnum += 1
        if self.is_found:
            return
        
        visited.add(w)
        if w == t:
            self.is_found = True
            return

        for q in self.adj[w]:
            # if self.is_found:
            #     return
            if q not in visited:
                prev[q] = w
                self.backtrack(q, t, visited, prev)


