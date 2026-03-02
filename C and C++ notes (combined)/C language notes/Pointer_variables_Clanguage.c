#include <stdio.h>
int main(){
    


    int b= 45;
    printf("The address of b is %p\n", &b);

    int* k= &b;
    printf("The address of b: %p\n", k);


    printf("The value of b at address k is %d\n", *k);


    printf("The address of k is %p\n", &k);


    printf("The value k is %p\n", *(&k)); 
    // K is a pointer variable which store the address of b. But k has also a memory address 
    // Usually when we do *(&b) it will first identify the memory address of b using & and then check value of b using *
    // But in case of k the value of k is memory address of b so when we do *(&k) it will give memory address of b as it's value
    // so value of k is address of b
    int **j = &k;
    printf("The value of address k is %p", j);
    return 0;
}