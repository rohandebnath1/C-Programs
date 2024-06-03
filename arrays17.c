#include<stdio.h>

// Initialiazation of 2-D Array with first bound as empty

int main(){
    int arr[][3] = {
        {1,2,3},
        {4,5,6}
    };
    printf("The first element of the 2-D Array is: %d", arr[0][0]);
return 0;
}