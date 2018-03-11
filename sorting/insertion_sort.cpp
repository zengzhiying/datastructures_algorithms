#include <iostream>
#include <algorithm>
#include "include/sort_util.h"

using namespace std;

/**
 * 插入排序算法
 */
template<typename T>
void insertionSort(T arr[], int n) {
    for(int i = 1; i < n; i++) {
        // 寻找第i个位置的元素的合适插入位置
        for(int j = i; j > 0; j--) {
            if(arr[j] < arr[j - 1])
                swap(arr[j], arr[j - 1]);
            else
                break;
        }
    }
}

/**
 * 插入排序算法 优化
 * 减少大量的元素交换耗时
 */
template<typename T>
void insertionSort2(T arr[], int n) {
    for(int i = 1; i < n; i++) {
        // 寻找第i个位置的元素的合适插入位置
        T e = arr[i];
        int j;    // 保存e应该插入的位置
        for(j = i; j > 0 && arr[j - 1] > e; j--) {
            arr[j] = arr[j - 1];
        }
        arr[j] = e;
    }
}

int main(int argc, char const *argv[])
{
    // 插入排序测试
    int n = 10000;
    int *arr = generateRandomArray(n, 0, n);
    int *arr1 = copyIntArray(arr, n);
    testSort("Insertion Sort", insertionSort, arr, n);
    testSort("Insertion Sort2", insertionSort2, arr1, n);
    delete[] arr;
    delete[] arr1;
    arr = NULL;
    arr1 = NULL;
    return 0;
}
