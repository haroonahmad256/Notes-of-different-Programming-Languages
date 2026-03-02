#include <iostream>
#include <cmath>
using namespace std;
int main(){
    int x =5.345;
    int y= 9;
    int z1= max(x,y);  //THis will give maximum between two numbers or more
    int z2= min(x,y);  //THis will give minimum between two numbers or more
    cout<<z1<<" "<<z2;
    int z3= pow(x,y); //y is the power of x
    int z4= sqrt(16); //This will give square root of x
    int z5= abs(-3); //This will give absolute value 
    cout<<z3<<" "<<z4;
    int z5= round(x);
    int z6 = ceil(x);
    int z7= floor(x);
    cout<<z5<<" "<<z6<<" "<<z7;
    //Go to www.cplusplus.com/reference/cmath/ for more math functions

}