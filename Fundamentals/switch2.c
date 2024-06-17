#include <stdio.h>

int main(){
    int x =10,y=5,z=0,ch;
    printf("Enter the choice between 2 3 or 4: ");
    scanf("%d",&ch);
    switch (ch){
        case 2: x++; //x increments to 11
                y = x++; //y is 11 as of x, then x increments to 12
                break;
        case 3: y = --x; //x becomes 9, y is assigned the value of x = 9
                z = ++y; //y becomes 10, z is assigned the value of y = 10 
        case 4: y++; //y increments to 11
                z = y; //z is assigned the value of y= 11
                x = ++z; //z becomes 12, x is assigned value of z = 12
                break; //so x = 12,y = 11,z = 12
        default: printf("Wrong Choice");
    }
    printf("%d \n",x);
    printf("%d \n",y);
    printf("%d \n",z);
    return 0;
}