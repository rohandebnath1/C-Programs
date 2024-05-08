#include <stdio.h>

// A simple program to take input an array of size 5 and print the array

int main(){
    int i, b[5];
    for (i=0;i<5;i++){
        printf("Enter the number: ");
        scanf("%d",&b[i]);
    }
    printf("The array is as follows: ");
    for (i=0;i<5;i++){
        printf("%d \t",b[i]);
    }
return 0;
}