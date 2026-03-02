#include <iostream>
using namespace std;
string concatstrings(string firstname, string lastname);
int main(){
    string firstname, lastname;
    firstname= "Haroon";
    lastname= "Ahmad";
    cout<<concatstrings(firstname, lastname);
    
}
string concatstrings(string firstname, string lastname){
    return firstname+ " " +lastname;
}