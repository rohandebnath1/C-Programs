#include<stdio.h>
#include <conio.h>

// Program in C to find the biggest among the two given numbers!

int main(){
    int a,b;
    printf("Enter any two number: ");
    scanf("%d%d",&a,&b);
    if (a>b){
        printf("First number is bigger!");
    }
    else if(b>a){
        printf("Second number is bigger!");
    }
    else{
        printf("Both are equal!");
    }
    return 0;
getch();
}