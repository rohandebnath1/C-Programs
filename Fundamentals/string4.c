#include<stdio.h>
#include<conio.h>

// Reading string using gets function

int main(){
    char name[15];
    printf("Enter Name: ");
    gets(name);
    printf("Your name is: %s",name);

getch();
return 0;
}