#!/usr/bin/env python3
# coding=utf-8
from linked_list import LinkedList

if __name__ == '__main__':
    # 链表基本操作验证
    print("================ 链表基本操作验证 =============")
    ll = LinkedList()
    ll.append(3)
    ll.append(4)
    ll.append(5)
    print(ll.traverse(), len(ll))
    ll.remove_value(3)
    print(ll.traverse(), len(ll))

    ll1 = LinkedList()
    ll1.insert(0, 2)
    ll1.insert(0, 1)
    ll1.insert(1, 6)
    ll1.insert(3, 8)
    print(ll1.traverse(), len(ll1))
    ll1.remove_index(0)
    ll1.append(7)
    ll1.remove_index(3)
    print(ll1.traverse(), len(ll1))
    ll1.remove_index(1)
    print(ll1.traverse(), len(ll1))

    # 检测是否有环
    print("==================== 检测是否有环 ==================")
    ll1.clear()
    for v in range(1, 6):
        ll1.append(v)
    print(ll1.traverse(), ll1.is_ring())
    # 手动设置环
    ll1.head.next.next.next.next.next = ll1.head.next
    # 此时不能使用遍历方法，否则数组无限增大会导致内存溢出
    print(ll1.is_ring())

    # 获取中间节点
    print("==================== 获取中间节点 ==================")
    ll = LinkedList()
    # 奇数长度链表
    for v in range(1, 6):
        ll.append(v)
    assert ll.get_middle_node().value == 3
    assert ll.get_middle_node2().value == 3
    # 偶数长度链表
    ll.remove_value(5)
    assert ll.get_middle_node().value == 3
    assert ll.get_middle_node2().value == 3

    # 删除倒数第 n 个节点
    print("==================== 删除倒数第 n 个节点 ==================")
    ll = LinkedList()
    for v in range(1, 6):
        ll.append(v)

    ll.remove_nth_from_last(5)
    print(ll.traverse())
    ll.remove_nth_from_last(2)
    print(ll.traverse())

    # 链表反转
    print("==================== 链表反转 ==================")
    ll = LinkedList()
    ll.reverse()
    print(ll.traverse())
    ll.append(1)
    ll.reverse()
    print(ll.traverse())
    for v in range(2, 6):
        ll.append(v)
    ll.reverse()
    print(ll.traverse())
    # 递归方式
    ll = LinkedList()
    ll.reverse()
    print(ll.traverse())
    ll.append(1)
    ll.reverse()
    print(ll.traverse())
    for v in range(2, 6):
        ll.append(v)
    ll.reverse()
    print(ll.traverse())

    # 回文检测
    print("==================== 回文检测 ==================")
    ll2 = LinkedList()
    ll2.append("我")
    print(ll2.traverse(), ll2.is_palindrome())
    ll2.append("是")
    print(ll2.traverse(), ll2.is_palindrome())
    s = "我是我"
    for w in s:
        ll2.append(w)
    print(ll2.traverse(), ll2.is_palindrome())
    s = "是不是你试试是不是"
    for w in s:
        ll2.append(w)
    print(ll2.traverse(), ll2.is_palindrome())
    s = "天连水尾水连天"
    for w in s:
        ll2.append(w)
    print(ll2.traverse(), ll2.is_palindrome())
