#include <stdio.h>
int Factorial_number(int a){
    int factorial=1;
    if (a==0 || a==1){
        return 1;
    }
    else{
        for(int i=1; i<=a; i++){
        factorial *=i;
    }
    printf("%d", factorial);
}
}
int main(){
    int number_to_find_factorial;
    printf("Enter a number to find factorial: ");
    scanf("%d",&number_to_find_factorial);
    Factorial_number(number_to_find_factorial);
    return 0;
}