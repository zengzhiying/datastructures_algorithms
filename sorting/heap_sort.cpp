#include <iostream>
#include <algorithm>
#include "include/sort_util.h"
#include "include/MaxHeap.h"

using namespace std;

/**
 * 堆排序算法
 * 时间复杂度: nlog(n)
 */
void heapSort(int arr[], int n) {
    MaxHeap maxheap = MaxHeap(n);
    // 将n个元素逐个插入到堆中, 复杂度为:O(nlogn)
    for(int i = 0; i < n; i++)
        maxheap.insert(arr[i]);

    for(int i = n - 1; i >= 0; i--)
        arr[i] = maxheap.extractMax();
}

/**
 * 堆排序算法优化, 在构造函数中直接调整堆结构
 * 将初始化堆的过程复杂度由O(nlogn) -> O(n)
 */
void heapSort2(int arr[], int n) {
    // 调用构造函数的同时会构造堆, 复杂度为O(n)
    MaxHeap maxheap = MaxHeap(arr, n);
    
    for(int i = n - 1; i >= 0; i--)
        arr[i] = maxheap.extractMax();
}

/**
 * shift down元素下降, 用于原地堆排序中构建最大堆
 * 此处最大堆的最大元素下标是0, 不是之前的1
 * 因此判断要做细微的调整, 但规律和之前一样很简单
 */
void shiftDown(int arr[], int n, int k) {
    while(2*k + 1 < n) {
        int j = 2*k + 1;
        if(j + 1 < n && arr[j + 1] > arr[j])
            j += 1;

        if(arr[k] >= arr[j])
            break;

        swap(arr[k], arr[j]);
        k = j;
    }
}

/**
 * 堆排序算法继续优化, 实现原地堆排序
 * 空间复杂度从原有的O(n) -> O(1)
 */
void heapSort3(int arr[], int n) {
    // 注意此处构造最大堆的首个元素下标为0, 不是1
    for(int i = (n - 1)/2; i >= 0; i--)
        shiftDown(arr, n, i);

    for(int i = n - 1; i > 0; i--) {
        swap(arr[0], arr[i]);
        shiftDown(arr, i, 0);
    }
}

int main(int argc, char const *argv[])
{
    // 堆排序测试
    int n = 1000000;
    int *arr = generateRandomArray(n, 0, n);
    int *arr2 = copyIntArray(arr, n);
    int *arr3 = copyIntArray(arr, n);
    testSort("Heap Sort", heapSort, arr, n);
    testSort("Heap Sort2", heapSort2, arr2, n);
    testSort("Heap Sort3", heapSort3, arr3, n);
    delete[] arr;
    arr = NULL;
    delete[] arr2;
    arr2 = NULL;
    delete[] arr3;
    arr3 = NULL;
    return 0;
}
