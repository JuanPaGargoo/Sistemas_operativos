# Estructuras de Datos para Manejo de Dispositivos

## Cola de E/S

Una cola de E/S (Entrada/Salida) es una estructura de datos que se usa para organizar las solicitudes de entrada y salida hacia un dispositivo, como un disco duro o una impresora. Cuando un proceso necesita hacer una operación de E/S, esta solicitud se pone en la cola para que se atienda por turnos, generalmente en el orden en que llegaron (FIFO: primero en entrar, primero en salir).

Esto permite que el sistema operativo pueda organizar y atender las solicitudes de manera ordenada y sin problemas. Así se asegura que todos los procesos tengan acceso justo a los dispositivos y se evita que haya conflictos. A veces, el sistema operativo también puede reorganizar las solicitudes en la cola para que el rendimiento sea mejor, por ejemplo, haciendo que el cabezal de un disco se mueva menos.

## Simulación de una Cola con Prioridad

Diseña una simulación de una cola con prioridad.

### Código de la Simulación de Cola con Prioridad

```python
import heapq


class ColaConPrioridad:
    def __init__(self):
        # Utilizamos una lista para almacenar los elementos de la cola con prioridad
        self.cola = []

    def insertar(self, prioridad, elemento):
        # Añadimos un elemento a la cola con su prioridad
        # Los elementos con menor prioridad salen primero
        heapq.heappush(self.cola, (prioridad, elemento))
        print(f"Elemento '{elemento}' con prioridad {prioridad} insertado en la cola.")

    def eliminar(self):
        # Extraemos el elemento con mayor prioridad (el menor valor de prioridad)
        if self.cola:
            prioridad, elemento = heapq.heappop(self.cola)
            print(f"Elemento '{elemento}' con prioridad {prioridad} eliminado de la cola.")
            return elemento
        else:
            print("La cola está vacía.")
            return None

    def mostrar_cola(self):
        # Mostramos el contenido de la cola con prioridad
        if self.cola:
            print("Contenido de la cola con prioridad:")
            for prioridad, elemento in sorted(self.cola):
                print(f"Prioridad: {prioridad}, Elemento: {elemento}")
        else:
            print("La cola está vacía.")


# Ejemplo de uso
if __name__ == "__main__":
    cola_prioridad = ColaConPrioridad()
    cola_prioridad.insertar(4, "Paciente para chequeo de rutina")
    cola_prioridad.insertar(1, "Paciente con trauma severo")
    cola_prioridad.insertar(5, "Paciente con molestias menores")
    cola_prioridad.insertar(2, "Paciente con dolor intenso")
    cola_prioridad.insertar(3, "Paciente con síntomas leves")
    print()
    cola_prioridad.mostrar_cola()
    print()
    cola_prioridad.eliminar()
    cola_prioridad.mostrar_cola()
    print()
    cola_prioridad.eliminar()
    cola_prioridad.mostrar_cola()
```

## Descripción Paso a Paso

1. **Insertar elementos en la cola**:

   - Acción: Insertar diferentes elementos con distintas prioridades en la cola.
   - Estado de la Cola: Los elementos se almacenan en función de su prioridad (los de menor valor salen primero).
   - Salida en Pantalla:
     - "Elemento 'Paciente para chequeo de rutina' con prioridad 4 insertado en la cola."
     - "Elemento 'Paciente con trauma severo' con prioridad 1 insertado en la cola."
     - "Elemento 'Paciente con molestias menores' con prioridad 5 insertado en la cola."
     - "Elemento 'Paciente con dolor intenso' con prioridad 2 insertado en la cola."
     - "Elemento 'Paciente con síntomas leves' con prioridad 3 insertado en la cola."

2. **Mostrar el contenido de la cola**:

   - Acción: Mostrar el contenido de la cola.
   - Estado de la Cola: Ordenada por prioridad.
   - Salida en Pantalla:
     - "Contenido de la cola con prioridad:"
     - "Prioridad: 1, Elemento: Paciente con trauma severo"
     - "Prioridad: 2, Elemento: Paciente con dolor intenso"
     - "Prioridad: 3, Elemento: Paciente con síntomas leves"
     - "Prioridad: 4, Elemento: Paciente para chequeo de rutina"
     - "Prioridad: 5, Elemento: Paciente con molestias menores"

3. **Eliminar el elemento con mayor prioridad**:

   - Acción: Eliminar el elemento con mayor prioridad (menor valor).
   - Estado de la Cola: Se elimina el elemento con prioridad 1.
   - Salida en Pantalla:
     - "Elemento 'Paciente con trauma severo' con prioridad 1 eliminado de la cola."
     - "Contenido de la cola con prioridad:"
     - "Prioridad: 2, Elemento: Paciente con dolor intenso"
     - "Prioridad: 3, Elemento: Paciente con síntomas leves"
     - "Prioridad: 4, Elemento: Paciente para chequeo de rutina"
     - "Prioridad: 5, Elemento: Paciente con molestias menores"

4. **Eliminar otro elemento**:
   - Acción: Eliminar el siguiente elemento con mayor prioridad.
   - Estado de la Cola: Se elimina el elemento con prioridad 2.
   - Salida en Pantalla:
     - "Elemento 'Paciente con dolor intenso' con prioridad 2 eliminado de la cola."
     - "Contenido de la cola con prioridad:"
     - "Prioridad: 3, Elemento: Paciente con síntomas leves"
     - "Prioridad: 4, Elemento: Paciente para chequeo de rutina"
     - "Prioridad: 5, Elemento: Paciente con molestias menores"
