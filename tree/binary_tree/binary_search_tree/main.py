#!/usr/bin/env python3
# coding=utf-8
from bst import Node
from bst import BST
from bst import BinarySearchTree

if __name__ == '__main__':
    tree = BST()
    values = [8, 5, 15, 3, 7, 12, 18, 2, 4, 6, 11, 14, 17, 19, 13]
    for v in values:
        tree.insert(v)

    tree.inorder_traversal()
    tree.search(13)
    tree.search(7)

    tree.delete(13)
    tree.inorder_traversal()
    tree.search(11)

    tree.delete(5)
    tree.inorder_traversal()
    tree.search(3)



    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)

    res = tree.traverse()
    print('->'.join([str(d) for d in res]))
    data = tree.search(13)
    assert(data.value == 13)
    data = tree.search(7)
    assert(data.value == 7)

    tree.delete(13)
    res = tree.traverse()
    print('->'.join([str(d) for d in res]))
    data = tree.search(11)
    assert(data.value == 11)

    tree.delete(5)
    res = tree.traverse()
    print('->'.join([str(d) for d in res]))
    data = tree.search(3)
    assert(data.value == 3)



