#include <stdio.h>

// WAP to input 3 sides of a triangle and check whether it is possible 
// to form a triangle or not. If possible, then determine 
// whether it is an equilateral or an isosceles or a scalene triangle.

int main(){
    float a,b,c;
    printf("Enter the three sides of the triangle one by one: ");
    scanf("%f%f%f",&a,&b,&c);
    if ((a+b)>c && (a+c)>b && (b+c)>a){
        printf("Triangle is possible! \n");
        if ((a==b) && (b==c)){
            printf("The triangle is an equilateral triangle!");
        }
        else if ((a==b) | (b==c) | (c==a)){
            printf("The triangle is an isosceles triangle!");
        }
        else{
            printf("The triangle is a scalene triangle!");
        }
    }
    else{
        printf("Triangle is not possible!!");

    }
return 0;
}