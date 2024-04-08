#include<stdio.h>
#include<math.h>

int main(){
    float s,a,b,c,ar;
    printf("Enter the three sides of triangles as A B and C values: ");
    scanf("%f%f%f",&a,&b,&c);
    s = (a+b+c)/2;
    ar = sqrt(s*(s-a)*(s-b)*(s-c));
    printf("The area of triangle using herons formula is: %0.2f",ar);
    return 0;
}

