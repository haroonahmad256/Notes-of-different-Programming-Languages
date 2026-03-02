#include <iostream>
using namespace std;
int main(){
    int num;
    int tries;
    srand(time(NULL));
    int random_number= (rand()%100)+1;
    do
    {
        cout<<"Gues a number between 1 and 100: ";
        cin>>num;
        tries++;
        if (num>random_number)
        {
            cout<<"Lower the number\n";
        }
        if (num<random_number)
        {
            cout<<"Higher the number\n";
        }
        if (num==random_number)
        {
            cout<<"Correct you guessed the number in "<<tries<<" tries\n";
        }
        
        
    } while (num!=random_number);
    
    
}