#include <iostream>
#include <algorithm>

using namespace std;

/**
 * 基于数组实现最大堆
 * 经典堆实现, 索引下标从1开始, 元素为0的元素不使用
 */

class MaxHeap
{
private:
    int *data;
    int count;
    int capacity;  // 元素最大数量限制
    // shift up操作, 保持最大堆结构不变
    void shiftUp(int k);
    // shift down操作, 小元素向下移动, 位置最大堆结构不变
    void shiftDown(int k);
public:
    MaxHeap(int capacity);
    // 构造函数2 heapify 构造最大堆
    MaxHeap(int arr[], int n);
    ~MaxHeap();
    int size();
    bool isEmpty();
    // 添加新的元素
    void insert(int item);
    // 推出最大值元素
    int extractMax();
};