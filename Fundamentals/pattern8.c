#include<stdio.h>

// For printing the following pattern
// 1
// 23
// 456
// 78910

int main(){
    int i,j,c=0;
    for (i=1;i<=4;i++){
        for (j=1;j<=i;j++){
            c = c + 1;
            printf("%d",c);
        }
    printf("\n");
    }
return 0;
}