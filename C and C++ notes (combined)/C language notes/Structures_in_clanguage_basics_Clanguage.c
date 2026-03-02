#include <stdio.h>
#include <string.h>
struct fitness     //Structures in C language these are used to organize data and avoid complexity
{
    int age;               
    char gender[10];
    float height;               //it is a data type which stores different types of data like integer, float, and charactar.
    int weight;
};

int main(){
    struct fitness l;
    printf("Enter your age: ");
    scanf("%d", &l.age);
    printf("%d", l.age);
    printf("\nEnter your gender(M/F): ");
    scanf("%c", &l.gender);
    strcpy(l.gender, "M");
    printf("%s", l.gender);
    printf("\nEnter your height: ");
    scanf("%f", &l.height);
    printf("%f", l.height);
    printf("\nEnter your weight: ");
    scanf("%c", &l.weight);
    printf("%d", l.weight);
    return 0;

}