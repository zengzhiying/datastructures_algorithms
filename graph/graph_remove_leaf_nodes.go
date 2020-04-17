package main

import (
    "fmt"
)

// 删除图的叶子结点Golang版本
// 基于邻接表实现图, 并且移除图中的叶子结点
// ignoreNodes: 可以自定义忽略删除某些结点
func graphRemoveLeafNodes(graph map[string]map[string]int, ignoreNodes map[string]int) {
    leafNodes := make([]string, 0)
    for n, nodes := range graph {
        _, ok := ignoreNodes[n]
        if (nodes == nil || len(nodes) <= 1) && !ok {
            leafNodes = append(leafNodes, n)
        }
    }

    for _, node := range leafNodes {
        delete(graph, node)
        for n, nodes := range graph {
            if _, ok := nodes[node]; ok {
                delete(graph[n], node)
            }
        }
    }
}


// 移除叶子结点时间复杂度优化版本, 先移除第一层邻接表, 再循环移除第二层
func graphRemoveLeafNodes2(graph map[string]map[string]int, ignoreNodes map[string]int) {

    leafNodes := make([]string, 0)

    for n, nodes := range graph {

        _, ok := ignoreNodes[n]

        if (nodes == nil || len(nodes) <= 1) && !ok {
            leafNodes = append(leafNodes, n)
        }
    }

    for _, node := range leafNodes {
        delete(graph, node)
    }


    for _, node := range leafNodes {
        for n, nodes := range graph {
            if _, ok := nodes[node]; ok {
                delete(graph[n], node)
            }
        }
    }
}

func main() {
    graph := make(map[string]map[string]int)
    graph["A"] = map[string]int{
        "B": 1,
    }
    graph["B"] = map[string]int{
        "A": 1,
        "C": 1,
        "D": 1,
    }
    graph["C"] = map[string]int{
        "B": 1,
    }
    graph["D"] = map[string]int{
        "B":1,"F":1,"G":1,"E":1,
    }
    graph["E"] = map[string]int{
        "D":1,"I":1,"H":1,
    }
    graph["F"] = map[string]int{"D":1}
    graph["G"] = map[string]int{"D":1}
    graph["H"] = map[string]int{"E":1,"J":1}
    graph["I"] = map[string]int{"E":1}
    graph["J"] = map[string]int{"H":1}
    fmt.Println(graph)
    // graphRemoveLeafNodes(graph, map[string]int{"KK":1})
    graphRemoveLeafNodes2(graph, map[string]int{"KK":1})
    // graphRemoveLeafNodes(graph, map[string]int{"J":1})
    fmt.Println(graph)
}
