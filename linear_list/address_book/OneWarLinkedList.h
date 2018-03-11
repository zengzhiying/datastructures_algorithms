#ifndef LINEAR_LIST_ONE_WAY_LINKED_LIST_H_
#define LINEAR_LIST_ONE_WAY_LINKED_LIST_H_
#include "Node.h"

class OneWarLinkedList {
public:
    OneWarLinkedList();
    ~OneWarLinkedList();
    void clear();
    bool empty();
    int length();
    bool get(int i, Node *node);
    int locate(Node *node);
    bool prior(Node *pCurrentNode, Node *prevNode);
    bool next(Node *pCurrentNode, Node *nextNode);
    void traverse();
    bool insert(int i, Node *node);
    bool remove(int i, Node *node);
    bool insertHead(Node *node);
    bool insertTail(Node *node);
private:
    Node *pNode;
    int element_number; // 当前长度
};

#endif
