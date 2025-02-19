#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// 计算差商表
void divided_differences(double x[], double **f, int n) {
    for (int i = 1; i < n; i++) {
        for (int j = i; j < n; j++) {
            f[i][j] = (f[i - 1][j] - f[i - 1][j - 1]) / (x[j] - x[j - i]);
        }
    }
}

// 牛顿插值法计算函数值
double newton_interpolation(double x[], double **f, int n, double X) {
    double result = f[0][0];
    double term = 1.0;
    // 根据差商表计算插值结果
    for (int i = 1; i < n; i++) {
        term *= (X - x[i - 1]);
        result += f[i][i] * term;
    }
    return result;
}

int main() {
    int n = 9;
    double **f = (double **) malloc(n * sizeof(double *));
    double *x;
    for(int i = 0; i < n; i++) {
        f[i] = (double *) malloc(n * sizeof(double));
        x = (double *) malloc(n * sizeof(double));
    }

    // 待估计自变量
    // x: 0.32, y: 0.9492
    double X = 0.32;

    // cos 函数测试
    double x0 = 0.1;
    for(int i = 0; i < n; i++) {
        x[i] = x0;
        f[0][i] = cos(x[i]);
        x0 += 0.1;
    }

    // 计算差商表
    divided_differences(x, f, n);
    // 进行牛顿插值计算
    double estimated_value = newton_interpolation(x, f, n, X);

    // 输出结果
    printf("根据牛顿插值法得到的函数估计值为：f(%.9lf) = %.9lf\n", X, estimated_value);

    free(x);
    for(int i = 0; i < n; i++) {
        free(f[i]);
    }
    free(f);

    return 0;
}
