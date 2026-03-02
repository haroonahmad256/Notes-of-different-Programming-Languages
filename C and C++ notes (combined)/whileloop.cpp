#include <iostream>
using namespace std;
int main(){
    string name;
    while (name.empty()) //This loop will continue until we don't enter something
    {
        cout<<"ENter your name: ";
        getline(cin, name);
    }
    cout<<"Hello "<<name;
}