
#include <iostream>
using namespace std;
int main()
{
    string foods[100];
    //fill()= fills the range of elements with a specified value 
    //        fill(begin, end, value) it means fill(begining of array, end of array, value to repeat)
    fill(foods, foods+(100)/2, "Hello world"); //It will give the first half and other half will be empty
    fill(foods+(100)/2, foods + 100, "Hello world"); //It will give the other half 
    
    for(string food: foods){  
        cout<<food<<'\n';
    }
    return 0;
}