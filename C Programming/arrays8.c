#include<stdio.h>

// A C program to replace the numbers by 0 and 1 if index if even and odd respectively

int main(){
    int i,arr[5];
    for (i=0;i<5;i++){
        printf("Enter the number: ");
        scanf("%d",&arr[i]);
    }
    for (i=0;i<5;i++){
        if(i % 2 != 0){
            arr[i] = 1;
        }
        else{
            arr[i] = 0;
        }
        printf("The new array would be: \n");
        printf("%d \t",arr[i]);
    }
    
return 0;
}