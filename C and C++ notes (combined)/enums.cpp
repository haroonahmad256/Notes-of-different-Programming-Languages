#include <iostream>
using namespace std;
enum day{sunday= 0, monday= 1, tuesday= 2, wednesday= 3, thursday= 4, friday= 5, saturday= 6};
int main(){
    /*
    anums(anumirations): a user defined data type that consist a paired named-integer constant.
    GREAT if you have a set of potential options. This is a modifier of switch case statements
    if we don't assign values to enums values would be assigned explicitly to each variable
    */

    //Normally we can't use strings in switch but we can do this
    day today= saturday;
    switch (today)
    {
    case monday:
        cout<<"Today is monday";
        break;

    case tuesday:
        cout<<"Today is Tuesday";
        break;
    case wednesday:
        cout<<"Today is wednesday";
        break;
    case thursday:
        cout<<"Today is Thursday";
        break;
    case friday:
        cout<<"Today is Friday";
        break;
    case saturday:
        cout<<"Today is Saturday";
        break;
    case sunday:
        cout<<"Today is Sunday";
        break;
    
    default:
        break;
    }
}