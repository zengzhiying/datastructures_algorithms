package com.monchickey;

public class MergeSort {
    public static void main(String[] args) {
        int[] arr = {11, 44, 23, 67, 88, 65, 34, 48, 9, 12};
        mergeSort(arr);
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }

    public static void merge(int[] arr, int low, int mid, int high) {
        int[] tmp = new int[high - low + 1];
        for(int i = low; i <= high; i++) {
            tmp[i - low] = arr[i];
        }

        int i = low, j = mid + 1;
        // 归并代码1
        int k = low;
        while (i <= mid && j <= high) {
            if (tmp[i-low]<=tmp[j-low]) {
                arr[k++] = tmp[i-low];
                i++;
            } else {
                arr[k++] = tmp[j-low];
                j++;
            }
        }
        while (i <= mid) {
            arr[k++] = tmp[i-low];
            i++;
        }
        while (j<=high) {
            arr[k++] = tmp[j-low];
            j++;
        }

        // 归并代码2
//        for(int k = low; k <= high; k++) {
//            if(i > mid) {
//                arr[k] = tmp[j - low];
//                j++;
//            } else if(j > high) {
//                arr[k] = tmp[i - low];
//                i++;
//            } else if(tmp[i - low] < tmp[j - low]) {
//                arr[k] = tmp[i - low];
//                i++;
//            } else {
//                arr[k] = tmp[j - low];
//                j++;
//            }
//        }
    }

    public static void mergeSort(int[] arr) {
        mergeSort(arr, 0, arr.length - 1);
    }


    public static void mergeSort(int[] arr, int low, int high) {
        if(low >= high)
            return;

        int mid = low + ((high - low) >> 1);
        mergeSort(arr, low, mid);
        mergeSort(arr, mid + 1, high);
        if(arr[mid] > arr[mid + 1])
            merge(arr,low,mid,high);
    }
}
