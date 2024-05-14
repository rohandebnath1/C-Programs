#include <stdio.h>
#include<conio.h>

// C Program to enter n number of terms in an 1-D Array and print it

int main(){
    int i,n;
    printf("Enter the number of terms: ");
    scanf("%d",&n);
    int arr[n];
    for (i=0;i<n;i++){
        printf("Enter Number: ");
        scanf("%d",&arr[i]);
    }

    for (i=0;i<n;i++){
        printf("%d \t",arr[i]);
    }
getch();
return 0;
}