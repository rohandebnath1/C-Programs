#include<stdio.h>

// Initialisation of a 2-D array in Runtime 

int main(){
    int a[2][3],i,j;
    for (i=0;i<2;i++){
        for (j=0;j<3;j++){
            printf("Enter Values: ");
            scanf("%d",&a[i][j]);
        }
    }
return 0;
}