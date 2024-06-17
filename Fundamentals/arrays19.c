#include<stdio.h>
#include<conio.h>

// Taking input of values in 2-D Array and printing values

int main(){
    int arr[2][3],i,j;
    for (i=0;i<2;i++){
        for (j=0;j<3;j++){
            printf("Enter Value: ");
            scanf("%d",&arr[i][j]);
        }
    }
    printf("The values in 2-D array is as follows: ");

    for (i=0;i<2;i++){
        for (j=0;j<3;j++){
            printf("%d",arr[i][j]);
        }
    }
getch();
return 0;
}