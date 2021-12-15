# coding=utf-8
from collections import deque

class ChainNode:
    """链式存储二叉树节点"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder_chain(node):
    """链式存储二叉树前序遍历
    """
    if node is None:
        return
    # print(node.value)
    rs.append(node.value)
    preorder_chain(node.left)
    preorder_chain(node.right)

def inorder_chain(node):
    """链式存储二叉树中序遍历
    """
    if node is None:
        return
    inorder_chain(node.left)
    # print(node.value)
    rs.append(node.value)
    inorder_chain(node.right)

def postorder_chain(node):
    """链式存储二叉树后序遍历
    """
    if node is None:
        return
    postorder_chain(node.left)
    postorder_chain(node.right)
    # print(node.value)
    rs.append(node.value)

def get_node_height(node):
    """获取节点的高度 深度优先
    """
    if node is None:
        return -1

    return max(get_node_height(node.left), get_node_height(node.right)) + 1

def get_node_height_level(node):
    """获取节点的高度 广度优先-层序遍历
    """
    if node is None:
        return -1

    q = deque()
    q.append(node)
    height = -1
    front, rear = 0, len(q)
    while q:
        node = q.popleft()
        front += 1
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

        if front == rear:
            front, rear = 0, len(q)
            height += 1

    return height


rs = []


if __name__ == '__main__':
    chain_head = ChainNode(5)
    chain_head.left = ChainNode(6)
    chain_head.right = ChainNode(7)
    chain_head.left.left = ChainNode(8)
    chain_head.left.right = ChainNode(9)
    chain_head.right.left = ChainNode(10)

    print("preorder:")
    # 5->6->8->9->7->10
    preorder_chain(chain_head)
    print('->'.join([str(v) for v in rs]))
    rs.clear()

    print("inorder:")
    # 8->6->9->5->10->7
    inorder_chain(chain_head)
    print('->'.join([str(v) for v in rs]))
    rs.clear()

    print("postorder:")
    # 8->9->6->10->7->5
    postorder_chain(chain_head)
    print('->'.join([str(v) for v in rs]))
    rs.clear()

    print("Binary tree1 height: {}".format(get_node_height(chain_head)))
    print("Binary tree1 height: {}".format(get_node_height_level(chain_head)))

    root = ChainNode(3)
    root.left = ChainNode(6)
    root.right = ChainNode(9)
    root.left.left = ChainNode(7)
    root.right.left = ChainNode(11)
    root.left.left.left = ChainNode(2)
    root.left.left.left.left = ChainNode(1)
    root.left.left.left.left.left = ChainNode(0)

    print("Binary tree2 height: {}".format(get_node_height(root)))
    print("Binary tree2 height: {}".format(get_node_height_level(root)))
    

