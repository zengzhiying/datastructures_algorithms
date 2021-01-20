# coding=utf-8

class Queen8(object):
    """八皇后问题类的一种解法"""
    def __init__(self):
        # 格子范围和皇后数量, 这里放在一起
        self.__max_num = 8
        # 初始化棋盘
        self.__chess_board = []
        for i in range(self.__max_num):
            self.__chess_board.append([0]*self.__max_num)

    def check(self, x, y):
        """判断皇后落点是否符合规则, 假设坐标系原点位于左上角
        Args:
            x: 落点横坐标, 也就是列数
            y: 落点纵坐标, 也就是行数
        Returns:
            符合规则返回True, 表示可以正常落点
            不符合规则返回False
        """
        for i in range(y):
            # 检查纵向
            if self.__chess_board[x][i] == 1:
                return False

            # 检查左侧斜向
            if x - 1 - i >= 0 and self.__chess_board[x - 1 - i][y - 1 - i] == 1:
                return False

            # 检查右侧斜向
            if x + 1 + i < self.__max_num and self.__chess_board[x + 1 + i][y - 1 - i] == 1:
                return False

        return True

    def recursive(self, y):
        """对皇后进行递归的放置
        Args:
            y: 递归的行数, 也就是纵坐标
        Returns:
            单次递归放置成功找到答案返回True
            未找到解法返回False
        """
        if y == self.__max_num:
            return True

        # 遍历行逐一进行验证
        for i in range(self.__max_num):
            # 清零当前行, 避免回溯出现脏数据
            for x in range(self.__max_num):
                self.__chess_board[x][y] = 0

            if self.check(i, y):
                self.__chess_board[i][y] = 1
                # 递归如果返回true, 说明下层已经找到解法, 无需继续循环
                if self.recursive(y + 1):
                    return True

        return False

    def print_chess_board(self):
        """打印棋盘当前值
        """
        for j in range(self.__max_num):
            for i in range(self.__max_num):
                print(self.__chess_board[i][j], end=' ')
            print('')

class Queen8All(object):
    """八皇后问题所有解法 采用一维数组简化 下标为行值为列
    """
    def __init__(self):
        # 格子范围和皇后数量, 这里放在一起
        self.__max_num = 8
        # 初始化棋盘
        self.__chess_board = [0] * self.__max_num
        # 结果数
        self.__res_num = 0

    def check(self, x, y):
        """判断皇后落点是否符合规则, 假设坐标系原点位于左上角
        Args:
            x: 落点横坐标, 也就是列数-1
            y: 落点纵坐标, 也就是行数-1
        Returns:
            符合规则返回True, 表示可以正常落点
            不符合规则返回False
        """
        for i in range(y):
            # 检查纵向
            if self.__chess_board[i] == x:
                return False

            # 检查左上对角线
            if self.__chess_board[i] == x - y + i:
                return False

            # 检查右上对角线
            if self.__chess_board[i] == x + y - i:
                return False

        return True

    def recursive(self, y):
        """对皇后进行递归的放置
        Args:
            y: 递归的行数, 也就是纵坐标
        Returns:
            递归全部结果无返回值
        """
        if y == self.__max_num:
            self.print_chess_board()
            return

        # 遍历列逐一进行验证
        for i in range(self.__max_num):
            if self.check(i, y):
                self.__chess_board[y] = i
                # 递归如果返回true, 说明下层已经找到解法, 无需继续循环
                self.recursive(y + 1)

    def print_chess_board(self):
        """打印棋盘当前值
        """
        # print(self.__chess_board)
        self.__res_num += 1
        print("res: %d" % self.__res_num)
        for j in range(self.__max_num):
            for i in range(self.__max_num):
                if self.__chess_board[j] == i:
                    print("Q", end=' ')
                else:
                    print("*", end=' ')
            print('')
        print('')

    # def test(self):
    #     self.__chess_board = [7, 5, 3, 6, 4, 4, 2, 4]
    #     print(self.check(4, 5))

if __name__ == '__main__':
    queen8 = Queen8()
    queen8.recursive(0)
    queen8.print_chess_board()

    print()

    queen8 = Queen8All()
    queen8.recursive(0)
    # queen8.test()
