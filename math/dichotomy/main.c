#include <stdio.h>
#include <math.h>
#include <stdlib.h>

// 定义目标函数 f(x) = x^3 - x - 1
double function_value(double x) {
    return pow(x, 3) - x - 1;
}

// 二分法求解方程 f(x) = 0 在区间 [a, b] 内的根
double dichotomy(double l, double r, double tolerance) {
    double root;
    int iteration_count = 0;

    // 检查区间端点是否满足二分法条件
    if (function_value(l) * function_value(r) >= 0) {
        fprintf(stderr, "输入的区间端点不满足二分法条件，函数在区间两端点的值必须异号。\n");
        exit(EXIT_FAILURE);
    }

    // 二分法迭代过程
    while (fabs(r - l) > tolerance) {
        root = (l + r) / 2.0;
        iteration_count++;

        if (function_value(l) * function_value(root) < 0) {
            // 根在左半区间
            r = root;
        } else if (function_value(l) * function_value(root) > 0) {
            // 根在右半区间
            l = root;
        } else {
            // 找到精确根
            break;
        }
    }

    // 最终根的计算
    root = (l + r) / 2.0;
    printf("二分法迭代次数: %d\n", iteration_count);

    return root;
}

int main() {
    double l, r, root;
    // 计算精度
    double tolerance = 1e-6;

    // 设置初值，符合 f(l)*f(r) < 0
    l = 1;
    r = 2;

    // 调用二分法函数求解方程的根
    root = dichotomy(l, r, tolerance);

    printf("方程根的近似值为：%lf\n", root);

    return 0;
}