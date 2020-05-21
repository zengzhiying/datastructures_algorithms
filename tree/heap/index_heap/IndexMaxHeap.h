#include <iostream>
#include <algorithm>

using namespace std;

/**
 * 基于数组实现索引最大堆
 * 只对于数组索引构建堆结构, 堆操作时只交换索引数字, 减少性能消耗
 */

class IndexMaxHeap
{
private:
    int *data;
    int *indexes;
    int *reverse;
    int count;
    int capacity;  // 元素最大数量限制
    // shift up操作, 保持最大堆结构不变
    void shiftUp(int k);
    // shift down操作, 小元素向下移动, 位置最大堆结构不变
    void shiftDown(int k);
public:
    IndexMaxHeap(int capacity);
    // 构造函数2 heapify 构造最大堆
    // MaxHeap(int arr[], int n);
    ~IndexMaxHeap();
    int size();
    bool isEmpty();
    // 添加新的元素
    void insert(int i, int item);
    // 推出最大值元素
    int extractMax();
    // 推出最大值元素对应的索引
    int extractMaxIndex();
    // 根据索引值获取数据
    int getIndexData(int i);
    // 给定索引堆中的位置修改索引值对应的元素
    void change(int i, int newItem);
    // 判断索引堆中给定i的原数组索引元素是否存在
    bool contain(int i);
};