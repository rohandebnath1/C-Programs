#include <stdio.h>
#include <math.h>

int main(){
    float x,y,a;
    printf("Enter the value of base x and power y: ");
    scanf("%f%f",&x,&y);
    a = pow(x,y);
    printf("The answer %0.2f to the power %0.2f is %0.2f: ",x,y,a);
    return 0;
}