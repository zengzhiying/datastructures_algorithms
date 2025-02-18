#include <stdio.h>
#include <math.h>
#include <stdlib.h>

// gcc main.c -lm -o main

// 定义目标函数 f(x) = x^3 - x - 1
double function_value(double x) {
    return pow(x, 3) - x - 1;
}

// 定义目标函数的导数 f'(x) = 3x^2 - 1
double derivative_value(double x) {
    return 3.0 * pow(x, 2) - 1;
}

// 牛顿迭代法求解方程 f(x) = 0 的根
double newton_iteration(double x, double tolerance) {
    double cur_x = x;
    double prev_x;
    int iteration_count = 0;

    do {
        prev_x = cur_x;
        // 计算当前 x 处的函数值
        double value = function_value(prev_x);
        // 计算当前 x 处的导数值
        double dvalue = derivative_value(prev_x);

        // 检查导数是否为零，避免除零错误
        if (dvalue == 0) {
            fprintf(stderr, "导数为零，牛顿迭代法无法继续进行。\n");
            exit(EXIT_FAILURE);
        }

        // 根据牛顿迭代公式更新 x 的值
        cur_x = prev_x - value / dvalue;

        iteration_count++;
    } while (fabs(cur_x - prev_x) > tolerance);

    printf("迭代次数: %d\n", iteration_count);

    return cur_x;
}

int main() {
    // 计算精度
    double tolerance = 1e-9;
    // 初始值
    double x = 1.0;
    double res;

    // 调用牛顿迭代法函数求解方程的根
    res = newton_iteration(x, tolerance);

    // 输出求解结果
    printf("方程根的估计值为：%lf\n", res);

    return 0;
}