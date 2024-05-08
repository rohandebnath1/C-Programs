#include<stdio.h>

int main(){
    char str[5],i;
    for (i=0;i<5;i++){
        printf("Enter any charcater: ");
        scanf("%s",&str[i]);
    }
    for (i=0;i<5;i++){
        printf("%s",str[i]);
    }

return 0;
}