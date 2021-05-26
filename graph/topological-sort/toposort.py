# coding=utf-8
from collections import defaultdict

class Graph:
    """拓扑排序应用对象为有向无环图"""
    def __init__(self):
        self.adj = defaultdict(list)

    def add_edge(self, f, t):
        """添加有向边 f->t
        """
        self.adj[f].append(t)

    def toposort_kahn(self):
        # 统计所有顶点的入度
        in_degree = defaultdict(int)

        for _, vs in self.adj.items():
            for v in vs:
                in_degree[v] += 1

        # 将入度为0的加入队列
        queue = []
        for v in self.adj:
            if in_degree[v] == 0:
                queue.append(v)

        seq = []

        while queue:
            w = queue.pop(0)
            # print('->', w, end='')
            seq.append(w)
            for v in self.adj[w]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        if len(seq) < len(self.adj):
            print("图存在环!")

        return seq

    def toposort_dfs(self):
        #构建逆邻接表
        inverse_adj = defaultdict(list)
        for v, vs in self.adj.items():
            for w in vs:
                inverse_adj[w].append(v)

        self.sequence = []

        visited = set()

        for v in self.adj:
            if v not in visited:
                visited.add(v)
                self._dfs(v, inverse_adj, visited)

        return self.sequence

    def _dfs(self, v, inverse_adj, visited):
        for w in inverse_adj[v]:
            if w not in visited:
                visited.add(w)
                self._dfs(w, inverse_adj, visited)

        # 先打印完其他的最后打印自己
        self.sequence.append(v)


