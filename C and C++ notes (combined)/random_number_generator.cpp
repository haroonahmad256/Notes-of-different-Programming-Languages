#include <iostream>
using namespace std;             
int main(){
    //pseduo random= Not truly random but close
    srand(time(NULL));
    int num= rand();  //Using rand function we can generate random number 
    int num2= (rand()%20)+1; //This will give random number between 0 and 20
    int num3= (rand()%6)+1; //If we are making a roll dice game then we would like to generate random number between 1 and 6
    //If we have to roll 3 dices at same time then
    cout<<"First dice: ";
    int num4= (rand()%6)+1;
    cout<<"Second dice: ";
    int num5= (rand()%6)+1;
    cout<<"Third dice: ";
    int num6= (rand()%6)+1;

    cout<<num;
}