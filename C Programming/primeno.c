#include <stdio.h>

int main(){
    int a,b=0,i;
    printf("Enter any number: ");
    scanf("%d",&a);
    if (a>1){
        for (i=1;i<=a;i++){
            if(a%i==0){
                b = b + 1;
            }
            else{
                continue;
            }
        }
    }
    if(b==2){
        printf("Its a prime number!");
    }
    else{
        printf("Its not a prime number!");
    }
return 0;
}