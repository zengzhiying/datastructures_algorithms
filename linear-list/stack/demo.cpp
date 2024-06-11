#include <iostream>
#include "Stack.h"
using namespace std;

int main(int argc, char const *argv[]) {
    // 数据结构 - 栈, 使用示例
    Stack *sta = new Stack(5);
    sta->push(Coordinate(1, 2));
    sta->push(Coordinate(5, 8));
    sta->push(Coordinate(6, 3));

    Coordinate coor;
    sta->pop(coor);
    coor.printCoordinate();
    cout << sta->length() << endl;
    sta->pop(coor);
    coor.printCoordinate();
    sta->traverse(true);

    sta->clear();

    if(sta->empty()) {
        cout << "stack empty!" << endl;
    }
    if(sta->full()) {
        cout << "stack full!" << endl;
    }
    delete sta;
    sta = NULL;
    return 0;
}
