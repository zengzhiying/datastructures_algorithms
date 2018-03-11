#include <iostream>
#include "Stack.h"
using namespace std;

#define BINARY 2
#define OCTONARY 8
#define HEXADECIMAL 16

int main(int argc, char const *argv[]) {
    char hex_number[] = "0123456789ABCDEF";
    Stack *pStack = new Stack(64);
    void hexStack(Stack *p, int number, int HEX);

    int number = 2017;
    // 二进制
    hexStack(pStack, number, BINARY);
    pStack->traverse(false);
    pStack->clear();
    // 八进制
    hexStack(pStack, number, OCTONARY);
    pStack->traverse(false);
    pStack->clear();
    // 十六进制
    hexStack(pStack, number, HEXADECIMAL);
    // pStack->traverse(false);
    int elem = 0;
    while(!pStack->empty()) {
        pStack->pop(elem);
        cout << hex_number[elem] << "  ";
    }
    cout << endl;

    delete pStack;
    pStack = NULL;
    return 0;
}

void hexStack(Stack *p, int number, int HEX) {
    int mod;
    while(number != 0) {
        mod = number % HEX;
        p->push(mod);
        number /= HEX;
    }
}
