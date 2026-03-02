#include <iostream>
using namespace std;
int main(){
    
    //Null value= a special value that means something has no value
    //            when a pointer is holding a null value, that pointer is not pointing at anything (null pointer)
    //nullptr= keyword represents a null pointer literal
    //nullptrs are helpful when determining if as address was successfully assigned to a pointer
    //when using null pointer be careful that you code isn't dereferecing null or pointing to free memory
    //this will cause undefined behaviour

    int *ptr= nullptr;
    int x= 123;     
    // ptr= &x;      //if we remove this address will not be assigned
    if (ptr==nullptr)
    {
        cout<<"Address didn't assigned";
    }
    else
    {
        cout<<"Address assigned";
        cout<<*ptr;
    }
    
}