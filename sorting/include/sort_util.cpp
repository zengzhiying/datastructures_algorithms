#include <iostream>
#include <ctime>
#include <cassert>
#include <cstdlib>
using namespace std;

int *generateRandomArray(int n, int rangeL, int rangeR) {
    assert(rangeL <= rangeR);
    int *arr = new int[n];
    // 设置以时间为随机数种子
    srand(time(NULL));
    for (int i = 0; i < n; i++)
    {
        arr[i] = rand() % (rangeR - rangeL + 1) + rangeL;
    }
    return arr;
}

int *generateNearlyOrderedArray(int n, int swap_number) {
    int *arr = new int[n];
    for(int i = 0; i < n; i++) {
        arr[i] = i;
    }
    srand(time(NULL));
    for(int i = 0; i < swap_number; i++) {
        int posx = rand() % n;
        int posy = rand() % n;
        swap(arr[posx], arr[posy]);
    }
    return arr;
}

// template<typename T>
void printArray(int arr[], int n) {
    for(int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

// template<typename T>
bool isSorted(int arr[], int n) {
    for(int i = 0; i < n - 1; i++) {
        if(arr[i] > arr[i + 1]) {
            return false;
        }
    }
    return true;
}

// template<typename T>
void testSort(string sort_name, void(*sort)(int[], int), int arr[], int n) {
    clock_t startTime = clock();
    sort(arr, n);
    clock_t endTime = clock();
    assert(isSorted(arr, n));
    // CLOCKS_PER_SEC表示每秒钟的时钟次数 也就是频率 总次数/频率 = 时间
    cout << sort_name << " loss time: " << double(endTime - startTime)/CLOCKS_PER_SEC << " s" << endl;
}

int *copyIntArray(int a[], int n) {
    int *arr = new int[n];
    copy(a, a + n, arr);
    return arr;
}
