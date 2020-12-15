# coding=utf-8

order_tree = [None] * 20
rs = []

def preorder(tree, i=1):
    """顺序二叉树前序遍历"""
    if tree[i] is None:
        return
    rs.append(tree[i])
    preorder(tree, i << 1)
    preorder(tree, (i << 1) + 1)

def inorder(tree, i=1):
    """顺序二叉树中序遍历"""
    if tree[i] is None:
        return
    inorder(tree, i << 1)
    rs.append(tree[i])
    inorder(tree, (i << 1) + 1)

def postorder(tree, i=1):
    """顺序二叉树后序遍历"""
    if tree[i] is None:
        return
    postorder(tree, i << 1)
    postorder(tree, (i << 1) + 1)
    rs.append(tree[i])


if __name__ == '__main__':
    # 数组存储二叉树
    order_tree[1] = 5
    order_tree[2] = 6
    order_tree[3] = 7
    order_tree[6] = 10
    order_tree[4] = 8
    order_tree[5] = 9


    print("preorder:")
    preorder(order_tree)
    # 5->6->8->9->7->10
    print('->'.join([str(v) for v in rs]))
    rs.clear()

    print("inorder:")
    inorder(order_tree)
    # 8->6->9->5->10->7
    print('->'.join([str(v) for v in rs]))
    rs.clear()


    print("postorder:")
    postorder(order_tree)
    # 8->9->6->10->7->5
    print('->'.join([str(v) for v in rs]))
    rs.clear()

