#include <assert.h>
#include "IndexMaxHeap.h"

IndexMaxHeap::IndexMaxHeap(int capacity) {
    data = new int[capacity + 1];
    indexes = new int[capacity + 1];
    reverse = new int[capacity + 1];
    // 初始化reverse全为0
    for(int i = 0; i <= capacity; i++)
        reverse[i] = 0;
    count = 0;
    this->capacity = capacity;
}

IndexMaxHeap::~IndexMaxHeap() {
    delete[] data;
    delete[] indexes;
    delete[] reverse;
    data = NULL;
    indexes = NULL;
    reverse = NULL;
}

int IndexMaxHeap::size() {
    return count;
}

bool IndexMaxHeap::isEmpty() {
    return count == 0;
}

// 传入的i对于用户来说, 是从0索引的
void IndexMaxHeap::insert(int i, int item) {
    assert(count + 1 <= capacity);
    assert(i + 1 >= 1 && i + 1 <= capacity);
    i += 1;
    data[i] = item;
    indexes[count + 1] = i;
    reverse[i] = count + 1;
    count++;
    // 新加入的元素有可能破坏堆, 做shift up上升, 仍然保持最大堆
    shiftUp(count);
}

void IndexMaxHeap::shiftUp(int k) {
    while(k > 1 && data[indexes[k/2]] < data[indexes[k]]) {
        swap(indexes[k/2], indexes[k]);
        reverse[indexes[k/2]] = k/2;
        reverse[indexes[k]] = k;
        k /= 2;
    }
}

int IndexMaxHeap::extractMax() {
    assert(count > 0);
    int ret = data[indexes[1]];
    swap(indexes[1], indexes[count]);
    reverse[indexes[1]] = 1;
    reverse[indexes[count]] = 0;  // 元素将被删除, 直接置0即可
    count--;
    shiftDown(1);
    return ret;
}

/**
 * 获取最大元素索引值, 然后根据索引可以很方便的获取元素
 */
int IndexMaxHeap::extractMaxIndex() {
    assert(count > 0);
    int ret = indexes[1] - 1;  // 外部来看是从0开始的, 因此减1
    swap(indexes[1], indexes[count]);
    reverse[indexes[1]] = 1;
    reverse[indexes[count]] = 0;
    count--;
    shiftDown(1);
    return ret;
}

/**
 * 根据索引值获取数据
 */
int IndexMaxHeap::getIndexData(int i) {
    assert(contain(i));
    return data[i + 1];
}

/**
 * 基于索引堆修改元素的值
 */
void IndexMaxHeap::change(int i, int newItem) {
    assert(contain(i));  // 判断索引堆是否包含给定索引为i的元素
    i += 1;
    data[i] = newItem;
    // 找到使得indexes[j] = i的j值, j即data[i]元素在索引堆中的位置
    // 循环时间复杂度为O(n), 大于插入和删除
    // for(int j = 1; j <= count; j++)
    //     if(indexes[j] == i) {
    //         // 找到j之后对j进行shiftUp和shiftDown
    //         shiftUp(j);
    //         shiftDown(j);
    //         return;
    //     }
    // 用reverse通过i反向查找j进行修改, 时间复杂度变为O(lgn)
    int j = reverse[i];
    shiftUp(j);
    shiftDown(j);
}

void IndexMaxHeap::shiftDown(int k) {
    while(2*k <= count) {
        int j = 2*k; // data[k]和data[j]交换位置
        if(j + 1 <= count && data[indexes[j + 1]] > data[indexes[j]])
            j += 1;
        if(data[indexes[k]] >= data[indexes[j]])
            break;
        swap(indexes[k], indexes[j]);
        reverse[indexes[k]] = k;
        reverse[indexes[j]] = j;
        k = j;
    }
}

/**
 * 判断索引堆中i的元素是否存在
 */
bool IndexMaxHeap::contain(int i) {
    assert(i + 1 >= 1 && i + 1 <= capacity);
    return reverse[i + 1] != 0;
}
