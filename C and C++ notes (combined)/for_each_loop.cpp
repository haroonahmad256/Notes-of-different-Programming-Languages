#include <iostream>
using namespace std;
int main(){
    // for each loop: loop that eases the traversal over an iterable data set
    // in simple loop we can iterate forward, backward and can also skip some iteration
    // in for each loop we go from start to end
    string students[]= {"Haroon", "Ahsan", "Daniyal"};
//for((data type of array through which we are iterating) name for current element : name of array through which to iterate)
    for (string student : students) 
    {
        cout<< student <<'\n';       // cout<< name of current element
    }
    

}