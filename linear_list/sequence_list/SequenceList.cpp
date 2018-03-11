#include <iostream>
#include "SequenceList.h"
using namespace std;

/**
 * 顺序表结构实现类
 */
SequenceList::SequenceList(int max_size) {
    this->max_size = max_size;
    this->element_number = 0;
    p = new int[max_size];
}

SequenceList::~SequenceList() {
    delete[] p;
    p = NULL;
}

void SequenceList::clear() {
    element_number = 0;
}

bool SequenceList::empty() {
    if(element_number == 0) {
        return true;
    }
    return false;
}

int SequenceList::length() {
    return element_number;
}

bool SequenceList::get(int i, int *element) {
    if(i < 0 || i >= max_size) {
        return false;
    }
    *element = p[i];
    return true;
}

int SequenceList::locate(int *element) {
    for(int i = 0; i < element_number; i++) {
        if(p[i] == *element) {
            return i;
        }
    }
    return -1;
}

bool SequenceList::prior(int *current_element, int *prev_element) {
    int index = locate(current_element);
    if(index == -1 || index == 0) {
        return false;
    }
    *prev_element = p[index - 1];
    return true;
}

bool SequenceList::next(int *current_element, int *next_element) {
    int index = locate(current_element);
    if(index == -1 || index == element_number - 1) {
        return false;
    }
    *next_element = p[index + 1];
    return true;
}

void SequenceList::traverse() {
    for(int i = 0; i < element_number; i++) {
        cout << p[i] << " ";
    }
    cout << endl;
}

bool SequenceList::insert(int i, int *element) {
    if(i < 0 || i > element_number || element_number == max_size) {
        return false;
    }
    for(int k = element_number - 1; k >= i; k--) {
        p[k + 1] = p[k];
    }
    p[i] = *element;
    element_number++;
    return true;
}

bool SequenceList::remove(int i, int *element) {
    if(i < 0 || i >= element_number) {
        return false;
    }
    *element = p[i];
    for(int k = i + 1; k < element_number; k++) {
        p[k - 1] = p[k];
    }
    element_number--;
    return true;
}
