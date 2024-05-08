#include <stdio.h>

// To print all the numbers of a given integer

int main(){
    int a,b,num;
    printf("Enter any integer: ");
    scanf("%d",&num);
    while(num>0){
        b = num % 10;
        printf("One of the digit is: %d \n",b);
        num = num / 10;
    }
return 0;
}