#include <iostream>
using namespace std;
// Overloaded constructors is a form of Compile time polymorphism
class burger{
    public:
        int burger_count;
        string burger_type;
        int burger_count2;
        string burger_type2;
        int burger_count3;
        string burger_type3;

    burger(int burger_count, string burger_type){
        this->burger_count= burger_count;
        this->burger_type= burger_type;
    }

    burger(){
        
    }

    burger(int burger_count, string burger_type, int burger_count2, string burger_type2 ){
        this->burger_count= burger_count;
        this->burger_type= burger_type;
        this->burger_count2= burger_count2;
        this->burger_type2= burger_type2;

    }

    burger(int burger_count, string burger_type, int burger_count2, string burger_type2, int burger_count3, string burger_type3 ){
        this->burger_count= burger_count;
        this->burger_type= burger_type;
        this->burger_count2= burger_count2;
        this->burger_type2= burger_type2;
        this->burger_count3= burger_count3;
        this->burger_type3= burger_type3;
    }
    
};

int main(){
    // overloaded constructors = multiple constructors with the same name but different parameters 
    //                           allow for varying arguments when instantiating(some type of declaration) an object
    burger order(2, "Chiken");
    burger order2(1, "Chiken", 2, "Beef");
    burger order3(1, "Chiken", 2, "Beef", 3, "Double Patty");
    burger order4;
    
    cout<<"count: "<<order.burger_count<<"Type: "<<order.burger_type<<endl;
    cout<<"count: "<<order.burger_count<<"Type: "<<order.burger_type<<"\n   "<<order2.burger_count2<<"  "<<order2.burger_count2<<endl;
    cout<<"count: "<<order.burger_count<<"Type: "<<order.burger_type<<"\n   "<<order2.burger_count2<<"  "<<order2.burger_count2<<"\n   "<<order2.burger_count2<<"  "<<order2.burger_count2;
}