#include <stdio.h>

// Program to find the number of digits in a number

int main(){
    int num,c=0,temp;
    printf("Enter a number: ");
    scanf("%d",&num);
    temp = num;
    while (temp != 0){
        temp = temp / 10;
        c++;
    }
printf("The total number of digits are: %d",c);
return 0;
}