#include <stdio.h>

// For printing the following pattern
//  ***** 
//   *** 
//    *

int main(){
    int i,j,k,l;
    for (i=1;i<=3;i++){
        for (j=1;j<=i;j++){
            printf(" ");
        }
        for (k=5;k>=(2*i)-1;k--){
            printf("*");
        }
        for (l=1;l<=i;l++){
            printf(" ");
        }
        printf("\n");
    }
return 0;
}