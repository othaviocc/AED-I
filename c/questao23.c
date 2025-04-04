#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>

int main(){
    int pedidos;
    printf("Numero de pedidos: ");
    scanf("%i", &pedidos);
    int todos[60]; 
    int num[pedidos]; 
    int cont=0;

    for (int i=1; i<=60;i++){
        todos[cont]=i;
        cont++;                       
    }
    for (int n=0; n<pedidos;n++){
        printf("Pedido: ");
        scanf("%i", &num[n]);
        if (num[n]>60 || num[n]<1){
            printf("Processo cancelado, você inseriu um numero diferente de 1 a 60.");
            exit(1);
        }
        for (int j=0;j<60;j++){
            if (num[n]==todos[j]){
                todos[j]=0;
            }
        }                                                         
    }
    printf("\n");
    printf("Pedidos não retirados: ");
    for (int i=0;i<60;i++){
        if (todos[i]!=0){
            printf("%i  ",todos[i]);
        }                                                                       
    }
    return 0;
}