#include <iostream>
#include <iomanip>  //It is used to control the formatting of input and output streams
//Here it is used to make precision in floating point number
using namespace std;

int amount= 70000;
int balance_to_deposit;
int withdraw_to_amount;
void balance(int amount);
void deposit(int balance_to_deposit);
void withdraw(int withdraw_amount);

int main(){
    int choice;
    
    do {
    cout<<"Banking System\n";
    cout<<"1. Show balance\n";
    cout<<"2. Amount to deposit\n";
    cout<<"3. Amount to withdraw\n";
    cout<<"Enter your choice: ";
    cin>>choice;
    switch (choice)
    {
    case 1:
        balance(amount);
        break;
    case 2:
        cout<<"Enter amount to deposit: ";
        cin>>balance_to_deposit;
        deposit(balance_to_deposit);
        break;
    case 3:
        cout<<"Enter amount to withdraw: ";
        cin>>withdraw_to_amount;
        withdraw(withdraw_to_amount);
        break;
    case 0:
        break;
    default:
        break;
    }
    
} while (choice!=0);


}

void balance(int amount){
    cout<<"Balance: "<<setprecision(2)<< fixed <<amount<<"\n";

}

void deposit(int balance_to_deposit){
    amount+=balance_to_deposit;
    cout<<balance_to_deposit<<" rupees deposited successfully\n";
    cout<<"Current balance: "<<amount<<endl;
}

void withdraw(int withdraw_amount){
    amount-=withdraw_amount;
    cout<<withdraw_amount<<" rupees withdrawn successfully\n";
    cout<<"Current balance: "<<amount<<endl;
}