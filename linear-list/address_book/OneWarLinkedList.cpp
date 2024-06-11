#include "OneWarLinkedList.h"
#include <iostream>
using namespace std;

OneWarLinkedList::OneWarLinkedList() {
    pNode = new Node;
    // pNode->data = 0;
    pNode->next = NULL;
    this->element_number = 0;
}

OneWarLinkedList::~OneWarLinkedList() {
    clear();
    delete pNode;
    pNode = NULL;
}

void OneWarLinkedList::clear() {
    Node * currentNode = pNode->next;
    while (currentNode != NULL) {
        Node *temp = currentNode->next;
        delete currentNode;
        currentNode = temp;
    }
    pNode->next = NULL;
    element_number = 0;
}

bool OneWarLinkedList::empty() {
    if(element_number == 0) {
        return true;
    }
    return false;
}

int OneWarLinkedList::length() {
    return element_number;
}

bool OneWarLinkedList::insertHead(Node *node) {
    Node * temp = this->pNode->next;
    Node * newNode = new Node;
    if(newNode == NULL) {
        return false;
    }
    newNode->data = node->data;
    this->pNode->next = newNode;
    newNode->next = temp;
    element_number++;
    return true;
}

bool OneWarLinkedList::insertTail(Node *node) {
    Node * currentNode = pNode;
    while(currentNode->next != NULL) {
        currentNode = currentNode->next;
    }
    Node * newNode = new Node;
    if(newNode == NULL) {
        return false;
    }
    newNode->data = node->data;
    newNode->next = NULL;
    currentNode->next = newNode;
    element_number++;
    return true;
}

bool OneWarLinkedList::insert(int i, Node *node) {
    if(i < 0 || i > element_number) {
        return false;
    }
    Node * currentNode = pNode;
    for(int k = 0; k < i; k++) {
        currentNode = currentNode->next;
    }
    Node * newNode = new Node;
    newNode->data = node->data;
    newNode->next = currentNode->next;
    currentNode->next = newNode;
    return true;
}

bool OneWarLinkedList::remove(int i, Node *node) {
    if(i < 0 || i >= element_number) {
        return false;
    }
    Node * currentNode = pNode;
    Node * currentNodeBefore = NULL;
    for(int k = 0; k <= i; k++) {
        currentNodeBefore = currentNode;
        currentNode = currentNode->next;
    }
    currentNodeBefore->next = currentNode->next;
    node->data = currentNode->data;
    delete currentNode;
    currentNode = NULL;
    element_number--;
    return true;
}

bool OneWarLinkedList::get(int i, Node *node) {
    if(i < 0 || i >= element_number) {
        return false;
    }
    Node * currentNode = pNode;
    // Node * currentNodeBefore = NULL;
    for(int k = 0; k <= i; k++) {
        // currentNodeBefore = currentNode;
        currentNode = currentNode->next;
    }
    node->data = currentNode->data;
    return true;
}

int OneWarLinkedList::locate(Node *node) {
    Node * currentNode = pNode;
    int index = 0;
    while(currentNode->next != NULL) {
        currentNode = currentNode->next;
        if(currentNode->data.name == node->data.name) {
            return index;
        }
        index++;
    }
    return -1;
}

bool OneWarLinkedList::prior(Node *pCurrentNode, Node *prevNode) {
    Node * currentNode = pNode;
    Node * tempNode = NULL;
    while(currentNode->next != NULL) {
        tempNode = currentNode;
        currentNode = currentNode->next;
        if(currentNode->data == pCurrentNode->data) {
            if(tempNode == pNode) {
                return false;
            }
            prevNode->data = tempNode->data;
            return true;
        }
    }
    return false;
}

bool OneWarLinkedList::next(Node *pCurrentNode, Node *nextNode) {
    Node * currentNode = pNode;
    while(currentNode->next != NULL) {
        currentNode = currentNode->next;
        if(currentNode->data == pCurrentNode->data) {
            if(currentNode->next == NULL) {
                return false;
            }
            nextNode->data = currentNode->next->data;
            return true;
        }
    }
    return false;
}

void OneWarLinkedList::traverse() {
    Node * currentNode = pNode;
    while(currentNode->next != NULL) {
        currentNode = currentNode->next;
        currentNode->printNode();
    }
}
