#include<stdio.h>
#include<conio.h>

// To print the sum of the numbers in the 1-D array entered by user

int main(){
    int i,arr[5],sum=0;
    for (i=0;i<5;i++){
        printf("Enter Number: ");
        scanf("%d",&arr[i]);
    }
    for (i=0;i<5;i++){
        sum = arr[i] + sum;
    }
    printf("The sum of the numbers in the array is: %d",sum);
getch();
return 0;
}