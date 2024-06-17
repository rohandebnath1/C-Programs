#include<stdio.h>
#include<conio.h>

// Linear Search Algo in 1-D array

int main(){
    int i, arr[5],num;
    printf("Enter the number to search in array: ");
    scanf("%d",&num);
    
    for(i=0;i<5;i++){
        printf("Enter Number: ");
        scanf("%d",&arr[i]);
    }

    for(i=0;i<5;i++){
        if(num == arr[i]){
            break;
        }
    }
    if(i == 5){
        printf("No Match Found!!");
    }
    else{
        printf("Match Found! At index number: %d",i);
    }
getch();
return 0;
}