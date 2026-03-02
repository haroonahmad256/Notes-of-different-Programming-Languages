// inheritance= a class can receive attributes and methods from another class 
// children classes inherit from parent class
// helps to reuse similar code found within multiple classes
#include <iostream>
using namespace std;
class countries{
    public:
        string province= "exist";

    void area(){
        cout<<"Countries have an large area\n";
    }
};

class Pakistan: public countries{
    public:
        string for_famous= "Northern Areas";

    void famous(){
        cout<<"Pakistan is a famous country";
    }

};

int main(){
    Pakistan paki;
    cout<<paki.province<<endl;
    paki.area();
    cout<<endl;
    cout<<paki.for_famous<<endl;
    paki.famous();
}