#include <iostream>
#include <algorithm>
#include "include/sort_util.h"

using namespace std;

/**
 *
 * partition 数组分割函数, 对[l, r]闭区间进行分割并返回下标索引
 * 下标索引p使得: arr[l,...,p - 1] < arr[p] 并且 arr[p + 1,...,r] > arr[p]
 */
template<typename T>
int partition(T arr[], int l, int r) {
    // 从第一个元素开始取并且partition
    T v = arr[l];
    // arr[l + 1,...,j] < v ; arr[j + 1,...,i) > v 初始条件下区间都为空
    int j = l;
    for(int i = l + 1; i <= r; i++) {
        if(arr[i] < v) {
            swap(arr[j + 1], arr[i]);
            j++;
        }
    }
    swap(arr[l], arr[j]);
    return j;
}

/**
 * 对arr [l, r]闭区间中元素进行快速排序
 */
template <typename T>
void quick_sort(T arr[], int l, int r) {
    if(l >= r)
        return;
    // partition操作
    int p = partition(arr, l, r);
    quick_sort(arr, l, p - 1);
    quick_sort(arr, p + 1, r);
}

/**
 * 快速排序主函数
 */
template <typename T>
void quickSort(T arr[], int n) {
    quick_sort(arr, 0, n - 1);
}

// --------- 快速排序算法优化1 应用于几乎有序的数组, 时间复杂度期望为:nlog(n) ---------

/**
 * 数组在近乎有序时, 默认的时间复杂度变成了O(n^2)
 * 这里优化partition函数, 随机选择标定元素
 * 
 * 由于标定随机数的耗时, 所以在完全随机情况下, 优化算法稍稍慢于原来的算法, 但耗时很接近
 */
template<typename T>
int partition1(T arr[], int l, int r) {
    // 随机取出元素来partition
    swap(arr[l], arr[rand() % (r - l + 1) + l]);
    T v = arr[l];
    // arr[l + 1,...,j] < v ; arr[j + 1,...,i) > v 初始条件下区间都为空
    int j = l;
    for(int i = l + 1; i <= r; i++) {
        if(arr[i] < v) {
            swap(arr[j + 1], arr[i]);
            j++;
        }
    }
    swap(arr[l], arr[j]);
    return j;
}

/**
 * 快速排序优化1 - 区间排序
 */
template <typename T>
void quick_sort1(T arr[], int l, int r) {
    if(l >= r)
        return;
    // partition操作
    int p = partition1(arr, l, r);
    quick_sort1(arr, l, p - 1);
    quick_sort1(arr, p + 1, r);
}

/**
 * 快速排序优化函数主函数1
 */
template <typename T>
void quickSort1(T arr[], int n) {
    srand(time(NULL));  // 初始化随机数种子
    quick_sort1(arr, 0, n - 1);
}


// --------- 快速排序算法优化2 应用于大量重复元素的数组, 时间复杂度期望为:nlog(n) ---------

/**
 * 数组在存在绝大部分相同元素时, 快速排序默认的时间复杂度又变成了O(n^2)
 * 这里优化partition函数, 减少大量不均衡的partition
 *
 * 此算法同样适用于完全随机数组的排序, 而且效率会更好
 */
template<typename T>
int partition2(T arr[], int l, int r) {
    // 随机取出元素来partition
    swap(arr[l], arr[rand() % (r - l + 1) + l]);
    T v = arr[l];
    // arr[l + 1,...,i) <= v; arr(j,...,r] >= v 初始为空
    int i = l + 1, j = r;
    while(true) {
        while(i <= r && arr[i] < v) i++;
        while(j >= l + 1 && arr[j] > v) j--;
        if(i > j) break;
        swap(arr[i], arr[j]);
        i++;
        j--;
    }
    swap(arr[l], arr[j]);
    return j;
}

/**
 * 快速排序优化2 - 区间排序
 */
template <typename T>
void quick_sort2(T arr[], int l, int r) {
    if(l >= r)
        return;
    // partition操作
    int p = partition2(arr, l, r);
    quick_sort2(arr, l, p - 1);
    quick_sort2(arr, p + 1, r);
}

/**
 * 快速排序优化函数主函数
 */
template <typename T>
void quickSort2(T arr[], int n) {
    srand(time(NULL));  // 初始化随机数种子
    quick_sort2(arr, 0, n - 1);
}

// --------- 快速排序算法优化3 三路快速排序 在存在大量相同元素的数组上性能远远超过其他的快速排序, 在随机数组上性能和其他快速排序相近 ---------


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
 * 三路快速排序处理 arr[l...r]
 * 将arr[l...r] 分为 < v; == v; > v 三部分
 * 分完之后对 < v; > v 两部分继续递归进行三路快速排序
 * 将等于v的值抽出, 可以减少大量的元素操作, 从而优化算法的性能
 */
template <typename T>
void quick_sort_3ways(T arr[], int l, int r) {
    // 这里元素数量过少时使用插入排序
    // 同时会避免递归到最后的错误
    if(r - l <= 15) {
        insertionSort(arr, l, r);
        return;
    }

    // partition 操作
    // int rand_number = rand() % (r - l + 1) + l;
    // cout << rand_number << endl;
    swap(arr[l], arr[rand() % (r - l + 1) + l]);
    T v = arr[l];
    // cout << l << "," << r << endl;

    // 设置初始分割区间, 初始为空
    int lt = l;  // arr[l + 1...lt] < v
    int gt = r + 1;  // arr[gt...r] > v
    int i = l + 1;  // arr[lt + 1...i) == v
    while(i < gt) {
        if(arr[i] < v) {
            swap(arr[i], arr[lt + 1]);
            lt++;
            i++;
        } else if(arr[i] > v) {
            swap(arr[i], arr[gt - 1]);
            gt--;
        } else { // arr[i] == v
            i++;
        }
    }

    swap(arr[l], arr[lt]);
    quick_sort_3ways(arr, l, lt - 1);
    quick_sort_3ways(arr, gt, r);
}

template <typename T>
void quickSort3Ways(T arr[], int n) {
    srand(time(NULL));
    quick_sort_3ways(arr, 0, n - 1);
}

int main()
{
    int n = 1000000;
    int *arr = generateRandomArray(n, 0, n);
    int *arrR = copyIntArray(arr, n);
    testSort("Quick Sort", quickSort, arr, n);
    testSort("Quick Sort1", quickSort1, arrR, n);
    // testSort("Quick Sort2", quickSort2, arrR, n);
    // 生成近乎有序的数组 应用于优化的快速排序函数
    int *arr1 = generateNearlyOrderedArray(n, 100);
    testSort("Quick Sort1", quickSort1, arr1, n);
    // 生成大量重复元素的数组
    int *arr2 = generateRandomArray(n, 0, 100);
    testSort("Quick Sort2", quickSort2, arr2, n);
    // 三路快排测试
    int *arr3 = generateRandomArray(n, 0, n);
    testSort("Quick Sort 3Ways", quickSort3Ways, arr3, n);
    delete[] arr;
    arr = NULL;
    delete[] arrR;
    arrR = NULL;
    delete[] arr1;
    arr1 = NULL;
    delete[] arr2;
    arr2 = NULL;
    delete[] arr3;
    arr3 = NULL;
    return 0;
}
