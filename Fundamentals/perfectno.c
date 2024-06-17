#include <stdio.h>
#include <conio.h>

// to check if a number is perfect number or not

int main(){
    int a,b,sum=0,num,i;
    printf("Enter a number: ");
    scanf("%d",&num);
    for (i=1;i<num;i++){
        if ((num % i ==0)){
            sum = sum + i;
        }
    }
    if (sum == num){
        printf("Its a perfect number!");
    }
    else{
        printf("Its not a perfect number!");
    }
return 0;
getch();
}