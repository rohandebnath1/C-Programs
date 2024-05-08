#include<stdio.h>

// Program in C to take an array as input and print only odd numbers in it

int main(){
    int i,b[5];
    for (i=0;i<5;i++){
        printf("Enter the number: ");
        scanf("%d",&b[i]);
    }
    printf("The array with only odd numbers is as follows: ");
    for (i=0;i<5;i++){
        if(b[i] % 2 != 0){
            printf("%d \t",b[i]);
        }    
    }
return 0;
}