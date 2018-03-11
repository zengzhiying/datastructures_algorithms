#include <iostream>
using namespace std;
class Stack {
public:
    Stack(int max_size);
    ~Stack();
    bool empty();
    bool full();
    void clear();
    int length();
    void push(int element);
    bool pop(int &element);
    void traverse(bool is_from_bottom);

private:
    int *p;
    int max_size;
    // 栈顶 也相当于栈中元素个数
    int stack_top;
};
