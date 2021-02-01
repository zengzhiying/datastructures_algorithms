#!/usr/bin/env python3
# coding=utf-8
from triangular_shortest_path import shortest_path

if __name__ == '__main__':
    triangle = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14, 15]]
    # 25
    print(shortest_path(triangle))

    triangle = [[5], [7, 8], [2, 3, 4], [4, 9, 6, 1], [9, 7, 2, 4, 5]]
    # 22
    print(shortest_path(triangle))

    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    # 11
    print(shortest_path(triangle))
