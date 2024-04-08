#include<stdio.h>
#include<math.h>

int main(){
    int a,b,c;
    float d;
    printf("Enter the number to find the square and root of6: \n");     
    scanf("%d%d",&a,&b);
    c = a*a;
    d = sqrt(b);
    printf("The square of the number is: %d and the root is: %f",c,d);
    return 0;
}

