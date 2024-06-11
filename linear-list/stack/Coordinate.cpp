#include "Coordinate.h"
#include <iostream>
using namespace std;

/**
 * 栈实例元素, 点坐标实现类
 */

Coordinate::Coordinate(int x, int y) {
    this->x = x;
    this->y = y;
}

void Coordinate::printCoordinate() {
    cout << "(" << x << "," << y << ")" << endl;
}
