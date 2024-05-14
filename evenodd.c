#include<stdio.h>
#include<conio.h>

//Program to find a number is odd or even using if else

int main(){
    int num;
    printf("Enter a number to check even or odd: ");
    scanf("%d",&num);
    if (num%2 == 0){
        printf("%d is even", num);
    }
    else{
        printf("%d is odd", num);
    }
    return 0;
getch();
}


