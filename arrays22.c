#include<stdio.h>
#include<conio.h>

int main(){
    int i, j, arr[3][3],sum=0;;
    for (i=0;i<3;i++){
        for (j=0;j<3;j++){
            printf("Enter Value: ");
            scanf("%d",&arr[i][j]);
        }
    }
    printf("The sum of diagonal elements are: ");

    for (i=0;i<3;i++){
        for (j=0;j<3;j++){
            if((i==j) || (i+j ==2)){
                sum = sum + arr[i][j];
            }
        }
    }
    sum = sum + arr[1][1]; //The centre element gets counted only once
    printf("\n %d",sum);

getch();
return 0;
}