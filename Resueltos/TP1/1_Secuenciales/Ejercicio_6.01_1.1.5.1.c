/* Ejercicio_6.01_1.1.5.1
    Escribir un programa que permita calcular el precio de un artículo
    para un año dado, considerando que la inflación es del 4 por 100 anual.
    La fórmula del precio es: P = C * (1 + R) ^ (N - A)
        C - Precio actual.
        N - Año futuro.
        R - Tasa de Inflación.
        A - Año actual.
*/
#include <stdio.h>
#include <math.h> //para funcion potencia "pow()"

int main(){
    //ambiente
    float precio_act, precio_fut;
    int año_act, año_fut;
    float inf = 0.04;
    //proceso
    printf("Inflacion cargada internamente: %f [Porc.] \n",inf*100);
    printf("Ingrese precio actual:\n");
    scanf("%f",&precio_act);
    printf("\t ingresado: $ %f\n",precio_act);
    printf("ingrese año actual:\n");
    scanf("%d",&año_act);
    printf("\t ingresado: Año %d\n",año_act);
    printf("ingrese año futuro:\n");
    scanf("%d",&año_fut);
    printf("\t ingresado: Año %d\n",año_fut);
    precio_fut = precio_act*pow((1+inf),(año_fut-año_act));
    printf("El precio en %d será de $ %f",año_fut,precio_fut);
}
