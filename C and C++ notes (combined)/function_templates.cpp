#include <iostream>
using namespace std;
template <typename L, typename U>   //this is template file for function template
L is_greater(L a, U b){  
/* Using L and U allows us to handle variables of any data type; they act as "universal" labels. 
Normally, if you pass a decimal (float) into a function made for whole numbers (integers), 
it won’t work correctly. However, with a Function Template, you can pass in almost any 
type—whether it is an integer or a decimal—and it will run smoothly. To use this, we simply 
add the template line at the very top. */
//The main benefit of this is we don't have to overload function or write same function multiple time to pass different data types
    return (a>b)? a:b;
}
int main(){
    /*
    Function templates describe what the function look like 
    Can be used to generate as many overloaded functions as needed each using different data types
    */
   is_greater('a', 3.9);

}