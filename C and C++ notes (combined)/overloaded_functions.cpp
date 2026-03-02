#include <iostream> 
using namespace std;
void friend_zone();
void friend_zone(string friend1, string friend2);
void friend_zone(string friend1, string friend2, string friend3);
int main(){
    friend_zone("Sahil", "Adan");
}
void friend_zone(){
    cout<<"Ahsan, Bilal, Daniyal, Husnain";
}
void friend_zone(string friend1, string friend2){
    cout<<"Ahsan, Bilal, Daniyal, Husnain"<<friend1<<" "<<friend2;
    
}
void friend_zone(string friend1, string friend2, string friend3){
    cout<<"Ahsan, Bilal, Daniyal, Husnain"<<friend1<<" "<<friend2<<" "<<friend3;

}
//These are overloaded functions functions can share the same name but different parameters
//Functions name and its parameters are called function signature and function signature needs to be unique