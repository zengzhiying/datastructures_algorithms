#include <iostream>
#include "OneWarLinkedList.h"
using namespace std;

int main(int argc, char const *argv[]) {
    // 单向链表数据结构使用示例
    OneWarLinkedList * pLinked = new OneWarLinkedList();

    Node node;
    node.data = 4;
    pLinked->insertHead(&node);
    node.data = 3;
    pLinked->insertHead(&node);

    node.data = 5;
    pLinked->insertTail(&node);
    node.data = 6;
    pLinked->insertTail(&node);

    Node * node1 = new Node;
    node1->data = 2;
    pLinked->insert(0, node1);
    delete node1;
    node1 = NULL;

    Node temp;
    pLinked->remove(2, &temp);

    pLinked->traverse();

    cout << "remove temp: " << temp.data << endl;

    pLinked->get(1, &temp);
    cout << "get temp: " << temp.data << endl;

    temp.data = 3;
    pLinked->prior(&temp, &temp);
    cout << "prev node: " << temp.data << endl;

    temp.data = 3;
    pLinked->next(&temp, &temp);
    cout << "next node: " << temp.data << endl;

    delete pLinked;
    pLinked = NULL;
    return 0;
}
