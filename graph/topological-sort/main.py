#!/usr/bin/env python3
# coding=utf-8

from toposort import Graph

if __name__ == '__main__':
    g = Graph()
    # 5->2->3->7
    #       |
    # 6->1->*
    g.add_edge(5, 2)
    g.add_edge(2, 3)
    g.add_edge(1, 3)
    g.add_edge(6, 1)
    g.add_edge(3, 7)

    # 加环测试
    # g.add_edge(3, 1)

    s = g.toposort_kahn()
    print("依赖关系:", '->'.join([str(v) for v in s]))

    s1 = g.toposort_dfs()
    print("依赖关系:", '->'.join([str(v) for v in s1]))
