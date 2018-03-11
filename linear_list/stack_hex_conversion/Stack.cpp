#include "Stack.h"

Stack::Stack(int max_size) {
    this->max_size = max_size;
    p = new int[max_size];
    this->stack_top = 0;
}

Stack::~Stack() {
    delete[] p;
    p = NULL;
}

bool Stack::empty() {
    if(0 == stack_top) {
        return true;
    }
    return false;
}

bool Stack::full() {
    if(stack_top == max_size) {
        return true;
    }
    return false;
}

void Stack::clear() {
    stack_top = 0;
}

int Stack::length() {
    return stack_top;
}

void Stack::push(int element) {
    if(!full()) {
        p[stack_top] = element;
        stack_top++;
    }
}

bool Stack::pop(int &element) {
    if(empty()) {
        return false;
    }
    stack_top--;
    element = p[stack_top];
    return true;
}

// bool is_from_bottom true 从栈底到栈顶 false 从栈顶到栈底
void Stack::traverse(bool is_from_bottom) {
    if(is_from_bottom) {
        for(int i = 0; i < stack_top; i++) {
            cout << p[i] << "  ";
        }
    } else {
        for(int i = stack_top - 1; i >= 0; i--) {
            cout << p[i] << "  ";
        }
    }
    cout << endl;
}
