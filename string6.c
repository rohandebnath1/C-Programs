#include<stdio.h>
#include<conio.h>
#include<string.h>


// Concatenation of two strings

int main(){
    char s1[20] = "Rohan ";
    char s2[10] = "Debnath";
    strcat(s1,s2);
    printf("Full name is %s",s1);

getch();
return 0;    
}