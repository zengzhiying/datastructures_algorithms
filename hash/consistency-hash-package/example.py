#!/usr/bin/env python3
# coding=utf-8
from consistency_hash import ConsitencyHash

nodes = ['mongodb1', 'mongodb2', 'mongodb3', 'mongodb4', 'mongodb5']

if __name__ == '__main__':
    con = ConsitencyHash(nodes, vnodes=5000)

    node_stat = dict(zip(nodes, [0 for _ in nodes]))

    # 模拟插入数据
    for group in range(1, 10000000):
        node = con.get_node(str(group).encode('utf-8'))
        node_stat[node] += 1

    print(node_stat)

    # 模拟添加1个节点
    new_nodes = nodes.copy()
    new_nodes.append('mongodb6')
    con2 = ConsitencyHash(new_nodes, vnodes=5000)

    # 测试丢失率或迁移量
    lost = 0
    for group in range(1, 10000000):
        object_id = str(group).encode('utf-8')
        node = con.get_node(object_id)
        node2 = con2.get_node(object_id)
        if node != node2:
            # node -> node2
            lost += 1

    print("Lost rate: {:.3f}%, count: {}".format(lost / 100000, lost))

