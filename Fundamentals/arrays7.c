#include<stdio.h>
#include<conio.h>

// A program in C to print only the numbers in 1-D Array divisible by 3 or 7

int main(){
    int i,arr[5];
    for (i=0;i<5;i++){
        printf("Enter the number: ");
        scanf("%d",&arr[i]);
    }
    printf("Numbers divisible only by 3 or 7 are as follows: ");
    for (i=0;i<5;i++){
        if ((arr[i] % 3 == 0) | (arr[i] % 7 == 0)){
            printf("%d \t",arr[i]);
        }
    }
getch();
return 0;
}