#include <locale.h>
#include <stdio.h>

int main(){
    setlocale(LC_ALL,"fr_FR.UTF-8");
    printf("Bonjour le monde! \n");
    return 0;
}