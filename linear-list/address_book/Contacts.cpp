#include "Contacts.h"

Contacts &Contacts::operator = (Contacts &contacts) {
    this->name = contacts.name;
    this->phone = contacts.phone;
    return *this;
}

bool Contacts::operator == (Contacts &contacts) {
    if(this->name == contacts.name && this->phone == contacts.phone) {
        return true;
    }
    return false;
}


ostream &operator << (ostream &out, Contacts &contacts) {
    out << contacts.name << " : " << contacts.phone << endl;
    return out;
}
