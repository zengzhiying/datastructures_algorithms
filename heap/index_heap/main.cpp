#include <iostream>

#include "IndexMaxHeap.h"

using namespace std;

int main()
{
    IndexMaxHeap *index_max_heap = new IndexMaxHeap(6);
    index_max_heap->insert(0, 5);
    index_max_heap->insert(1, 2);
    cout << "size: " << index_max_heap->size() << endl;
    index_max_heap->insert(2, 26);
    cout << "out: " << index_max_heap->extractMax() << endl;
    cout << "out1: " << index_max_heap->extractMaxIndex() << endl;
    index_max_heap->change(1, 8);
    cout << "out1: " << index_max_heap->extractMax() << endl;
    cout << "is empty? " << index_max_heap->isEmpty() << endl;
    delete index_max_heap;
    index_max_heap = NULL;
    return 0;
}
