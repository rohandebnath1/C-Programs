#include<stdio.h>

// Program to convert temperature from Celcius to Fahrenheit
int main(){
    float c,f;
    printf("Enter the value in C: ");
    scanf("%f",&c);
    f = ((9*c)/5)+32;
    printf("Value of temp in F is: %.2f",f);
    return 0;
}