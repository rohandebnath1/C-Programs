#include<stdio.h>

// A C Program to reverse the contents of an array

int main(){
    int i,arr[5],c=0;
    for(i=0;i<5;i++){
        printf("Enter the Number: ");
        scanf("%d",&arr[i]);
    }
    printf("The reversed array is as follows: ")
    for(i=4;i>-1;i--){
        printf("%d \t",arr[i]);
    }
return 0;
}