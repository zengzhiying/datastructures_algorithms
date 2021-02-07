#!/usr/bin/env python3
# coding=utf-8
from union_find_set import UnionFindSet

if __name__ == '__main__':
    edges = [('a', 'b'), ('b', 'c'), ('b', 'a'), ('a', 'c'), ('a', 'e'), ('d', 'o'), ('d', 'p'), ('d', 'q')]
    vertexs = set()
    for v1, v2 in edges:
        vertexs.add(v1)
        vertexs.add(v2)

    ufs = UnionFindSet(vertexs)
    for v1, v2 in edges:
        ufs.merge(v1, v2)

    print(ufs.find('b'))
    print(ufs.find('c'))
    print(ufs.find('a'))

    print(ufs.find('p'))

    print(ufs.count_sets())

    print(ufs.get_roots())

    print(ufs.is_connected('c', 'e'))
    print(ufs.is_connected('d', 'b'))
