#include <iostream>
#include <algorithm>
#include "include/sort_util.h"

using namespace std;

/**
 * 选择排序算法
 */
template<typename T>
void selectionSort(T arr[], int n) {
    // 外层循环依次选定每组最小值
    for(int i = 0; i < n; i++) {
        // 对于每一个i寻找[i, n)区间的最小值并交换
        int minIndex = i;
        for(int j = i + 1; j < n; j++) {
            if(arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        // 已经找到最小值, 进行交换  另外swap函数在标准库std中
        swap(arr[i], arr[minIndex]);
    }
}

int main(int argc, char const *argv[])
{
    // 选择排序测试
    int n = 10000;
    int *arr = generateRandomArray(n, 0, n);
    testSort("Selection Sort", selectionSort, arr, n);
    delete[] arr;
    arr = NULL;
    return 0;
}
