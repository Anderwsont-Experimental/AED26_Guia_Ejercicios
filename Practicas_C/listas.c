#include <stdio.h>
#include <stdlib.h>

// Definición de la estructura del nodo
typedef struct Nodo {
    int dato;               // El valor que almacena el nodo
    struct Nodo* siguiente; // Puntero al siguiente nodo
} Nodo;

//funcion que crea nodo
Nodo *crearNodo(int valor) {
    // 1. Reservar memoria para el nuevo nodo
    Nodo* nuevoNodo = (Nodo*) malloc(sizeof(Nodo));
    
    // Verificar si la asignación de memoria falló
    if (nuevoNodo == NULL) {
        printf("Error: No se pudo asignar memoria.\n");
        exit(1);
    }
    
    // 2. Asignar el dato e inicializar el puntero siguiente a NULL
    nuevoNodo->dato = valor;
    nuevoNodo->siguiente = NULL;
    
    return nuevoNodo;
}