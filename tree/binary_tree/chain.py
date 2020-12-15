# coding=utf-8

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
    

