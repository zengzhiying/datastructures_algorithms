#!/usr/bin/env python3
# coding=utf-8
"""代码参考链接: 
https://yikun.github.io/2016/06/09/%E4%B8%80%E8%87%B4%E6%80%A7%E5%93%88%E5%B8%8C%E7%AE%97%E6%B3%95%E7%9A%84%E7%90%86%E8%A7%A3%E4%B8%8E%E5%AE%9E%E8%B7%B5/
"""
import hashlib
import struct
import bisect

def _hash(value: bytes) -> int:
    m = hashlib.md5()
    m.update(value)
    d = m.digest()[4:12]
    return struct.unpack_from('>L', d)[0]

def bignum_mod_hex(num: str, m: int) -> int:
    """对于无法用uint64表示的大整数取模运算
    Args:
        num: 大整数, 使用16进制字符串方式表示
        m: 待取模的对象
    Returns:
        返回取模的运算结果
    """
    ans = 0

    for c in num:
        ans = (ans * 16 + int(c, 16)) % m

    return ans

def bignum_mod_dec(num: str, m: int) -> int:
    """十进制大整数取模运算
    """
    ans = 0

    for c in num:
        ans = (ans * 10 + int(c)) % m

    return ans



def virtual_node():
    """虚节点算法
    """
    # 实际节点个数
    nodes_count = 100
    # 每个节点虚拟出来的节点个数
    v_nodes_count = 300

    # hash环
    ring = []
    # 通过虚节点hash找到实节点
    node_by_hash = {}

    for i in range(nodes_count):
        for j in range(v_nodes_count):
            src = str(i) + str(j)
            h = _hash(src.encode('utf-8'))
            ring.append(h)
            node_by_hash[h] = i

    # 对ring进行排序形成环 (最后的元素和第一个元素相连)
    ring.sort()

    node_stat = [0 for i in range(nodes_count)]

    # 开始模拟向节点分配数据
    for data in range(10000000):
        h = _hash(struct.pack('>I', data))
        # 选择待插入的区间, 如果值正好和hash边界相同, 则往左边的区间插入
        # bisect_left返回计算好的插入位置下标, 并不进行任何插入
        partition = bisect.bisect_left(ring, h)
        if partition == len(ring):
            # 分配到区间0
            node_stat[0] += 1
            continue
        node_stat[node_by_hash[ring[partition]]] += 1

    print(sum(node_stat), node_stat)
    maxinum, mininum = max(node_stat), min(node_stat)
    print(f"max: {maxinum}, min: {mininum}")

    # 那么现在增加一个节点看看有多少缓存丢失(或需要变动的)
    ring2 = []
    node_by_hash2 = {}
    for i in range(nodes_count + 1):
        for j in range(v_nodes_count):
            src = str(i) + str(j)
            h = _hash(src.encode('utf-8'))
            ring2.append(h)
            node_by_hash2[h] = i

    ring2.sort()


    number_lost = 0
    for data in range(10000000):
        h = _hash(struct.pack('>I', data))
        partition = bisect.bisect_left(ring, h)
        partition2 = bisect.bisect_left(ring2, h)
        if partition == len(ring):
            partition = 0
        if partition2 == len(ring2):
            partition2 = 0
        if node_by_hash[ring[partition]] != node_by_hash2[ring2[partition2]]:
            number_lost += 1

    print(f"add one node number of lost: {number_lost} ({number_lost/sum(node_stat)})")

    # 删除节点同理


def partition_node():
    """openstack中的partition方式
    """
    # 节点个数
    number_nodes = 100
    number_log_nodes = 7
    max_power = 32
    part = max_power - number_log_nodes

    nodes_stat = [0] * number_nodes

    ring = []
    node_by_part = {}
    node_by_part2 = {}

    for p in range(2 ** number_log_nodes):
        ring.append(p)
        node_by_part[p] = p % number_nodes
        node_by_part2[p] = p % (number_nodes + 1)

    number_lost = 0

    for data in range(10000000):
        h = _hash(struct.pack('>I', data)) >> part
        p = bisect.bisect_left(ring, h)
        n = p % number_nodes
        n2 = p % (number_nodes + 1)
        nodes_stat[n] += 1
        if n != n2:
            number_lost += 1

    print(sum(nodes_stat), nodes_stat)
    maxinum, mininum = max(nodes_stat), min(nodes_stat)
    print(f"max: {maxinum}, min: {mininum}")

    print(f"add one node number of lost: {number_lost} ({number_lost / sum(nodes_stat)})")



if __name__ == '__main__':
    # virtual_node()
    partition_node()

