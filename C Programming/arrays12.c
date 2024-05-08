#include <stdio.h>
#include<conio.h>

// A simple c program to find equal adjacent values in an array!

int main(){
    int i, arr[5],temp = 0;
    for (i=0;i<5;i++){
        printf("Enter a digit: ");
        scanf("%d",&arr[i]);
    }
    for (i=0;i<5;i++){
        if ((arr[i]) == (arr[i+1])){
            temp = 1;
        }
    }
    if (temp == 1){
        printf("Two adjacent equal values found!");
    }
    else{
        printf("No adjacent equal values found!!");
    }
getch();
return 0;
}
