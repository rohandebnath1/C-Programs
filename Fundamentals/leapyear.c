#include <stdio.h>
#include <conio.h>

// to check if a year is leap year or not

int main(){
    int y;
    printf("Enter a year: ");
    scanf("%d",&y);

    if (y%400 == 0){
        if (y%4 == 0){
            if (y%4 == 0){
                printf("Leap Year!");
            }
            else{
                printf("Not leap year!");
            }
        
        }
        printf("Leap year");
    }
return 0;
getch();
}
        