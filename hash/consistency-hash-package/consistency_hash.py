# coding=utf-8
import hashlib
import struct
import bisect

class ConsitencyHash:
    def __init__(self, nodes, vnodes=5000):
        """初始化一致性哈希
        Args:
            nodes: 传入实际节点列表, 可以为代号, 比如: [1, 2, 3]
            vnodes: 每个节点对应虚拟节点个数, 默认: 5000 集群规模越大, vnodes可以越小
        """
        self.nodes = nodes

        self.nodes_count = len(self.nodes)
        self.vnodes_count = vnodes

        # hash环
        self.ring = []

        # 虚节点hash -> 实际节点映射
        self.node_by_hash = {}

        for i in range(self.nodes_count):
            for j in range(self.vnodes_count):
                src = struct.pack('>2I', i, j)
                h = self.__hash(src)
                self.ring.append(h)
                self.node_by_hash[h] = self.nodes[i]

        # 排序
        self.ring.sort()


    def __hash(self, src: bytes) -> int:
        """hash函数"""
        m = hashlib.md5()
        m.update(src)
        d = m.digest()[4:12]
        return struct.unpack_from('>L', d, 0)[0]

    def get_node(self, data: bytes):
        """给定数据返回node节点
        """
        h = self.__hash(data)

        # 计算插入区间 左开右闭 边界值插入到左边区间
        partition = bisect.bisect_left(self.ring, h)
        if partition == len(self.ring):
            return self.nodes[0]
        return self.node_by_hash[self.ring[partition]]
