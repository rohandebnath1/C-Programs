#include <stdio.h>
#include <conio.h>

int main(){
    int y;
    printf("Enter a year: ");
    scanf("%d",&y);
    if ((y%4 == 0) & (y%400 == 0) | (y%100 != 0)){
        printf("Its a leap year!");
    }
    else{
        printf("Not a leap year!");
    }
return 0;
getch();
}