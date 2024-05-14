#include<stdio.h>
#include<conio.h>

// C program to print the sum of odd and even numbers seperately in 1-D array

int main(){
    int i,arr[5],sum1=0,sum2=0;
    for (i=0;i<5;i++){
        printf("Enter the number: ");
        scanf("%d",&arr[i]);
    }
    for (i=0;i<5;i++){
        if (arr[i] % 2 == 0){
            sum1 = arr[i] + sum1;
        }
        else{
            sum2 = arr[i] + sum2;
        }
    }
    printf("The sum of even numbers is %d and odd numbers is %d ",sum1,sum2);
getch();
return 0;
}