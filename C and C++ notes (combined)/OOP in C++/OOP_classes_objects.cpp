#include <iostream>
using namespace std;
class country{
    public:  // public access modifier, it is used for making variables pulicily accessible
             // The variables inside it called are called public attributes
        string name; // These are attributes which are characteristices of objects
        string capital; //attribute
        string forfamous;   //attribute

        void condition(){ // These are the methods in form of functions which we can apply on objects
            cout<<"The country is currently suffering\n";
        }
        void beauty(){
            cout<<"But the country is beautiful\n";
        }
        void history(){
            cout<<"The country have a rich history\n";
        }
};
int main(){
    /*
    Objects: A collection of attributes and methods 
    They have characteristic and perform actions
    can be used to mimic real world items (ex. Phone, Book, Dog)
    created from a class which acts as a blueprint. It is a bit similar to struct
    */

    country pakistan;
    pakistan.name= "Pakistan";
    pakistan.capital= "islamabad";
    pakistan.forfamous= "Northern Areas";
    cout<<pakistan.name<<" "<<pakistan.capital<<" "<<pakistan.forfamous<<endl;
    pakistan.beauty();
    pakistan.condition();
    pakistan.history();
    return 0;
}