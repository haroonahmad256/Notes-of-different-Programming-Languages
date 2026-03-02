#include <stdio.h>
struct represent
{
    int n;
};

int main(){

    struct represent problem;
    struct represent *ptr= &problem.n;
    

    printf("The value is %p", ptr);

    
    return 0;
}