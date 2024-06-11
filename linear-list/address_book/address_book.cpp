#include <iostream>
#include "OneWarLinkedList.h"
using namespace std;

int main(int argc, char const *argv[]) {
    int menu();
    void create_contacts(OneWarLinkedList * pLinked);
    bool delete_contacts(OneWarLinkedList * pLinked);
    int user_order = 0;
    OneWarLinkedList * pLinked = new OneWarLinkedList();
    while(user_order != 4) {
        user_order = menu();
        // 用户操作开始
        switch (user_order) {
            case 1:
                cout << "new contacts: " << endl;
                create_contacts(pLinked);
                break;
            case 2:
                cout << "remove contacts: " << endl;
                if(delete_contacts(pLinked)) {
                    cout << "remove ok!" << endl;
                } else {
                    cout << "remove error!" << endl;
                }
                break;
            case 3:
                cout << "browse book: " << endl;
                pLinked->traverse();
                break;
            case 4:
                cout << "exit book: " << endl;
                break;
            default:
                break;
        }
    }

    delete pLinked;
    pLinked = NULL;
    return 0;
}

/**
 * 显示通讯录菜单
 */
int menu() {
    cout << "address book menu: " << endl;
    cout << "1. new contacts" << endl;
    cout << "2. remove contacts" << endl;
    cout << "3. browse book" << endl;
    cout << "4. exit book" << endl;

    cout << "Please enter: ";
    int order = 0;
    cin >> order;

    return order;
}

void create_contacts(OneWarLinkedList * pLinked) {
    Node node;
    Contacts contacts;
    cout << "Please input name: ";
    cin >> contacts.name;
    cout << "Please input phone: ";
    cin >> contacts.phone;
    node.data = contacts;
    pLinked->insertTail(&node);
}

bool delete_contacts(OneWarLinkedList * pLinked) {
    Node node;
    Contacts contacts;
    cout << "Please input name: ";
    cin >> contacts.name;
    node.data.name = contacts.name;
    int index = pLinked->locate(&node);
    if(index == -1) {
        return false;
    }
    pLinked->remove(index, &node);
    return true;
}
