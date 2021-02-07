# coding=utf-8

class Levenshtein:
    """回溯法计算Levenshtein距离
    """

    def __init__(self):
        self.__min_dist = 2 ** 32 - 1

    def distance(self, s1, s2):
        self.__min_dist = 2 ** 32 - 1
        self.s1 = s1
        self.s2 = s2
        self.n1 = len(s1)
        self.n2 = len(s2)
        self.__distance(0, 0, 0)
        return self.__min_dist

    def __distance(self, i, j, dist):
        if i == self.n1 or j == self.n2:
            # 多余的编辑距离计算
            if i < self.n1:
                dist += (self.n1 - i)
            if j < self.n2:
                dist += (self.n2 - j)

            # 更新最终的距离
            if dist < self.__min_dist:
                self.__min_dist = dist

            return

        if self.s1[i] == self.s2[j]:
            # 匹配
            self.__distance(i + 1, j + 1, dist)
        else:
            # 不匹配
            self.__distance(i + 1, j, dist + 1)  # 删除i或j前面插入字符
            self.__distance(i, j + 1, dist + 1)  # 删除j或i前面插入字符
            self.__distance(i + 1, j + 1, dist + 1)  # 字符替换

