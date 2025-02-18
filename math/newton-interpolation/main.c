#include <stdio.h>

// 计算差商表
void divided_differences(double x[], double f[][18], int n) {
    // 计算一阶及更高阶差商
    for (int i = 1; i < n; i++) {
        for (int j = i; j < n; j++) {
            f[i][j] = (f[i - 1][j] - f[i - 1][j - 1]) / (x[j] - x[j - i]);
        }
    }
}

// 牛顿插值法计算函数值
double newton_interpolation(double x[], double f[][18], int n, double X) {
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
    double f[18][18];
    int n = 9;

    // 待估计自变量
    double X = 0.32;

    double x[9] = {0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9};
    
    double y[9] = {0.9950041652780258, 0.9800665778412416, 0.955336489125606, 0.9210609940028851, 0.8775825618903728, 0.8253356149096783, 0.7648421872844885, 0.6967067093471654, 0.6216099682706644};

    // x: 0.32, y: 0.9492
    for(int i = 0; i < n; i++) {
        f[0][i] = y[i];
    }

    // 计算差商表
    divided_differences(x, f, n);
    // 进行牛顿插值计算
    double estimated_value = newton_interpolation(x, f, n, X);

    // 输出结果
    printf("根据牛顿插值法得到的函数估计值为：f(%.9lf) = %.9lf\n", X, estimated_value);

    return 0;
}