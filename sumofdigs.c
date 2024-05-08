#include <stdio.h>

// To print the sum of digits of a number

int main(){
    int num,a,sum=0;
    printf("Enter an integer: ");
    scanf("%d",&num);
    while(num!=0){
        a = num % 10;
        sum = sum + a;
        num = num / 10;
    }
printf("The sum of digits are: %d",sum);
return 0;
}