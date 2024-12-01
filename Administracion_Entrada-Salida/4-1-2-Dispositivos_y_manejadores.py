'''
Diseña un programa que implemente un manejador de dispositivos
sencillo para un dispositivo virtual de entrada.

'''


class DispositivoVirtual:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estado = "desconectado"
        self.datos = []

    def conectar(self):
        # Conecta el dispositivo si está desconectado
        if self.estado == "desconectado":
            self.estado = "conectado"
            print(f"El dispositivo '{self.nombre}' está ahora conectado.")
        else:
            print(f"El dispositivo '{self.nombre}' ya está conectado.")

    def desconectar(self):
        # Desconecta el dispositivo si está conectado
        if self.estado == "conectado":
            self.estado = "desconectado"
            print(f"El dispositivo '{self.nombre}' se ha desconectado.")
        else:
            print(f"El dispositivo '{self.nombre}' ya está desconectado.")

    def leer_datos(self):
        # Lee datos del dispositivo si está conectado
        if self.estado == "conectado":
            # Simulamos la lectura de datos del dispositivo
            dato = input(f"Ingrese un dato para el dispositivo '{
                         self.nombre}': ")
            self.datos.append(dato)
            print(f"Dato '{dato}' recibido del dispositivo '{self.nombre}'.")
        else:
            print(f"No se puede leer datos porque el dispositivo '{
                  self.nombre}' está desconectado.")

    def mostrar_datos(self):
        # Muestra los datos recibidos si existen
        if len(self.datos) > 0:
            print(f"Datos recibidos del dispositivo '{
                  self.nombre}': {', '.join(self.datos)}")
        else:
            print(f"No se han recibido datos del dispositivo '{
                  self.nombre}' todavía.")


# Ejemplo de uso
if __name__ == "__main__":
    dispositivo = DispositivoVirtual("Dispositivo de Entrada 1")
    dispositivo.conectar()  # Conecta el dispositivo
    dispositivo.leer_datos()  # Lee un dato del dispositivo
    dispositivo.mostrar_datos()  # Muestra los datos recibidos
    dispositivo.desconectar()  # Desconecta el dispositivo
