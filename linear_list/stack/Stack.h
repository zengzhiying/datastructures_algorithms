#include <iostream>
#include "Coordinate.h"
using namespace std;
class Stack {
public:
    Stack(int max_size);
    ~Stack();
    bool empty();
    bool full();
    void clear();
    int length();
    void push(Coordinate element);
    bool pop(Coordinate &element);
    void traverse(bool is_from_bottom);

private:
    Coordinate *p;
    int max_size;
    // 栈顶 也相当于栈中元素个数
    int stack_top;
};
