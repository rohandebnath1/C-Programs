#include<stdio.h>

// Printing numbers starting from an user given point

int main(){
    int i,num;
    printf("Enter any number between 1-50: ");
    scanf("%d",&num);
    if (num<50){
        for (i=num;i<=50;i++){
            printf("%d \n",i);
        }
    }
    else{
        printf("Enter number between 1 - 50!! ");
    }
return 0;
}