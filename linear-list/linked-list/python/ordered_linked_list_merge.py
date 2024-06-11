#!/usr/bin/env python3
# coding=utf-8
"""两个有序链表合并"""

class Node:
    """单向链表节点"""
    def __init__(self, v):
        self.value = v
        self.next = None

def linked_list_traverse(head: Node) -> None:
    l = []
    while head:
        l.append(str(head.value))
        head = head.next
    l.append("NULL")
    print("->".join(l))

def tow_linked_list_merge(l1: Node, l2: Node) -> Node:
    """合并链表, 返回合并后链表的头结点
    """
    # 哨兵
    p_node = Node(-1)
    prev = p_node
    while l1 and l2:
        if l1.value <= l2.value:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next

    if l1:
        prev.next = l1
    else:
        prev.next = l2

    return p_node.next

def merge_recursive(l1: Node, l2: Node) -> Node:
    """递归方式合并"""
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.value <= l2.value:
        l1.next = merge_recursive(l1.next, l2)
        return l1
    l2.next = merge_recursive(l1, l2.next)
    return l2

if __name__ == '__main__':
    l1 = Node(1)
    l1.next = Node(4)
    l1.next.next = Node(5)

    l2 = Node(1)
    l2.next = Node(2)
    l2.next.next = Node(3)
    l2.next.next.next = Node(6)

    print("迭代方式合并: ")
    
    linked_list_traverse(l1)
    linked_list_traverse(l2)

    l = tow_linked_list_merge(l1, l2)
    linked_list_traverse(l)


    l1 = Node(1)
    l1.next = Node(4)
    l1.next.next = Node(5)

    l2 = Node(1)
    l2.next = Node(2)
    l2.next.next = Node(3)
    l2.next.next.next = Node(6)

    print("递归方式合并: ")

    linked_list_traverse(l1)
    linked_list_traverse(l2)

    l = merge_recursive(l1, l2)
    linked_list_traverse(l)

