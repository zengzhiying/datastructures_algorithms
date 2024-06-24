#include <iostream>
#include <algorithm>
#include "include/sort_util.h"

using namespace std;

/**
 *
 * 插入排序算法修改 对[l, r]闭区间块内的元素进行排序
 */
template<typename T>
void insertionSort(T arr[], int l, int r) {
    for(int i = l + 1; i <= r; i++) {
        // 寻找第i个位置的元素的合适插入位置
        T e = arr[i];
        int j;    // 保存e应该插入的位置
        for(j = i; j > l && arr[j - 1] > e; j--) {
            arr[j] = arr[j - 1];
        }
        arr[j] = e;
    }
}

/**
 *
 * 将[l, mid] 和 [mid + 1, r]两部分进行归并
 */
template<typename T>
void merge(T arr[], int l, int mid, int r) {
    T aux[r - l + 1];
    for(int i = l; i <= r; i++)
        aux[i - l] = arr[i];
    int i = l, j = mid + 1;
    for(int k = l; k <= r; k++) {
        // 范围边界控制
        if(i > mid) {
            arr[k] = aux[j - l];
            j++;
        } else if(j > r) {
            arr[k] = aux[i - l];
            i++;
        }
        // 当索引有效时再次比较元素大小
        else if(aux[i - l] < aux[j - l]) {
            arr[k] = aux[i - l];
            i++;
        } else {
            arr[k] = aux[j - l];
            j++;
        }
    }
}

/**
 *
 * 递归的使用归并排序, 对arr数组 [l...r]的范围进行排序
 */
template<typename T>
void merge_sort(T arr[], int l, int r) {
    // if(l >= r)
    //     return;
    // 优化部分 当n很小时n^2级别的算法要比nlogn的算法快, 所以此时转换为插入排序进行优化
    if(r - l <= 15) {
        insertionSort(arr, l, r);
        return;
    }
    // 计算中点位置
    int mid = (l + r)/2;
    // 分别对两块进行排序
    merge_sort(arr, l, mid);
    merge_sort(arr, mid + 1, r);
    // 对排好序的两段进行归并 只有在mid元素大于mid+1的元素时才执行归并, 减少多余的性能开销
    if(arr[mid] > arr[mid + 1])
        merge(arr, l, mid, r);
}

/**
 *
 * 归并排序主函数
 */
template<typename T>
void mergeSort(T arr[], int n) {
    merge_sort(arr, 0, n - 1);
}

/**
 *
 * 自底向上的归并排序
 */
template<typename T>
void mergeSortBU(T arr[], int n) {
    for(int size = 1; size <= n; size += size)
        for(int i = 0; i + size < n; i += size + size)
            // 对arr [i, i + size - 1]和[i + size - 1, i + 2*size -1]闭区间进行归并排序
            merge(arr, i, i + size - 1, min(i + size + size - 1, n - 1));
}

int main(int argc, char const *argv[])
{
    // 归并排序性能测试
    int n = 1000000;
    int *arr = generateRandomArray(n, 0, n);
    int *arr1 = copyIntArray(arr, n);
    testSort("Merge Sort", mergeSort, arr, n);
    testSort("Merge Sort BU", mergeSortBU, arr, n);
    delete[] arr;
    delete[] arr1;
    arr = NULL;
    arr1 = NULL;
    return 0;
}
