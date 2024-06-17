#include<stdio.h>

// WAP (menu driven) to interchange (swap) the values of 2 variables 
// i) using 3rd variable ii) without using 3rd variable.

int main(){
    int a,b,c,ch;
    printf("Enter your choice to swap from the following: \n 1.using 3rd variable.\n 2.Without using 3rd variable.");
    scanf("%d",&ch);
    switch(ch){
        case 1: printf("Enter 1st and 2nd variable one after one: ");
                scanf("%d%d",&a,&b);
                c = a;
                a = b;
                b = c;
                printf("Now the 1st value is %d and the 2nd value is %d ",a,b);
                break;
        
        case 2: printf("Enter 1st and 2nd variable one after one: ");
                scanf("%d%d",&a,&b);
                a = a + b;
                b = a - b;
                a = a - b;
                printf("Now the 1st value is %d and the 2nd value is %d ",a,b);
                break;
        
        default: printf("Incorrect choice given!!");
    }
return 0;
}