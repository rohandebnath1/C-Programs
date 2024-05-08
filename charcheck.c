#include <stdio.h>
#include <ctype.h>

// WAP to input a character and check whether it is a 
// lowercase vowel or uppercase vowel or none using if statement.

int main(){
    char ch;
    printf("Enter any vowel: ");
    scanf("%c",&ch);
    if (ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u'){
        if (isupper(ch)){
        printf("The vowel is in uppercase!");
        }
        else if(islower(ch)){
            printf("The vowel is in lowercase!");
        }
        else{
            printf("Wrong character entered!!");
        }
    }
    else{
        printf("Enter a vowel!!");
    }
return 0;
}