#include <iostream>
using namespace std;
struct Mine
{
    string name;
    int age;
    char gender;
    string role;
    string currentaddress;
};

int main(){
    /*
    Struct: A structre which group related variables under one name structs can contain many different 
    data types (String, integers, double, bool, etc ) variables in a struct are known as members 
    members can access with .
    it is like a data type which stores other different data type variables
    */
   Mine information;
   information.name= "Haroon";
   information.age= 18;
   information.currentaddress= "Gujranwala";
   information.role= "Student";
   cout<<information.name<<endl;
   cout<<information.age<<endl;
   cout<<information.currentaddress<<endl;
   cout<<information.role<<endl;
    cout<<"\n";

   Mine Him;
   Him.name= "Ahsan";
   Him.age= 18;
   Him.currentaddress= "Gujranwala";
   Him.role= "StudentBBA";
   cout<<Him.name<<endl;
   cout<<Him.age<<endl;
   cout<<Him.currentaddress<<endl;
   cout<<Him.role<<endl;

}