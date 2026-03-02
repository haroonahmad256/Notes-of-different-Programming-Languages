#include <iostream>
using namespace std;
class my_info{
    public:
        string name;
        string mN;
        int age;
        int class_grade;
        string address;

    my_info(string n, string m, int a, int c, string ad){
                            //If the name of arguments my_info function is taking are same as name of variables in public 
                            //domain then we will write this-> other wise we don't need to write this
                            // This can be also done through this
        this->name= n;      //name= n;
        this->mN= m;        //mN= m;
        this->age= a;       //age= a;
        this->class_grade= c; //class_grade= c;
        this->address= ad;  // address= ad;
    }

    void profession(){
        cout<<"He is a AI student\n";
    }

    void character(){
        cout<<"His character is good\n";
    }
};

/*
A constructor is a special method or function that is automatically called when an object is instantiated (some type of declaration)
useful for assigning values to attributes (which are varibles in objects) as arguments
(within the constructor you can assign those arguments(defined in class name based function like something) 
to the attributes(variables of objects defined in public of class) of that class)
*/

int main(){
    my_info haroon("Haroon", "0324-3913749", 19, 13, "Wazir k Chattha");  // In this way we don't have to add values to attributes manually one by one
    // Here we passed arguments to class constuctors
    cout<<"Name: "<<haroon.name<<"\nMobile Number: "<<haroon.mN<<"\nClass: "<<haroon.class_grade<<"\nAge: "<<haroon.age<<"\n";
    haroon.character();
    haroon.profession();
    return 0;
}