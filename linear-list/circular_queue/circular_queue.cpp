#include <iostream>
#include "CircularQueue.h"
using namespace std;

int main() {
    // 环形队列使用示例
    CircularQueue *p = new CircularQueue(4);

    p->enQueue(10);
    p->enQueue(12);
    p->enQueue(16);
    p->enQueue(18);
    // 插入失败
    p->enQueue(20);
    p->traverse();
    int e = 0;
    p->deQueue(e);
    cout << "取到: " << e << endl;
    p->traverse();
    p->deQueue(e);
    cout << "取到: " << e << endl;
    p->traverse();
    p->enQueue(36);
    p->traverse();
    p->clear();
    cout << "清空." << endl;
    p->traverse();
    cout << endl;
    p->enQueue(10);
    p->enQueue(18);
    p->traverse();

    delete p;
    p = NULL;
    return 0;
}
