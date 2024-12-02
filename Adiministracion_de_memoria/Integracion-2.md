# Simulación del Swapping de Procesos en Memoria Virtual

Escribe un código que implemente una simulación del swapping de procesos en memoria virtual.

## Código para Simular el Swapping de Procesos

```python
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
        print(f"Memoria insuficiente para el proceso {proceso.id_proceso}. Necesita swapping.")
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
```

## Descripción Paso a Paso

1. **Inicialización de la Memoria y los Procesos**:

   - Acción: Definir el tamaño de la memoria y crear una lista de procesos con tamaños aleatorios.
   - Estado del Sistema: Memoria vacía inicialmente, lista de procesos definida.

2. **Agregar Procesos a la Memoria**:

   - Acción: Intentar agregar cada proceso a la memoria.
   - Flujo de Comunicación:
     - Si hay suficiente memoria disponible, el proceso se agrega.
     - Si no hay suficiente memoria, se realiza el swapping, eliminando un proceso aleatorio para hacer espacio.
   - Salida en Pantalla:
     - Mensajes que muestran si un proceso ha sido agregado o si se necesitó realizar swapping.

3. **Swapping de Procesos**:

   - Acción: Cuando no hay suficiente memoria, se selecciona y elimina un proceso aleatorio para hacer espacio.
   - Estado del Sistema: Actualización de la memoria después de eliminar un proceso y agregar uno nuevo.
   - Salida en Pantalla:
     - Mensajes indicando qué proceso fue eliminado y cuál fue agregado.

4. **Resultado Final**:

   - Acción: Mostrar el estado de la memoria después de cada operación.
   - Estado del Sistema: Estado final de la memoria después de procesar todos los procesos.
   - Salida en Pantalla:
     - Estado actual de la memoria después de cada operación.
