#include<stdio.h>
#include<conio.h>
#include<string.h>

// Concatenating two strings without strcat

int main(){
    char s1[20] = "Hello ";
    char s2[10] = "World";
    int len1 = strlen(s1); //7
    int len2 = strlen(s2); //6
    
    for (int i=0;i<=len2;i++){
        s1[len1 + i] = s2[i]; 
    }
    printf("%s ",s1);

getch();
return 0;
}