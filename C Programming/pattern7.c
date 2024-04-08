#include<stdio.h>

// For printing the following pattern
//      1     
//     101
//    10101
//   1010101

int main(){
    int i,j,k,l;
    for (i=1;i<=4;i++){
        for (j=5;j>=i;j--){
            printf(" ");
        }
        for (k=1;k<=(2*i)-1;k++){
            if(k%2 != 0){
                printf("1");
            }
            else{
                printf("0");
            }
        }
        for (l=5;l>=i;l--){
            printf(" ");
        }
    printf("\n");
    }
return 0;
}