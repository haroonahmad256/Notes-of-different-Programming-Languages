#include <stdio.h>
#include <string.h>
int main(){

    int num;
    printf("Enter a number: ");
    scanf("%d",&num);
    int i=0;
    printf("Natural numbers: ");
    while(i<=num){ // Loop will run untill i which is zero is less than or equal to input number
        printf("%d\n",i);
        i++; // Update i and add 1 into it every time loop runs
    }

    int num1;
    printf("Enter a number: ");
    scanf("%d",&num1);
    int k=0;
    printf("Whole numbers: ");
    do   // Do while loop always executes atleast one time
    {        
        printf("%d\n", k);
        k++;

    }while(k<=num);

    int num2;
    printf("Enter a number: ");
    scanf("%d",&num2);
    int i2=1;
    while(i2<=10){   // Table of input number will be printed with help of while loop
        printf("%d x %d= %d\n",num2,i2,(num2*i2));
        i2++;

    }
    int i3=10;
    while(i3>0){    // This is also printing table but in reverse direction 
        printf("%d x %d= %d\n",num2,i3,(num2*i3));
        i3--;
    }    

}
