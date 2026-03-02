#include <stdio.h>
void slice(char arr[]);
void vowels_occurence(char is_vowel[]);
int main(){
    //we will discuss about strings
    //The array will is terminated with a null character(\0) is called called string
    //by using \0 c compiler take other alphabets of array as a word or sentence just like that
    // char first_string[]= {'h','a','r','o','o','n','\0'};
    // for (int i = 0; first_string[i] != '\0'; i++)
    // {
    //     printf("%c", first_string[i]);
    // }

    char string[]= "Haroon Ahmad";
    // slice(string);
    vowels_occurence(string);


    
    return 0;
}

void vowels_occurence(char is_vowel[]){
    int count=0;
    int count2=0;
    int count3=0;
    for (int i = 0; is_vowel[i]!='\0'; i++)
    {
        if (is_vowel[i]=='a'|| is_vowel[i]=='e'|| is_vowel[i]=='i'|| is_vowel[i]=='o'|| is_vowel[i]=='u')
        {
            count++;
        }
        else if(is_vowel[i]==' ')
        {
            count2++;
        }
        else
        {
            count3++;
        }
        
        

        
    }
    printf("Total number of vowels in string are %d\n", count);
    printf("Total number of spaces in string are %d\n", count2);
    printf("Total number of consonants in string are %d\n", count3);
    
}

void slice(char arr[]){
    int n, m;
    printf("Enter n: ");
    scanf("%d", &n);
    printf("Enter m: ");
    scanf("%d", &m);
    for (int i = n; i <=m; i++)
    {
        printf("%c", arr[i]);
    }

}