#include <iostream>
#include "SequenceList.h"
using namespace std;

int main() {
    // 顺序表数据结构使用示例
    SequenceList *sequence = new SequenceList(10);

    int e = 1;
    sequence->insert(0, &e);
    e = 3;
    sequence->insert(1, &e);
    e = 8;
    sequence->insert(2, &e);
    e = 16;
    sequence->insert(3, &e);
    e = 32;
    sequence->insert(4, &e);

    sequence->remove(3, &e);
    // cout << e << endl;
    sequence->traverse();
    if(!sequence->empty()){
        cout << "not empty!" << endl;
    }
    cout << sequence->length() << endl;
    // sequence->get(3, &e);
    // cout << e << endl;
    // int temp = 8;
    // e = sequence->locate(&temp);
    // cout << e << endl;
    int temp = 8;
    sequence->next(&temp, &e);
    cout << e << endl;
    sequence->clear();
    if(sequence->empty()){
        cout << "empty!" << endl;
    }
    sequence->traverse();

    delete sequence;
    sequence = NULL;
    return 0;
}
