#include<stdio.h>

// A C program to display only the even values in 1-D array entered by user

int main(){
    int i,a[5];
    for (i=0;i<5;i++){
        printf("Enter the number: ");
        scanf("%d",&a[i]);
    }
    printf("The new array with only even values: ");
    for (i=0;i<5;i++){
        if(a[i] % 2 == 0){
            printf("%d \t",a[i]);
        }
    }
return 0;
}