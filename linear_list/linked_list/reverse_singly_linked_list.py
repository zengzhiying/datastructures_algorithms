#!/usr/bin/env python3
# coding=utf-8

class Node:
    """定义单向链表节点"""
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

def reverse_linked_list(head: Node) -> Node:
    """反转链表 - 迭代方式
    原地修改链表并返回头结点
    """
    prev = None
    while head is not None:
        tmp = head.next
        head.next = prev
        prev = head
        head = tmp
    return prev

def reverse_linked_list_recursive(head: Node) -> Node:
    """递归方式反转链表
    重点是把当前节点后面的节点当做一个整体代入递归条件
    """
    if head is None or head.next is None:
        return head
    linked_k = reverse_linked_list_recursive(head.next)
    # 将linked_k的尾结点和head反转
    head.next.next = head
    head.next = None
    return linked_k


if __name__ == '__main__':
    # 构建链表
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    linked_list_traverse(head)
    p = reverse_linked_list(head)
    assert head.next is None
    linked_list_traverse(p)
    p = reverse_linked_list_recursive(p)
    linked_list_traverse(head)
    # 等价
    linked_list_traverse(p)

