#include <stdio.h>
#include <conio.h>

// A pattern to print the heart symbol <3

int main(){
    int i,j,k,l,m,n,p,x,y,z;
    for (i=1;i<=5;i++){
        for (j=4;j>=i;j--){
            printf(" ");
        }
        for (k=1;k<=i;k++){
            printf("* ");
        }
        for (m=4;m>=i;m--){
            printf(" ");
        }
        for (p=4;p>=i;p--){
            printf(" ");
        }
        for (n=1;n<=i;n++){
            printf("* ");
        }
    printf("\n");
    }

    for (x=1;x<=11;x++){
        for (y=1;y<=x;y++){
            printf(" ");
        }
        for (z=9;z>=x;z--){
            printf("* ");
        }
    printf("\n");
    }
    

return 0;
getch(); 
}