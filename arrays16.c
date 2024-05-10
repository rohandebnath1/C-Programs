#include <stdio.h>
#include <conio.h>

//To find the prime numbers in an 1-D array

int prime(int x){
    int i,c;
    for (i=1;i<=x;i++){
        if(x % i == 0){
            c += 1;
        }
    }
return c;
}

int main(){
    int i,arr[5];
    
    for(i=0;i<5;i++){
        printf("Enter the numbers: ");
        scanf("%d",&arr[i]);
    }
    printf("The Prime numbers in the array are: \n");

    for (i=0;i<5;i++){
        if(prime(arr[i]) == 2){
            printf("%d \t",arr[i]);
        }
    }
getch();
return 0;  
}

