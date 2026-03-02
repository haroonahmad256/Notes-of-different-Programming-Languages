#include <iostream>
using namespace std;
int main(){
    //pointers = These are the variables in c++ which store the memory address of another variable
    //           sometimes it is easier to work with an address

    //& address-of operator      it is used to give the address of variable
    //* dereference operator     it gives the value of variable at a particular address
    string me= "Haroon";
    string *ptr= &me;   //data type of pointer and variable should be same
    cout<<ptr;
    cout<<*ptr; //vaue at address
    string freeburgers[]={"burger1", "burger2", "burger3", "burger4", "burger5"};
    //instead of distributing free burgers home by home we can simply tell the address to homies so thry can collect burgers
    int age=34;
    int *ptr2= &age;
    cout<<ptr2<<endl;
    cout<<*ptr2;
    string *ptr3= freeburgers;  //array is already a pointer so we don't use & 
    //To print address of freeburger we can simply do this
    cout<<freeburgers<<'\n';
    cout<<ptr3<<'\n'; //but this will give the value of array first element
    return 0;
}