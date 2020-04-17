#!/usr/bin/env python3
# coding=utf-8
"""删除链表中的节点"""
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

def remove_node_by_index(head: Node, index: int) -> Node:
    """按照下标删除节点
    """
    if index == 0:
        return head.next
    cur = head
    prev = cur
    for i in range(index):
        prev = cur
        cur = cur.next
        if cur is None:
            return head
    prev.next = cur.next
    return head

def remove_node_by_value(head: Node, value: int) -> Node:
    """按照值删除节点"""
    if head.value == value:
        return head.next
    cur = head
    prev = None
    while cur:
        if cur.value == value:
            prev.next = cur.next
            # cur.next = None
            break
        prev = cur
        cur = cur.next
    return head

def remove_nth_from_last(head: Node, n: int) -> Node:
    """删除链表中倒数第n个元素
    双指针法, 固定间距为n
    """
    # 哨兵, 简化问题
    sentry = Node(0)
    sentry.next = head
    fast, slow = sentry, sentry

    # 先走n步
    for i in range(n):
        fast = fast.next
        if fast is None:
            # 不存在倒数第n个节点
            return head

    fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return sentry.next


if __name__ == '__main__':
    # 构建链表
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    linked_list_traverse(head)
    p = remove_node_by_index(head, 0)
    linked_list_traverse(p)

    remove_node_by_value(p, 5)
    linked_list_traverse(p)

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    # p = remove_nth_from_last(head, 5)
    p = remove_nth_from_last(head, 2)
    linked_list_traverse(p)
