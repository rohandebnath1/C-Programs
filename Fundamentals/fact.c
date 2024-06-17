#include <stdio.h>
#include <conio.h>

//To enter a number it finds out the factorial of it

int main(){
    int a,i,fact;
    fact = 1;
    printf("Enter any number: ");
    scanf("%d",&a);
    for (i=1;i<=a;i++){
        fact = fact * i;
    }
printf("The factorial of the number is: %d",fact);
return 0;
getch();
}