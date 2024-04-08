#include<stdio.h>

int main(){
    float pi = 3.14159;
    float rad,side,length,breadth;
    int ch;
    float acir,pcir,asq,psq,arec,prec;
    printf("Enter the choice between 1, 2 or 3 - \n 1.Area Perimeter of Circle \n 2.Area Perimeter of Square \n 3.Area Perimeter of Rectangle ");
    scanf("%d",&ch);
    switch(ch){
        case 1: printf("Enter the radius of the circle: ");
                scanf("%f",&rad);
                acir = pi * rad * rad;
                pcir = 2 * pi * rad;
                printf("The area of the circle is %.2f and the perimeter is %.2f ",acir,pcir);
                break;
        case 2: printf("Enter the side of the square: ");
                scanf("%f",&side);
                asq = side * side;
                psq = 4 * side;
                printf("The area of the square is %.2f and the perimeter is %.2f ",asq,psq);
                break;
        case 3: printf("Enter the length and breadth of the rectangle: ");
                scanf("%f%f",&length,&breadth);
                arec = length * breadth;
                prec = 2*(length + breadth);
                printf("The area of the square is %0.2f and the perimeter is %0.2f",arec,prec);
                break;
        default: printf("Selected wrong choice!");
    }
return 0;

}