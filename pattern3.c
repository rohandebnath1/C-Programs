#include <stdio.h>
#include <conio.h>

// Printing this following pattern 
//      *
//     **
//    ***
//   ****
//  *****
// ******

int main(){
    int i,j,k;
    for (i=1;i<=6;i++){
        for (j=5;j>=i;j--){
            printf(" ");
        }
        for (k=1;k<=i;k++){
            printf("*");
        }
    printf("\n");
    }
return 0;
getch();
}