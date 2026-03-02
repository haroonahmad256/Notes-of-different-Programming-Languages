#include <stdio.h>
#include <string.h>
void To_greet(char greet[])
{
    printf("Good %s\n", greet);
}
int main()
{
    To_greet("Morning");
    To_greet("Afternoon");
    To_greet("Evening");
    int i=10;
    while(i>0){
        printf("%d", i);
    }

    return 0;
}

