#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>

void ler(){
    char string[27];
    int i, f;
    printf("String: ");
    scanf("%9s", string);                //A STRING TODA
    printf("\nInicio: ");
    scanf("%i", &i);                     //O INICIO
    printf("\nFim: ");
    scanf("%i", &f);                     //O FIM


    for (int j=0;j<27;j++){
        if (j>=i && j<=f){
            printf("%c", string[j]);                //CALCULO PARA FAZER O CORTE DAS PARTES INDESEJADAS
        }
    }
}

int main(){
    ler();
    printf("\n");
    return 0;
}