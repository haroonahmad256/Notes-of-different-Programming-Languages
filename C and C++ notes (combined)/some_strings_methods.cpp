#include <iostream>
#include <string>
using namespace std;
int main(){
    string name;
    cout<<"Enter your name: ";
    getline(cin, name);  //This will input the string
    // name.length();  //This will give the length of string
    cout<<name; //printing
    name.clear(); //This function clear the content of string you entered 
    name.append("is the greates player of all time"); //append method combines two strings
    cout<<name.at(1);  ///This will give the character at given index
    name.insert(0, "how are you"); //0 is the index number and how are you is the string we want to inset in string at index 0
    cout<<name;
    name.find(" ");  //This method will find through a string
    name.erase(0,3); //This will erase a portion if string 0 is starting index and 3 is ending index and 3 will not included
    //These were some built in functions for more follow link: www.cplusplus.com/reference/string/string/
    

}