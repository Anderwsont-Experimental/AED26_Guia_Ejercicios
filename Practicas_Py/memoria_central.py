import string
import os

def limpiar_pantalla():
    # 'nt' corresponde a Windows, de lo contrario es Linux/macOS
    os.system("cls" if os.name == "nt" else "clear")

# --- DEFINICIONES DE ESTADOS DE MEMORIA ---
MEM_LIBRE = ["~"]  # Espacio libre sin usar
MEM_FRAG = ["*"]  # Espacio con fragmentación externa
MEM_VACIA = MEM_LIBRE + MEM_FRAG  # Espacio asignable para un nuevo proceso
MEM_SO = ["#"]  # Carácter para el Sistema Operativo

# Definicion de Caracteres Permitidos, para validar entradas manuales
caracteres_permitidos = list(string.ascii_uppercase) + MEM_VACIA

# Creación de Memoria Central (MC) inicializada con el estado de memoria libre
TAM_SO = 100
memoria_central = MEM_SO * TAM_SO + [MEM_LIBRE[0] for _ in range(550 - TAM_SO)]

# FUNCION imprimir en pantalla estado de memoria central
def mapa_MC(mc):
    """Muestra los elementos de la memoria central en filas de 45 columnas
    separadas únicamente por un espacio.
    """
    for i in range(0, len(mc), 25):
        fila = mc[i : i + 25] # Tomamos un bloque de 45 elementos usando slicing [i:i+10]
        print(" ".join(fila)) # Los unimos separados por un espacio y los imprimimos

# FUNCIÓN para cargar un proceso en memoria
def carga_proceso(dir, tam, proc):
    """Carga el proceso 'proc' en 'memoria_central' desde el índice 'dir'
    ocupando 'tam' posiciones consecutivas.
    """
    # Validación del carácter del proceso
    if proc not in caracteres_permitidos:
        print(f"Error: El proceso '{proc}' no es un carácter permitido.")
        return False

    # Validación de límites en la memoria central
    if dir < 0 or dir >= len(memoria_central):
        print(
            f"Error: La dirección inicial {dir} está fuera del rango de memoria (0-449)."
        )
        return False

    if dir + tam > len(memoria_central):
        print(
            f"Error: El proceso de tamaño {tam} excede el límite de la memoria desde la dirección {dir}."
        )
        return False

    # Carga del proceso en las posiciones indicadas
    for i in range(dir, dir + tam):
        memoria_central[i] = proc

    print(
        f"Proceso '{proc}' cargado con éxito en las direcciones [{dir} a {dir + tam - 1}]."
    )
    return True

# FUNCIÓN de asignación por Best Fit
def asignar_bestfit(tam, proc):
    """Busca el hueco vacío (MEM_VACIA) que mejor se ajuste a 'tam'

    y carga el proceso 'proc' en la mejor dirección tentada.
    """
    dir_tentativa = -1
    menor_tamano_hueco = float("inf")

    i = 0
    n = len(memoria_central)

    while i < n:
        # 1. Encontrar el inicio de un bloque vacío (MEM_VACIA)
        if memoria_central[i] in MEM_VACIA:
            inicio_hueco = i

            # Contar la extensión total del hueco continuo
            while i < n and memoria_central[i] in MEM_VACIA:
                i += 1

            tamano_hueco = i - inicio_hueco

            # 2. Verificar si el hueco tiene espacio suficiente
            if tamano_hueco >= tam:
                # Comprobar con menor estricto (<) para mantener la dirección más baja posible
                if tamano_hueco < menor_tamano_hueco:
                    menor_tamano_hueco = tamano_hueco
                    dir_tentativa = inicio_hueco
            else:
                # 3. Si NO cabe, marcar este bloque insuficiente como fragmentación externa
                carga_proceso(
                    dir=inicio_hueco, tam=tamano_hueco, proc=MEM_FRAG[0]
                )
        else:
            i += 1

    # Al finalizar el recorrido de la memoria:
    if dir_tentativa != -1:
        exito = carga_proceso(dir=dir_tentativa, tam=tam, proc=proc)
        if exito:
            print(
                f"ASIGNACIÓN BEST-FIT: Proceso '{proc}' (tam: {tam}) asignado en la dirección {dir_tentativa} (tamaño del hueco: {menor_tamano_hueco})."
            )
            return True
    else:
        print(
            f"ERROR: No se encontró ningún espacio suficiente para asignar el proceso '{proc}' de tamaño {tam}."
        )
        return False

# --- Demostración de Uso ---

limpiar_pantalla()
print("--- ESTADO INICIAL ---")
mapa_MC(memoria_central)

# Escenario de prueba:
carga_proceso(dir=130, tam=20, proc="X")  # Hueco 1 de tamaño 30 (100 a 129)
carga_proceso(dir=300, tam=50, proc="Y")  # Hueco 2 de tamaño 150 (150 a 299)
carga_proceso(dir=400, tam=20, proc="Z")  # Hueco 3 de tamaño 50 (350 a 399)

print("\n--- ESCENARIO DE PRUEBA CREADO ---")
mapa_MC(memoria_central)

input("Presione ENTER para continuar...")

print("\n--- APLICANDO BEST FIT PARA PROCESO 'B' (TAMAÑO 40) ---")
asignar_bestfit(tam=40, proc="B")

print("\n--- RESULTADO FINAL EN MEMORIA ---")
mapa_MC(memoria_central)