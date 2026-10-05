#include <stdio.h>
#include <time.h> //para usar time(NULL)
#include <stdio.h> //para random?
//definicion del arreglo
int vector[20];
int largo = sizeof(vector) / sizeof(vector[0]); //calcula cant elementos mediante cociente de los pesos.
//impresion del arreglo
void imp_arr(int disp){
    if (disp==0)
    {
        //impresion en vertical hasta 3 digitos
        printf(" Indice\t  Valor\n|--------------|\n");
        for (int i = 0; i < largo; i++) {printf("|%5d\t|%5d |\n",i,vector[i]);}
        printf("|--------------|\n");
    }else{
        //impresion en horizontal
        printf("\t -");
        for (int i = 0; i < largo; i++) {printf("-------");}
        printf("\n");
        printf("Indice:\t");
        for (int i = 0; i < largo; i++) {printf(" |%5d",i);}
        printf(" |\nValor:\t");
        for (int i = 0; i < largo; i++) {printf(" |%5d",vector[i]);}
        printf(" |\n\t -");
        for (int i = 0; i < largo; i++) {printf("-------");}
        printf("\n");
    }
}
/************************************************************/
int main(){
    srand(time(NULL)); //Generacion de semilla para random
    for (int i = 0; i < largo; i++)
    {
        //Carga manual del arreglo
        /* printf("ingrese contenido para posicion %d: ",i);
        scanf("%d",&a[i]); */

        //Carga random del arreglo
        vector[i] = rand() % 100; //el numero hace que los aleatorios sean menores a él.
    }
    
    imp_arr((largo-1) % 20); //Automaticamente vertical si largo supera 20
    return 0;
}
