#include<stdio.h>
#include<conio.h>

// Printing the following pattern
// *
// ***
// *****

int main(){
    int i,j;
    for (i=1;i<=3;i++){
        for (j=1;j<=(2*i)-1;j++){
            printf("*");
        }
    printf("\n");
    }
return 0;
getch();
}