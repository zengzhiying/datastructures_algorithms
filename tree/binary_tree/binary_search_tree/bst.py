# coding=utf-8
"""二叉查找树
"""

class Node:
    """二叉查找树节点"""
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BST:
    """二叉查找树递归实现"""
    def __init__(self, root=None):
        self.root = root

    def inorder_traversal(self):
        """遍历: 中序遍历"""
        self.res = []
        self._traversal(self.root)
        print('->'.join([str(v) for v in self.res]))

    def _traversal(self, node):
        if node is None:
            return
        self._traversal(node.left)
        self.res.append(node.value)
        self._traversal(node.right)


    def insert(self, value):
        """插入元素"""
        self.root = self._insert(self.root, value)



    def _insert(self, node, value):
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        return node

    def delete(self, value):
        """删除元素"""
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return

        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            # 节点相等删除
            if node.left and node.right:
                # 选择左子树最大的节点替代当前待删除节点, 正好仍然满足二叉查找树规则
                max_node = node.left
                while max_node.right:
                    max_node = max_node.right
                node = self._delete(node, max_node.value)
                node.value = max_node.value
            else:
                if node.left:
                    node = node.left
                else:
                    node = node.right

        return node

    def search(self, value):
        """查找元素"""
        self.count = 0
        self._search(self.root, value)
        print("Find times: {}".format(self.count))

    def _search(self, node, value):
        if node is None:
            return

        if value < node.value:
            self._search(node.left, value)
            self.count += 1
        elif value > node.value:
            self._search(node.right, value)
            self.count += 1
        else:
            print("search value: {} = {}".format(value, node.value))
            self.count += 1


class BinarySearchTree:
    """二叉查找树迭代实现"""
    def __init__(self, root=None):
        self.root = root


    def insert(self, data):
        """插入数据"""
        if self.root is None:
            self.root = Node(data)
            return

        p = self.root

        while p:
            if data > p.value:
                # 右子树
                if p.right is None:
                    p.right = Node(data)
                    return
                p = p.right
            else:
                # 左子树
                if p.left is None:
                    p.left = Node(data)
                    return
                p = p.left


    def search(self, data):
        """查找数据"""
        p = self.root

        while p:
            if data < p.value:
                p = p.left
            elif data > p.value:
                p = p.right
            else:
                # p.value = data
                return p

        return

    def delete(self, data):
        """删除数据"""
        p = self.root
        pp = None
        while p and p.value != data:
            pp = p
            if data > p.value:
                p = p.right
            else:
                p = p.left

        if p is None:
            return

        if p.left and p.right:
            # 查找右树最小节点
            p_min = p.right
            pp_min = p  # 父节点
            while p_min.left:
                pp_min = p_min
                p_min = p_min.left

            p.value = p_min.value
            # 下面赋值方便继续删除叶子节点 而不是在当前重复写代码
            p = p_min
            pp = pp_min

        if p.left:
            child = p.left
        elif p.right:
            child = p.right
        else:
            child = None

        if pp is None:
            # 删除根节点
            self.root = child
        elif pp.left == p:
            pp.left = child
        else:
            pp.right = child

    def traverse(self):
        """中序遍历"""
        res = []
        def t(p):
            if p is None:
                return

            t(p.left)
            res.append(p.value)
            t(p.right)

        p = self.root
        t(p)
        return res
        

