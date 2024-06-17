#include <stdio.h>

int Factorial(int);

int main(){
    int num,result;
    scanf("%d",&num);
    result = Factorial(num);
    printf("Factorial of %d is %d",num,result);

return 0;
}

int Factorial(int x){
    if (x == 0 || x == 1){
        return 1;
    }
    else{
        return (x * Factorial(x-1));
    }
}