# coding=utf-8

class Node:
    def __init__(self, v):
        self.value = v
        self.next = None

    def __str__(self) -> str:
        return "Node({})".format(self.value)


class LinkedList:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        # header 哨兵
        self.header = Node(0)

    def insert_to_tail(self, value):
        """在链表尾部插入元素
        """
        if self.size >= self.cap:
            return

        node = self.header
        while node.next is not None:
            node = node.next

        node.next = Node(value)
        self.size += 1

    def insert_to_head(self, value):
        """插入元素到链表头部
        """
        if self.size >= self.cap:
            return

        node = Node(value)
        node.next = self.header.next
        self.header.next = node
        self.size += 1
    
    def find_by_value(self, value):
        """按照值在链表中查找
        Args:
            value: 要查找的值
        Returns:
            返回元素所在的第一个下标(下标仍然从0开始)
            如果没有找到则返回-1
        """

        node = self.header.next
        cur = 0
        while node is not None:
            if node.value == value:
                return cur

            node = node.next

            cur += 1

        return -1

    def find_by_index(self, i):
        """按照下标在链表中查找元素
        Args:
            i: 下标, 从0开始
        Returns:
            返回查找到的node，i越界则返回None
        """
        if i >= self.size:
            return None

        node = self.header
        for _ in range(i + 1):
            node = node.next

        return node

    def delete_tail(self):
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
        """遍历链表并输出
        """
        if self.size == 0:
            return

        node = self.header.next
        # 两个判断为了输出美观
        while node is not None and node.next is not None:
            print(node.value, end="->")
            node = node.next

        print(node.value)

    def clear(self):
        """清空链表
        """
        self.header.next = None
        self.size = 0
    
