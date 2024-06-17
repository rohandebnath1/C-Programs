#include<stdio.h>
#include<math.h>
#include<conio.h>

int main(){
    int a,b,num,sum=0,temp,c=0;
    printf("Enter any number: ");
    scanf("%d",&num);
    temp = num;
    while(temp!=0){
        temp = temp / 10;
        c++;
    }
    temp = num;
    printf("Number of digits in you number: %d \n",c);
    while (temp != 0){
        a = temp % 10; //3,5,1 
        b = ceil(pow(a,c)); //27,125,1
        temp = temp / 10; //15,1,0
        sum = sum + b;//27,152,153
    }
    if (sum==num){
        printf("Its an Armstrong Number");
    }
    else{
        printf("Its not an Armstrong number");
    }
getch();
return 0;
}
