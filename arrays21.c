#include<stdio.h>
#include<conio.h>

// Takihng input in a 2-D array and then printing the sum of corner elements

int main(){
    int i,j,arr[3][3],sum=0;
    for (i=0;i<3;i++){
        for (j=0;j<3;j++){
            printf("Enter Value: ");
            scanf("%d",&arr[i][j]);
        }
    }
    printf("The sum of all elements in the corner is: ");

    for (i=0;i<3;i++){
        for (j=0;j<3;j++){
            if ((i==0 && j==0) || (i==0 && j == 2) || (i==2 && j==0) || (i==2 && j==2)){
                sum = sum + arr[i][j];
            }
        }
    }
    printf("\n %d",sum);

getch();
return 0;
}