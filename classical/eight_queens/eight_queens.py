# coding=utf-8

class Queen8(object):
    """八皇后问题类"""
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

if __name__ == '__main__':
    queen8 = Queen8()
    queen8.recursive(0)
    queen8.print_chess_board()
