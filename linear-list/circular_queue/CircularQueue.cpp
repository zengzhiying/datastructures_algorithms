#include "CircularQueue.h"
#include <iostream>
using namespace std;

/**
 * 环形队列数据结构实现类
 * 因环形队列也是基于线性逻辑结构实现的, 所以环形队列也属于线性表
 */

CircularQueue::CircularQueue(int max_size) {
    this->max_size = max_size;
    this->head = this->tail = 0;
    this->p = new int[max_size];
    this->element_number = 0;
}

CircularQueue::~CircularQueue() {
    delete[] this->p;
    this->p = NULL;
}

void CircularQueue::clear() {
    head = tail = element_number = 0;
}

bool CircularQueue::empty() const {
    if(element_number == 0) {
        return true;
    }
    return false;
}

bool CircularQueue::full() const {
    if(element_number == max_size) {
        return true;
    }
    return false;
}

int CircularQueue::length() const {
    return element_number;
}

bool CircularQueue::enQueue(int element) {
    if(full()) {
        return false;
    }
    p[tail] = element;
    tail++;
    tail = tail % max_size;
    element_number++;
    return true;
}

bool CircularQueue::deQueue(int &element) {
    if(empty()) {
        return false;
    }
    element = p[head];
    head++;
    head = head % max_size;
    element_number--;
    return true;
}

void CircularQueue::traverse() {
    for(int i = head; i < head + element_number; i++) {
        cout << p[i % max_size] << endl;
        cout << "前面还有：" << (i - head) << "个元素！" << endl;
    }
}
