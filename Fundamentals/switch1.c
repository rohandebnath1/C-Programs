#include<stdio.h>

// First program related to Switch statement

int main(){
    int x = 5; 
    switch(x){
        case 1: printf("Hello World");
        break;
        case 2: printf("How are you?");
        break;
        case 5: printf("Yes it works!"); //The given val of x matches with the case
        break;
        default: printf("Just the default statement.."); //If none matches 
    }
    return 0;
}