#!/usr/bin/python3 env
# coding=utf-8

# 采用邻接表实现图, 邻接表默认为array的形式
# 这里实现将图的最外层叶子结点裁减掉, 为方便裁剪使用字典表实现

#       G  I
#       |  |
# A——B——D——E——H 
#    |  |     |
#    C  F     J
# 上面的树裁剪一层叶子结点后应为: B——D——E——H

def remove_leaf_nodes(graph):
    leaf_nodes = []
    for n, adj in graph.items():
        if not adj:
            leaf_nodes.append(n)
        elif len(adj) == 1:
            leaf_nodes.append(n)

    for leaf in leaf_nodes:
        del graph[leaf]
        for n, adj in graph.items():
            if leaf in adj:
                graph[n].remove(leaf)

if __name__ == '__main__':
    # 构建graph
    graph = {}
    graph['A'] = set(['B'])
    graph['B'] = set(['A', 'C', 'D'])
    graph['C'] = set(['B'])
    graph['D'] = set(['B', 'F', 'G', 'E'])
    graph['E'] = set(['D', 'I', 'H'])
    graph['F'] = set(['D'])
    graph['G'] = set(['D'])
    graph['H'] = set(['E', 'J'])
    graph['I'] = set(['E'])
    graph['J'] = set(['H'])

    remove_leaf_nodes(graph)
    print(graph)
