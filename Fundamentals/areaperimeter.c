#include<stdio.h>
#include<conio.h>

//To calculate and display the area and perimeter of a circle, square and rectangle

int main(){
    float rad,side,len,br;
    float pcir,acir,asq,psq,arec,prec;
    int ch;
    float pi = 3.141;
    printf("Enter choice to find Area/Perimeter of: \n 1.Circle \n 2.Square \n 3.Rectangle : ");
    scanf("%d",&ch);
    switch(ch){
        case 1 : printf("Enter radius of circle: ");
                 scanf ("%f",&rad);
                 pcir = 2 * pi * rad;
                 acir = pi * rad * rad;
                 printf("The circumference is %.2f and area is %.2f ",pcir,acir);
                 break;
        case 2 : printf("Enter side of square: ");
                 scanf("%f",&side);
                 psq = 4 * side;
                 asq = side * side;
                 printf("The perimeter is %.2f and area is %.2f ",psq,asq);
                 break;
        case 3 : printf("Enter length and breadth of rectangle: ");
                 scanf("%f%f",&len,&br);
                 prec = 2 * (len + br);
                 arec = len * br;
                 printf("The perimeter is %.2f and area is %.2f ",prec,arec);
                 break;
        default: printf("Enter correct choice!!");
    }
getch();
return 0;
}