'''
Escribe un programa en C o Python que simule la administración de
memoria mediante particiones fijas.

'''


class Particion:
    def __init__(self, tamano, id_particion):
        self.tamano = tamano
        self.id_particion = id_particion
        self.ocupada = False
        self.proceso = None

    # Asigna un proceso a la partición
    def asignar_proceso(self, proceso):
        try:
            if self.ocupada:
                raise Exception(
                    f"La partición {self.id_particion} ya está ocupada.")
            if proceso.tamano > self.tamano:
                raise Exception(f"El proceso {
                                proceso.id_proceso} es demasiado grande para la partición {self.id_particion}.")
            self.proceso = proceso
            self.ocupada = True
        except Exception as e:
            print(e)

    # Libera la partición
    def liberar_particion(self):
        self.ocupada = False
        self.proceso = None


# Clase que representa un proceso
class Proceso:
    def __init__(self, id_proceso, tamano):
        self.id_proceso = id_proceso
        self.tamano = tamano


# Clase que administra la memoria con las particiones
class AdministradorMemoria:
    def __init__(self, particiones):
        self.particiones = particiones  # Lista de particiones

    # Asigna un proceso a una partición libre que tenga suficiente espacio
    def asignar_proceso(self, proceso):
        for particion in self.particiones:
            if not particion.ocupada and particion.tamano >= proceso.tamano:
                particion.asignar_proceso(proceso)
                print(f"Proceso {proceso.id_proceso} asignado a la Partición {
                      particion.id_particion}.")
                return
        print(f"No se encontró una partición adecuada para el Proceso {
              proceso.id_proceso}.")

    # Libera una partición que tiene un proceso asignado
    def liberar_proceso(self, id_proceso):
        for particion in self.particiones:
            if particion.ocupada and particion.proceso.id_proceso == id_proceso:
                particion.liberar_particion()
                print(f"Proceso {id_proceso} removido de la Partición {
                      particion.id_particion}.")
                return
        print(f"No se encontró el Proceso {id_proceso}.")

    # Muestra el estado actual de la memoria
    def mostrar_estado_memoria(self):
        print("\nEstado de la Memoria:")
        for particion in self.particiones:
            if particion.ocupada:
                print(f"Partición {particion.id_particion}: Ocupada por el Proceso {
                      particion.proceso.id_proceso} ({particion.proceso.tamano} KB).")
            else:
                print(f"Partición {particion.id_particion}: Libre ({
                      particion.tamano} KB).")


# Ejemplo de uso
if __name__ == "__main__":
    # Definimos las particiones
    particiones = [Particion(100, 1), Particion(
        200, 2), Particion(300, 3), Particion(400, 4)]

    # Inicializamos el administrador de memoria
    administrador = AdministradorMemoria(particiones)

    # Creamos procesos
    procesos = [Proceso(1, 90), Proceso(2, 150),
                Proceso(3, 300), Proceso(4, 50)]

    # Asignamos los procesos a las particiones
    for proceso in procesos:
        administrador.asignar_proceso(proceso)

    # Mostramos el estado actual de la memoria
    administrador.mostrar_estado_memoria()

    # Liberamos un proceso de la memoria
    administrador.liberar_proceso(2)

    # Mostramos el estado actualizado de la memoria
    administrador.mostrar_estado_memoria()

    # Intentamos asignar un nuevo proceso
    nuevo_proceso = Proceso(5, 250)
    administrador.asignar_proceso(nuevo_proceso)

    # Mostramos el estado final de la memoria
    administrador.mostrar_estado_memoria()
