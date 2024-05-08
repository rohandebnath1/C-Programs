#include<stdio.h>

// WAP to input a number and check whether it is odd or even. 
// If it is odd then add any even number to it,
// if it is even then add any odd number to it and display the final number.

int main(){
    int a,b,c;
    printf("Enter any number: ");
    scanf("%d",&a);
    if (a%2==0){
        printf("The entered number is even! \n");
        printf("Enter any odd number now!");
        scanf("%d",&b);
        if (b%2!=0){
            c = a+b;
            printf("The new number is: %d",c);
        }
        else{
            printf("You did not enter an odd number!!");
        }
    }
    else{
        printf("The entered number is odd! \n");
        printf("Enter an even number: ");
        scanf("%d",&b);
        if (b%2 ==0){
            c = a+b;
            printf("The new number is: %d",c);
        }
        else{
            printf("You didnt enter an even number!!");
        }
    }
return 0;
}


