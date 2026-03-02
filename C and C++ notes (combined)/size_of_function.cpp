#include <iostream>
using namespace std;
int main(){
    //sizeof()= determines the size in byte of a:
    // variables, data type, class, objects, etc.
    string name= "Haroon";  //usually will take 32 bytes
    char grade= 'A'; //Will take 1 byte
    bool student= true; //will also take 1 byte
    char grade[]= {'A', 'B', 'C', 'D', 'E'}; //will take 5 bytes 
    cout<<sizeof(grade);
    cout<<sizeof(grade)/sizeof(char)<< " is the length of array";
    
    string students[]= {"Waleed", "Bilal", "Sahil"};
    cout<<sizeof(grade)/sizeof(string)<< " is the length of array";
    

}