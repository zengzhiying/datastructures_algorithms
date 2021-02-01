#!/usr/bin/env python3
# coding=utf-8

class TrieTree:
    """Trie前缀树
    """
    def __init__(self):
        self.root = {'/':{}}

    def insert(self, text: str):
        """插入text字符串
        """
        p = self.root['/']
        for c in text:
            if c not in p:
                p[c] = {}
            p = p[c]

    def find(self, pattern: str):
        """查找字符串
        """
        p = self.root['/']
        for c in pattern:
            if c not in p:
                return False
            p = p[c]

        if p:
            # 只是前缀匹配
            return False
        return True

    def dfs(self):
        # 深度
        # self._depth = 1
        # 因为trie tree是无环的因此 迭代所有路径时不需要缓存节点
        # self._visited = set()
        self._stack = []
        p = self.root

        self._dfs(p, '/')


    def _dfs(self, p, v):
        # key = '%d-%s' % (self._depth, v)
        # self._visited.add(key)
        self._stack.append(v)
        # self._depth += 1
        if not p[v]:
            print(''.join(self._stack)[1:])
            self._stack.pop()
            # self._depth -= 1
            return

        for c in p[v]:
            # key = '%d-%s' % (self._depth, c)
            # if key not in self._visited:
            self._dfs(p[v], c)

        self._stack.pop()
        # self._depth -= 1





if __name__ == '__main__':
    trie = TrieTree()
    trie.insert("hello java")
    trie.insert("hello python")
    trie.insert("caffe")
    trie.insert("hadoop")
    trie.insert("hello go")
    trie.insert("tensorflow")
    trie.insert("我爱数据结构")
    trie.insert("我爱算法")

    print(trie.root['/'])
    print(trie.find("hello"))
    print(trie.find("coco"))
    print(trie.find("hadoop"))
    print(trie.find("tensorflow"))
    print(trie.find("我爱数据结构")) 


    trie.dfs()

