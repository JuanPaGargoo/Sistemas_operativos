'''
Realiza una simulación en cualquier lenguaje de programación que
emule el swapping de procesos en memoria virtual.

'''

import random
import time

TAMANIO_MEMORIA = 50
memoria = []

# Creamos una clase para los procesos


class Proceso:
    def __init__(self, id_proceso, tamanio):
        self.id_proceso = id_proceso
        self.tamanio = tamanio

# Función para agregar un proceso a la memoria


def agregar_proceso(proceso):
    if len(memoria) + proceso.tamanio <= TAMANIO_MEMORIA:
        memoria.extend([proceso.id_proceso] * proceso.tamanio)
        print(f"Proceso {proceso.id_proceso} agregado a la memoria.")
    else:
        print(f"Memoria insuficiente para el proceso {
              proceso.id_proceso}. Necesita swapping.")
        swapping(proceso)

# Función para remover un proceso de la memoria


def remover_proceso(proceso_id):
    while proceso_id in memoria:
        memoria.remove(proceso_id)
    print(f"Proceso {proceso_id} eliminado de la memoria.")

# Función para realizar el swapping de procesos


def swapping(proceso):
    # Seleccionamos un proceso aleatorio para eliminar
    if memoria:
        proceso_a_eliminar = random.choice(memoria)
        remover_proceso(proceso_a_eliminar)
        agregar_proceso(proceso)
    else:
        print("La memoria está vacía, no se puede realizar el swapping.")

# Simulación de la ejecución de procesos en memoria


def simulacion():
    # Creamos una lista de procesos con tamaños aleatorios
    procesos = [Proceso(i, random.randint(10, 20)) for i in range(1, 16)]

    for proceso in procesos:
        # Pausa para simular el tiempo de ejecución de un proceso
        time.sleep(0.5)
        agregar_proceso(proceso)
        print(f"Estado actual de la memoria: {memoria}")


# Ejecutamos la simulación
if __name__ == "__main__":
    simulacion()
