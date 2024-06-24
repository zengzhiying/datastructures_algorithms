#include <assert.h>
#include "MaxHeap.h"

MaxHeap::MaxHeap(int capacity) {
    data = new int[capacity + 1];
    count = 0;
    this->capacity = capacity;
}

MaxHeap::MaxHeap(int arr[], int n) {
    data = new int[n + 1];
    capacity = n;
    for(int i = 0; i < n; i++)
        data[i + 1] = arr[i];
    count = n;

    // 调整结构使之形成最大堆结构
    // 从第一个不是叶子节点的节点开始
    for(int i = count/2; i >= 1; i--)
        shiftDown(i);
}

MaxHeap::~MaxHeap() {
    delete[] data;
    data = NULL;
}

int MaxHeap::size() {
    return count;
}

bool MaxHeap::isEmpty() {
    return count == 0;
}

void MaxHeap::insert(int item) {
    assert(count + 1 <= capacity);
    data[count + 1] = item;
    count++;
    // 新加入的元素有可能破坏堆, 做shift up上升, 仍然保持最大堆
    shiftUp(count);
}

void MaxHeap::shiftUp(int k) {
    while(k > 1 && data[k/2] < data[k]) {
        swap(data[k/2], data[k]);
        k /= 2;
    }
}

int MaxHeap::extractMax() {
    assert(count > 0);
    int ret = data[1];
    swap(data[1], data[count]);
    count--;
    shiftDown(1);
    return ret;
}

void MaxHeap::shiftDown(int k) {
    while(2*k <= count) {
        int j = 2*k; // data[k]和data[j]交换位置
        if(j + 1 <= count && data[j + 1] > data[j])
            j += 1;
        if(data[k] >= data[j])
            break;
        swap(data[k], data[j]);
        k = j;
    }
}
