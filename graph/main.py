#!/usr/bin/env python3
# coding=utf-8
from graph import Graph

if __name__ == '__main__':
    g = Graph()

    for i in range(30):
        g.add_vertex(str(i))

    g.add_edge('0', '1')
    g.add_edge('0', '3')
    g.add_edge('1', '2')
    g.add_edge('1', '4')
    g.add_edge('3', '4')
    g.add_edge('4', '5')
    g.add_edge('4', '6')
    g.add_edge('2', '5')
    g.add_edge('5', '7')
    g.add_edge('6', '7')

    g.add_edge('7', '8')
    g.add_edge('8', '9')
    g.add_edge('8', '10')
    g.add_edge('8', '11')
    g.add_edge('11', '12')
    g.add_edge('12', '13')
    g.add_edge('8', '14')
    g.add_edge('14', '15')
    g.add_edge('15', '16')
    g.add_edge('16', '17')
    g.add_edge('17', '18')
    g.add_edge('18', '12')
    g.add_edge('12', '19')

    g.add_edge('6', '19')
    g.add_edge('19', '20')
    g.add_edge('20', '21')
    g.add_edge('21', '22')
    g.add_edge('22', '23')
    g.add_edge('22', '24')
    g.add_edge('22', '25')
    g.add_edge('22', '26')
    g.add_edge('26', '27')
    g.add_edge('22', '28')
    g.add_edge('28', '29')
    # g.add_edge('29', '23')

    g.bfs('0', '7')
    # g.bfs('0', '23')

    # g.dfs('0', '7')
    g.dfs('0', '23')

