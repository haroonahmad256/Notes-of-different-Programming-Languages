#include <stdio.h>
int main()
{
    FILE *fptr; // This is a pointer which is pointing to the structre of file
    // Reading a file
    char ch; //variable to store characters as we read in file
    fptr = fopen("Test.txt", "r"); //fopen("file name", "mode of opening file") fopen opens the file
    if (fptr == NULL) //fptr returns NULL if file doesn't exist
    {
        printf("doesn't exist!\n");
    }
    else
    {

        fscanf(fptr, "%c", &ch); //Structure: filescanf(filepointer name, format 
        //specifier, the vairable in which we want to store the readed file or data) 
        //simple scanf function which read the data we input just like fscanf reads the data in file



        printf("character in file is : %c\n", ch); 
        fscanf(fptr, "%c", &ch);
        printf("character in file is : %c\n", ch);
        fclose(fptr);

    }
    // Writing in a file
    ch = 'M';
    fptr = fopen("NewFile.txt", "w");

    fprintf(fptr, "%cANGO", ch);
    fclose(fptr);
    // fgets
    fptr = fopen("NewFile.txt", "r");
    printf("character in file is : %c\n", fgetc(fptr));
    printf("character in file is : %c\n", fgetc(fptr));
    printf("character in file is : %c\n", fgetc(fptr));
    printf("character in file is : %c\n", fgetc(fptr));
    printf("character in file is : %c\n", fgetc(fptr));
    fclose(fptr);
    // fputc
    fptr = fopen("NewFile.txt", "w");
    fputc('a', fptr);
    fputc('p', fptr);
    fputc('p', fptr);
    fputc('l', fptr);
    fputc('e', fptr);
    fclose(fptr);
    // read the full file (EOF)
    fptr = fopen("NewFile.txt", "r");
    ch = fgetc(fptr);
    while (ch != EOF)
    {
        printf("%c", ch);
        ch = fgetc(fptr);
    }
    printf("\n");
    fclose(fptr);
    return 0;
}