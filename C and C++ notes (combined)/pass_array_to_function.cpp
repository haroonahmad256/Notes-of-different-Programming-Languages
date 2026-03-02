#include <iostream>
using namespace std;
void print_array(string arr[]); //it is not necessary to specify the length of array 
int main(){
    string arr1[]= {"Haroon", "Ahsan", "Bilal"};
    print_array(arr1);        //we only need to pass array name 
}
void print_array(string arr[]){
    for (int i = 0; i < 10; i++)
    {
        printf("%s", arr[i]);
    }
    
}
// return -1 is used usually when something is not found