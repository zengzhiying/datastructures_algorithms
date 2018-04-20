#include <iostream>

using namespace std;

#define M 2
#define N 3
#define P 4

/**
 * 矩阵相乘函数的实现
 * 传入参数: 矩阵a, 维度: m*n; 矩阵b, 维度: n*p;
 * 矩阵r为矩阵a, b相乘后的结果矩阵, 维度m*p
 */
void matrix_multiply(int *a,
                     int *b,
                     int m,
                     int n,
                     int p,
                     int **r) {
    // 计算
    for(int i = 0; i < m; i++) {
        for(int j = 0; j < p; j++) {
            // 计算矩阵中每一个元素
            int sum = 0;
            for(int t = 0; t < n; t++)
                sum += (*(a + i*n + t) * *(b + t*p + j));
            // r[i][j] = sum;
            *((int *)r + i*p + j) = sum;
        }
    }
}

int main(int argc, char const *argv[])
{
    int m, n, p;
    m = 2;
    n = 3;
    p = 4;
    // 矩阵乘法 m*n 乘以 n*p => m*p
    int a[M][N] = {{1, 2, 4}, {2, 5, 8}};
    int b[N][P] = {{2, 5, 11, 23}, {6, 10, 7, 9}, {1, 8, 29, 16}};

    int r[M][P];

    // 计算
    // for(int i = 0; i < m; i++) {
    //     for(int j = 0; j < p; j++) {
    //         // 计算结果矩阵中每一个元素
    //         int sum = 0;
    //         for(int t = 0; t < n; t++) {
    //             sum += (a[i][t] * b[t][j]);
    //         }
    //         r[i][j] = sum;
    //     }
    // }
    matrix_multiply((int *)a, (int *)b, m, n, p, (int **)r);

    for(int i = 0; i < m; i++) {
        for(int j = 0; j < p; j++) {
            cout << r[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
