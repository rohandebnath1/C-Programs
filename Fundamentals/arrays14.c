#include <stdio.h>
#include <conio.h>

// A C program to check whether a value is repeated in a 1-D Array

int main(){
    int i,arr[6],n,temp = 0;
    for (i=0;i<6;i++){
        printf("Enter value: ");
        scanf("%d",&arr[i]);
    }
    
    for (i=1;i<6;i++){
        n = arr[0];
        if (n == arr[i]){
            temp = 1;
        }
        else{
            n = n + 1;
        }
    }
    if (temp == 1){
        printf("Match Found! at index");
    }
    else{
        printf("No Match Found!!");
    }
getch();
return 0;

}