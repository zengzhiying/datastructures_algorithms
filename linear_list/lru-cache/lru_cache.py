# coding=utf-8

class KVNode:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.next = None

    def __str__(self) -> str:
        return "Node({},{})".format(self.key, self.value)


class LruCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        # header 哨兵
        self.header = KVNode(0, 0)

    def __insert_to_tail(self, key, value):
        """在链表尾部插入元素
        """
        if self.size >= self.cap:
            return

        node = self.header
        while node is not None and node.next is not None:
            node = node.next

        node.next = KVNode(key, value)
        self.size += 1

    def __insert_to_head(self, key, value):
        """插入元素到链表头部
        """
        if self.size >= self.cap:
            return

        node = KVNode(key, value)
        node.next = self.header.next
        self.header.next = node
        self.size += 1

    def get(self, k):
        """按照key获取cache值 O(n)
        """
        node = self.header.next
        prev = self.header
        while node is not None:
            if node.key == k:
                # 移动元素到头部
                prev.next = node.next
                node.next = self.header.next
                self.header.next = node
                # self.__insert_to_head(node)
                return node.value

            prev = node
            node = node.next

    def put(self, k, v):
        """向lru缓存中插入元素 O(n)
        """
        node = self.header
        prev = None
        while node.next is not None:
            prev = node
            node = node.next
            if node.key == k:
                # 将节点移动至头部
                node.value = v
                prev.next = node.next
                node.next = self.header.next
                self.header.next = node
                return

        # 未找到元素 插入到头部
        if self.size == self.cap:
            # 淘汰尾部元素
            prev.next = None
            self.size -= 1

        node = KVNode(k, v)
        node.next = self.header.next
        self.header.next = node
        self.size += 1

    def __delete_tail(self):
        """删除尾节点
        """
        if self.size == 0:
            return
        
        node = self.header
        prev = None
        while node.next is not None:
            prev = node
            node = node.next
        
        # 此时prev为倒数第二个节点(有可能为header)
        prev.next = None
        self.size -= 1

    def traverse(self):
        """遍历lru cache并输出
        """
        if self.size == 0:
            return

        node = self.header.next
        # 两个判断为了输出美观
        while node is not None and node.next is not None:
            print(node, end="->")
            node = node.next

        print(node)

    def clear(self):
        """清空缓存
        """
        self.header.next = None
        self.size = 0

class TwoKVNode:
    """双向链表节点
    """
    def __init__(self, k, v) -> None:
        self.key = k
        self.value = v
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return "Node({}, {})".format(self.key, self.value)

class LruCachePro:
    def __init__(self, capacity: int):
        if capacity < 0:
            capacity = 0
        self.cap = capacity
        self.size = 0
        # header和tail 哨兵
        self.header = TwoKVNode(0, 0)
        self.tail = TwoKVNode(0, 0)
        self.header.next = self.tail
        self.tail.prev = self.header
        # key -> Node
        self.cache = {}

    def get(self, k):
        """按照key获取cache值 O(1)
        """
        if k not in self.cache:
            return

        node = self.cache[k]
        # 移动node到头部
        # 删除
        node.prev.next = node.next
        node.next.prev = node.prev
        # 添加
        node.prev = self.header
        node.next = self.header.next
        self.header.next.prev = node
        self.header.next = node
        return node.value

    def put(self, k, v):
        """向lru缓存中插入元素 O(n)
        """
        if self.cap == 0:
            return

        if k in self.cache:
            node = self.cache[k]
            # 更新值并移动至头部
            node.value = v
            # 删除
            node.prev.next = node.next
            node.next.prev = node.prev
            # 添加
            node.prev = self.header
            node.next = self.header.next
            self.header.next.prev = node
            self.header.next = node
            return

        # 未找到元素 直接插入到头部
        if self.size == self.cap:
            # 淘汰尾部元素
            del self.cache[self.tail.prev.key]
            self.tail.prev.prev.next = self.tail
            self.tail.prev = self.tail.prev.prev
            self.size -= 1

        node = TwoKVNode(k, v)
        node.prev = self.header
        node.next = self.header.next
        self.header.next.prev = node
        self.header.next = node
        self.cache[k] = node
        self.size += 1

    def traverse(self):
        """遍历lru cache并输出
        """
        if self.size == 0:
            return

        node = self.header.next
        while node.next is not None:
            print(node, end="->")
            node = node.next

        print("NULL")
    
