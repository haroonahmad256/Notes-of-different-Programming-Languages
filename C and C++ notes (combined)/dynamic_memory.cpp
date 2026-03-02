#include <iostream>
using namespace std;
int main(){
    /*
    Dynamic memory: Memory that is allocated after the program is usually compiled and running. 
    Use the 'new' operator to allocate memory in heap rather than stack.
    Useful when we know how much memory we will need. Makes our program more flexible, 
    especially when accepting user input
    */
    int *ptr= NULL;
    ptr= new int;
    *ptr= 12;
    cout<<"The address\n"<<ptr;
    cout<<"The value: "<<*ptr;
    delete ptr;
    /*
    We wouldn't allocate memory dynamically without any point we would do this when we don't 
    know the size. A dynamic array might be preferred if: the maximum logical size is unknown, 
    or difficult to calculate, before the array is allocated.
    useful when we don't know how much memory we will need. Makes our program more flexible, especially
    when taking user input
    */
    char *pgrade = NULL;
    int size;
    cout<<"How many grades to enter in?:";
    cin>>size;
    pgrade = new char[size];
    for (int i = 0; i < size; i++)
    {
        cout<<"Enter #"<<i+1<<": ";
        cin>>pgrade[i];
    }
    
    for (int i = 0; i < size; i++)
    {
        cout<<pgrade[i]<<" ";
    }
    delete pgrade;

}