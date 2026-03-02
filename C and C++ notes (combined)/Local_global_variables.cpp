#include <iostream>
using namespace std;

int myNum = 8; // GLOBAL variable (Accessible everywhere)

// Fixed the prototype to match the definition
void printNum(int incomingNum); 

int main(){
    
    // LOCAL variable (Only exists inside main)
    int myNum = 2; 
    
    // We pass the local main value (2) into the function
    printNum(myNum); 
    
    // This prints the local variable in main
    cout << "\nInside Main: " << myNum; 
    cout << "\nInside Main: " << ::myNum; 
    //using :: we can give precedence to global variable instead of function variable or LOCAL
    //if we use :: before variable where we are printing it the value of global variable is printed
    return 0;
}

void printNum(int incomingNum){
    // LOCAL variable (Only exists inside this function)
    // This 'shadows' (hides) the global variable 8
    int myNum = 4; 
    
    cout << "Inside Function: " << myNum << '\n';
}