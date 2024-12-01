'''
Diseña una simulación de
una cola con prioridad.
'''
import heapq


class ColaConPrioridad:
    def __init__(self):
        # Utilizamos una lista para almacenar los elementos de la cola con prioridad
        self.cola = []

    def insertar(self, prioridad, elemento):
        # Añadimos un elemento a la cola con su prioridad
        # Los elementos con menor prioridad salen primero
        heapq.heappush(self.cola, (prioridad, elemento))
        print(f"Elemento '{elemento}' con prioridad {
              prioridad} insertado en la cola.")

    def eliminar(self):
        # Extraemos el elemento con mayor prioridad (el menor valor de prioridad)
        if self.cola:
            prioridad, elemento = heapq.heappop(self.cola)
            print(f"Elemento '{elemento}' con prioridad {
                  prioridad} eliminado de la cola.")
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
