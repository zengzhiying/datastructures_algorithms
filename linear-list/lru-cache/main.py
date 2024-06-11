#!/usr/bin/env python3
# coding=utf-8
import time

from linked_list import LinkedList
from lru_cache import LruCache
from lru_cache import LruCachePro

if __name__ == '__main__':
    linked = LinkedList(6)
    linked.insert_to_head(3)
    linked.insert_to_tail(7)
    linked.insert_to_tail(2)
    linked.insert_to_tail(9)
    linked.insert_to_tail(2)
    linked.insert_to_tail(8)
    linked.insert_to_tail(1)

    linked.traverse()

    print(linked.find_by_value(9))
    print(linked.find_by_index(5))
    linked.delete_tail()
    linked.traverse()
    linked.insert_to_head(6)
    linked.traverse()

    for _ in range(10):
        linked.delete_tail()

    linked.traverse()

    # l = [1,2,3,4,5,6]
    # linked.clear()

    # for _ in range(1000000):
    #     for n in l:
    #         linked.insert_to_tail(n)

    # linked.traverse()

    lru = LruCachePro(10)
    for i in range(10):
        lru.put(str(i), i)

    lru.traverse()
    lru.get("6")
    lru.put("100", "100")
    lru.put("8", "9")
    lru.get("1000")
    print(lru.get("8"))
    # print(lru.get("100"))
    lru.traverse()
    

    t1 = time.time()
    lru = LruCache(10000)
    for i in range(10001):
        lru.put(str(i), i)

    for i in range(100):
        lru.get(10000 - i)
    t2 = time.time()
    print("time1: {:.3f}s".format(t2 - t1))

    t1 = time.time()
    lru = LruCachePro(10000)
    for i in range(10001):
        lru.put(str(i), i)

    for i in range(100):
        lru.get(10000 - i)
    t2 = time.time()
    print("time1: {:.3f}s".format(t2 - t1))

    
