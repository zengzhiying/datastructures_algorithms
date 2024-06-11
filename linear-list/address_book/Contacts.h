#include <string>
#include <ostream>
#include <iostream>
using namespace std;

class Contacts {
    // 输出方法全局重写
    friend ostream &operator << (ostream &out, Contacts &contacts);
public:
    string name;    // 姓名
    string phone;   // 电话号码
    Contacts &operator = (Contacts &contacts);  // 赋值方法重载
    bool operator == (Contacts &contacts);  // 判断是否相等重载
};
