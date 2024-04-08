#include <stdio.h>

// WAP to input 3 angles of a triangle and check whether it is 
// possible to form a triangle or not. If possible, then 
// determine whether it is acute angled or obtuse angled or right angled triangle.

int main(){
    float a,b,c;
    printf("Enter the three angles of the triangle one by one: ");
    scanf("%f%f%f",&a,&b,&c);
    if ((a+b+c) == 180){
        printf("Triangle is possible! \n");
        if((a==90) | (b==90) | (c==90)){
            printf("The triangle is right angled!");
        }
        else if ((a>90) | (b>90) | (c>90)){
            printf("The triangle is obtuse angled!");
        }
        else{
            printf("The triangle is acute angled!");
        }
    }
    else{
        printf("Triangle is not possible!");
    }
return 0;
}