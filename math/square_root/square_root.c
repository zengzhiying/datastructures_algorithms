#include <stdio.h>
#include <math.h>
#include <sys/time.h>

double newton_sqrt(double x)
{
    const double EPS = 1e-6;
    if(x < EPS)
        return 0;
    double x_next = x;
    double x_last;
    do {
        x_last = x_next;
        x_next = (x_next + x / x_next) / 2;
    } while (fabs(x_next - x_last) > EPS);  // 注意如果错用abs会出现非常奇异的行为: 默认会占用cpu 100%; 但是如果在上面加一行打印就没问题
    return x_next;
}

double binary_sqrt(double x)
{
    const double EPS = 1.0e-6;
    if(x < EPS)
        return 0;
    double low = 0.0;
    double high = x;
    double mid = 0.0;
    double last_mid = 1.0;
    while(fabs(mid - last_mid) > EPS) {
        last_mid = mid;
        mid = (low + high) / 2;
        if(mid * mid > x)
            high = mid;
        else
            low = mid;
    }
    return mid;
}

float quick_sqrt(float number)
{
    // printf("%d, %d\n", sizeof(long), sizeof(int));
    // int 和 long都可以, int速度更快
    long i;
    float x2, y;
    const float threehalfs = 1.5F;

    x2 = number * 0.5F;
    y = number;
    i = *(long *)&y;
    i = 0x5f3759df - (i >> 1);
    y = *(float *)&i;

    y = y * (threehalfs - (x2 * y * y));
    y = y * (threehalfs - (x2 * y * y));
    // y = y * (threehalfs - (x2 * y * y));
    // y = 1/sqrt(n) => sqrt(n) = n * y or sqrt(n) = 1/y
    return number * y;
}

float quick_streamline_sqrt(float x)
{
    // 快速开方精简版
    float xhalf = 0.5F * x;
    int i = *(int *)&x;
    i = 0x5f375a86 - (i >> 1);
    x = *(float *)&i;
    x = x * (1.5F - xhalf * x * x);
    return x;
}


int main(int argc, char const *argv[])
{
    double newton_sqrt(double x);
    double x = 1024;
    printf("math.h sqrt(1024) = %lf\n", sqrt(x));
    printf("newton sqrt(1024) = %lf\n", newton_sqrt(x));
    printf("binary sqrt(1024) = %lf\n", binary_sqrt(x));
    printf("quick sqrt(1024) = %lf\n", quick_sqrt(x));
    printf("quick streamline sqrt(1024) = %lf\n", 1/quick_streamline_sqrt(x));

    int i = 0;
    double use_time;
    struct timeval time1, time2;
    gettimeofday(&time1, NULL);
    for(i = 0; i < 100000; i++)
        sqrt(x);
    gettimeofday(&time2, NULL);
    use_time = (time2.tv_sec - time1.tv_sec) + (time2.tv_usec - time1.tv_usec) / 1e6;
    printf("Time1 math sqrt: %lf\n", use_time);

    gettimeofday(&time1, NULL);
    for(i = 0; i < 100000; i++)
        newton_sqrt(x);
    gettimeofday(&time2, NULL);
    use_time = (time2.tv_sec - time1.tv_sec) + (time2.tv_usec - time1.tv_usec) / 1e6;
    printf("Time2 newton sqrt: %lf\n", use_time);

    gettimeofday(&time1, NULL);
    for(i = 0; i < 100000; i++)
        binary_sqrt(x);
    gettimeofday(&time2, NULL);
    use_time = (time2.tv_sec - time1.tv_sec) + (time2.tv_usec - time1.tv_usec) / 1e6;
    printf("Time3 binary sqrt: %lf\n", use_time);

    gettimeofday(&time1, NULL);
    for(i = 0; i < 100000; i++)
        quick_sqrt(x);
    gettimeofday(&time2, NULL);
    use_time = (time2.tv_sec - time1.tv_sec) + (time2.tv_usec - time1.tv_usec) / 1e6;
    printf("Time4 quick sqrt: %lf\n", use_time);

    gettimeofday(&time1, NULL);
    for(i = 0; i < 100000; i++)
        quick_streamline_sqrt(x);
    gettimeofday(&time2, NULL);
    use_time = (time2.tv_sec - time1.tv_sec) + (time2.tv_usec - time1.tv_usec) / 1e6;
    printf("Time5 quick streamline sqrt: %lf\n", use_time);
    return 0;
}
