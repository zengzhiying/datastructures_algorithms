#!/usr/bin/env python3
# coding=utf-8
"""获取链表的中间节点"""

class Node:
    """单向链表节点"""
    def __init__(self, v):
        self.value = v
        self.next = None

def get_middle_node(head: Node) -> Node:
    """如果链表值个数为偶数, 则返回中间的第二个元素
    快慢指针法: 每次分别走1步和2步
    """
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def get_middle_node2(head: Node) -> Node:
    """奇偶变动的方法, 类似于快慢指针"""
    middle, cur = head, head

    i = 0
    while cur:
        if i & 1:
            middle = middle.next
        cur = cur.next
        i += 1

    return middle

if __name__ == '__main__':
    # 构建奇数链表
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    assert get_middle_node(head).value == 3
    assert get_middle_node2(head).value == 3

    # 构建偶数链表
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)

    assert get_middle_node(head).value == 3
    assert get_middle_node2(head).value == 3
