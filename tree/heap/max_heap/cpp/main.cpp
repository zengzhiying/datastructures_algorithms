#include <iostream>
#include <ctime>
#include <cstdlib>
#include "MaxHeap.h"

using namespace std;

int main(int argc, char const *argv[])
{
    MaxHeap maxheap = MaxHeap(100);
    srand(time(NULL));
    for(int i = 0; i < 15; i++) {
        maxheap.insert(rand() % 100);
    }
    cout << maxheap.size() << endl;
    while(!maxheap.isEmpty())
        cout << maxheap.extractMax() << " ";
    cout << endl;
    return 0;
}
