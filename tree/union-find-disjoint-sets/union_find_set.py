# coding=utf-8

class UnionFindSet:
    """并查集"""

    def __init__(self, vertexs):
        self.disjoint_set = {}
        self.rank = {}
        self.vertexs = set(vertexs)
        for v in self.vertexs:
            self.disjoint_set[v] = v
            self.rank[v] = 1

    def find(self, v):
        if v not in self.disjoint_set:
            return

        if self.disjoint_set[v] == v:
            return v
        else:
            self.disjoint_set[v] = self.find(self.disjoint_set[v])
            return self.disjoint_set[v]


    def merge(self, v1: str, v2: str):
        p1, p2 = self.find(v1), self.find(v2)
        if p1 is None or p2 is None or p1 == p2:
            return

        if self.rank[p1] <= self.rank[p2]:
            # p1祖先为p2
            self.disjoint_set[p1] = p2
        else:
            self.disjoint_set[p2] = p1

        if self.rank[p1] == self.rank[p2]:
            self.rank[p2] += 1

    def is_connected(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)
        return p1 is not None and p2 is not None and p1 == p2

    def count_sets(self):
        s = set()
        for v in self.vertexs:
            s.add(self.find(v))
        return len(s)

    def get_roots(self):
        s = set()
        for v in self.vertexs:
            s.add(self.find(v))

        return list(s)
