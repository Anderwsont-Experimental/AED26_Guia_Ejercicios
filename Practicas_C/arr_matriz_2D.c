#include <stdio.h>
#include <time.h> //para usar time(NULL)
#include <stdio.h> //para random
//definicion del arreglo
int matrix[15][21];
int filas = 15;
int columnas = 21;
//impresion del arreglo
void imp_arr(){
    printf("\n\t");
    for (int j = 0; j < (columnas); j++)
        {
            printf("| Col ");
        }
    printf("|\n\t");
    for (int j = 0; j < (columnas); j++)
        {
            printf("|%4d ",j);
        }
    printf("|\n\t");
    printf("|-----");
    for (int j = 1; j < (columnas); j++)
        {
            printf("------");
        }
    printf("|\n");
    for (int i = 0; i < filas; i++)
    {
        printf("Fila %2d |",i);
        for (int j = 0; j < (columnas-1); j++)
        {
            printf("%5d ",matrix[i][j]);
        }
        printf("%5d|",matrix[i][columnas]);
        printf("\n");
    }
    printf("\t|-----");
    for (int j = 1; j < (columnas); j++)
        {
            printf("------");
        }
    printf("|\n\n");
}
/************************************************************/
int main(){
    srand(time(NULL)); //Generacion de semilla para random
    for (int i = 0; i < filas; i++)
    {
        for (int j = 0; j < columnas; j++)
        {
            //Carga random del arreglo
            matrix[i][j] = rand() % 100; //el numero hace que los aleatorios sean menores a él. (max: 100000)
        }
    }
    imp_arr();
    return 0;
}
