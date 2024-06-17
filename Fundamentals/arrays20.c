#include<stdio.h>
#include<conio.h>

// To take a 2-D array as input and print sum of all elements

int main(){
    int i,j,arr[2][3];
    for (i=0;i<2;i++){
        for (j=0;j<3;j++){
            printf("Enter Value: ");
            scanf("%d",&arr[i][j]);
        }
    }
    printf("The sum of all the elements in the 2-D array is: ");

    int sum = 0;
    for (i=0;i<2;i++){
        for (j=0;j<3;j++){
            sum = sum + arr[i][j];
        }
    }
    printf("\n %d",sum);
getch();
return 0;
}