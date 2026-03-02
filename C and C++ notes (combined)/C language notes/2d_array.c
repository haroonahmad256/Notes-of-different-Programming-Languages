#include <stdio.h>
int main(){

    int Mul_arr[3][10];
    int Mul_num[3]= {4,8,10};
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            Mul_arr[i][j]= Mul_num[i]* (j+1);
        }
        
    }
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            printf("%d X %d = %d\n\n",Mul_num[i], (j+1), Mul_arr[i][j]);

        }
        
    }
    
}