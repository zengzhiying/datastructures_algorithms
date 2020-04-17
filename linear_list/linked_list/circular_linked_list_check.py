#!/usr/bin/env python3
# coding=utf-8
"""链表是否有环检测"""
class Node:
    """单向链表节点"""
    def __init__(self, v):
        self.value = v
        self.next = None

def exist_ring(head: Node) -> bool:
    """检测链表是否有环
    快慢指针检测
    """
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

if __name__ == '__main__':
    # 构建链表
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print(exist_ring(head))

    head.next.next.next.next.next = head.next
    print(exist_ring(head))

