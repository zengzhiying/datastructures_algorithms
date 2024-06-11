# coding=utf-8

"""链表实现类封装以及各类操作算法实现
常见的操作算法比如:
1. 插入和删除操作
2. 检测链表是否有环
3. 计算链表的中间节点
4. 删除链表倒数第 n 个节点
5. 链表反转：包括迭代和递归方式
6. 基于链表的回文检测
"""

class Node:
    """链表节点
    """
    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        """计算链表长度
        外部通过 len() 调用
        """
        return self.size
    
    def is_empty(self):
        """判断链表是否为空
        """
        return self.size == 0
    
    def append(self, v):
        """在链表尾部插入节点
        """
        if self.head is None:
            self.head = Node(v)
            self.size += 1
            return
        
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        
        cur.next = Node(v)
        self.size += 1

    def insert(self, pos, v):
        """在链表指定下标位置插入节点
        """
        if pos < 0 or pos > self.size:
            return
        
        if pos == 0:
            node = Node(v)
            node.next = self.head
            self.head = node
            self.size += 1
            return
        
        prev = None
        cur = self.head
        for _ in range(pos):
            prev = cur
            cur = cur.next
        node = Node(v)
        node.next = cur
        prev.next = node
        self.size += 1
    
    def remove_index(self, i):
        """根据下标删除节点
        """
        if i < 0 or i >= self.size:
            return
        
        if i == 0:
            self.head = self.head.next
            self.size -= 1
            return
        
        prev = None
        cur = self.head
        for _ in range(i):
            prev = cur
            cur = cur.next
        prev.next = cur.next
        self.size -= 1

    def remove_value(self, v):
        """根据第一个匹配的值删除节点
        """
        if self.head is None:
            return
        if self.head.value == v:
            self.head = self.head.next
            self.size -= 1
            return
        prev = self.head
        cur = self.head.next
        while cur is not None:
            if cur.value == v:
                prev.next = cur.next
                self.size -= 1
                break
            prev = cur
            cur = cur.next

    def remove_nth_from_last(self, n):
        """删除链表中倒数第 n 个元素，n 必须为大于 0 的正整数
        通过双指针法固定间距 n 从而实现删除
        """
        if n <= 0 or self.size < n:
            return
        
        if self.size == n:
            self.head = self.head.next
            self.size -= 1
            return
        
        slow, fast = self.head, self.head

        for _ in range(n):
            fast = fast.next
        
        # 快指针多走一步，这样慢指针可以指向待删除元素的上一个元素，从而方便删除
        fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

    def clear(self):
        """清空链表"""
        self.head = None
        self.size = 0

    def traverse(self):
        """链表遍历输出，方便结构化显示
        """
        res = []
        cur = self.head
        while cur is not None:
            res.append(str(cur.value))
            cur = cur.next
        res.append('NULL')
        return '->'.join(res)
    
    def is_ring(self) -> bool:
        """检测链表是否有环
        通过快慢指针检测
        """
        slow, fast = self.head, self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
    
    def get_middle_node(self) -> Node:
        """获取链表的中间节点，如果链表值个数为偶数, 则返回中间的第二个元素
        通过快慢指针法实现
        """
        slow, fast = self.head, self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
    
    def get_middle_node2(self) -> Node:
        """获取链表的中间节点，奇偶变动法实现
        """
        middle, cur = self.head, self.head

        i = 0
        while cur:
            if i & 1:
                middle = middle.next
            cur = cur.next
            i += 1

        return middle
    
    def reverse(self):
        """反转链表，默认为迭代方式
        此操作会直接在当前链表原地生效
        """
        if self.is_empty():
            return

        prev = None
        cur = self.head
        while cur is not None:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        self.head = prev

    def reverse_recursive(self, cur):
        """递归方式反转链表
        重点是把当前节点后面的节点当做一个整体代入递归条件
        """
        if self.head is None or self.head.next is None:
            return
        self.head = self.__reverse_recursive(self.head.next)
    
    def __reverse_recursive(self, cur):
        if cur is None or cur.next is None:
            return cur
        node = self.__reverse_recursive(cur.next)
        cur.next.next = cur
        cur.next = None
        return node
    
    def is_palindrome(self):
        if self.size <= 1:
            return True
        
        prev = None
        fast = self.head
        slow = self.head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            node = slow.next
            slow.next = prev
            prev = slow
            slow = node

        # 反转之后当前链表作废
        self.head = None
        self.size = 0
        # 长度为奇数的情况
        if fast is not None:
            slow = slow.next

        while slow is not None:
            if slow.value != prev.value:
                return False
            prev = prev.next
            slow = slow.next

        return True
        
