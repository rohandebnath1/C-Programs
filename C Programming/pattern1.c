#include <stdio.h>

// A simple pattern using for loop   
//*
//**
//***
//****
//***** 
int main(){
    int i,j;
    for (i=1;i<=5;i++){
        for (j=1;j<=i;j++){
            printf("*");
        }
        printf("\n");
    }
return 0;
}