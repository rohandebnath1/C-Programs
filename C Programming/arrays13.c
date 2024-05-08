#include <stdio.h>

// A simple c program to calculate the size of the array using SizeOf

int main(){
    int i,n;
    printf("Enter the number of elements in the array: ");
    scanf("%d",&n);
    int arr[n];
    for (i=0;i<n;i++){
        printf("Enter element: ");
        scanf("%d",&arr[i]);
    }
    int sizr = sizeof(arr)/4;
    printf("The size of the array is: %d",sizr);
return 0;
}