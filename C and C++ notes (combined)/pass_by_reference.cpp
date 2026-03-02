#include <iostream>
using namespace std;
void swap(string &x, string &y);    

int main(){
    string x= "Haroon";  //Pass by Value → “Give me a copy”
    string y= "Ahmad"; // Pass by Reference → “Give me the original” 
    swap(x, y);           //This is pass by value
    cout<<"X: "<<x<<endl;              
    cout<<"Y: "<<y<<endl;  
}

void swap(string &x, string &y){         //pass with reference deals with original values of variables and pass by value copy of values of variables
    //if we don't use & it will called pass by value other wise call by reference
    string temp;
    temp = x;
    x=y;
    y= temp;
}
