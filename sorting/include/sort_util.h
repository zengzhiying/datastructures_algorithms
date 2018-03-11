#ifndef SORT_UTIL_H

#define SORT_UTIL_H

using namespace std;

// 生成随机数组
int *generateRandomArray(int n, int rangeL, int rangeR);
// 生成近乎有序的数组
int *generateNearlyOrderedArray(int n, int swap_number);
// 打印数组元素
void printArray(int arr[], int n);
// 判断数组是否已排好序
bool isSorted(int arr[], int n);
// 测试排序函数耗时
void testSort(string sort_name, void(*sort)(int[], int), int arr[], int n);
// 拷贝整型数组为一个新的数组
int *copyIntArray(int a[], int n);

#endif