#include <stdio.h>
struct cars_owners
{
    char owner_1[10];
    char owner_2[10];
    char owner_3[10];
    char car_1[10];
    char car_2[10];
    char car_3[10];
};
 
int main(){
    struct cars_owners cars_all= {"Jhon", "Wick", "Edward", "BMW", "Audi", "Toyota"};
    struct cars_owners cars_all2;
    cars_all2= cars_all;
    printf("%s is the owner of %s.\n", cars_all.owner_1, cars_all.car_1);
    printf("%s is the owner of %s.\n", cars_all.owner_2, cars_all.car_2);
    printf("%s is the owner of %s.\n", cars_all.owner_3, cars_all.car_3);
    printf("%s is the owner of %s.\n", cars_all2.owner_1, cars_all2.car_1);
    printf("%s is the owner of %s.\n", cars_all2.owner_2, cars_all2.car_2);
    printf("%s is the owner of %s.", cars_all2.owner_3, cars_all2.car_3);
    return 0;
}
 