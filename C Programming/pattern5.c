#include <stdio.h>

// For printing the followinf pattern
//      *     
//     ***    
//    *****   

int main(){
    int i,j,k,l;
    for (i=1;i<=4;i++){
        for (j=5;j>=i;j--){
            printf(" ");
        }
        for (k=1;k<=(2*i)-1;k++){
            printf("*");
        }
        for (l=5;l>=i;l--){
            printf(" ");
        }
    printf("\n");
    }
return 0;
}
