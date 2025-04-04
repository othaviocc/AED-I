#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>

int main(){
    int vitorias[10];
    int j=1;
    int grup1=0;
    int grup2=0;
    int grup3=0;
    int descl=0;
    for (int i=0;i<10;i++){
        printf("Vitorias do jogador %i: ", j);
        scanf("%i", &vitorias[i]);
        if (vitorias[i]>6 || vitorias[i]<=0){
            printf("Numero invalido, tente novamente...");
            i--;
            j--;
        }
        j++;
    }
    for (int i=0;i<10; i++){
        if (vitorias[i]==6 || vitorias[i]==5){
            grup1++;
        }
        if (vitorias[i]==4 || vitorias[i]==3){
            grup2++;
        }
        if (vitorias[i]==2 || vitorias[i]==1){
            grup3++;
        }
        if (vitorias[i]==0){
            descl++;
        }
    }
    printf("\nGrupo 1: %i", grup1);
    printf("\nGrupo 2: %i", grup2);
    printf("\nGrupo 3: %i", grup3);
    printf("\nDesclassificados: %i", descl);
    printf("\n");
    return 0;
}