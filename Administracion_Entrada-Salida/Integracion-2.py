'''
Diseña un sistema que maneje múltiples dispositivos simulados (disco
duro, impresora, teclado) y muestra cómo se realiza la comunicación
entre ellos.

'''


# Definimos las clases que simulan los dispositivos

class Teclado:
    def __init__(self):
        self.tecla_presionada = None

    def presionar_tecla(self, tecla):
        self.tecla_presionada = tecla
        print(f"Tecla '{tecla}' presionada.")

    def obtener_tecla(self):
        return self.tecla_presionada


class DiscoDuro:
    def __init__(self):
        self.datos = ""

    def guardar_datos(self, datos):
        self.datos += datos
        print(f"Datos guardados en el disco duro: {
              self.datos}")  # Muestra todo lo acumulado

    def obtener_datos(self):
        """Devuelve los datos almacenados en el disco duro"""
        return self.datos.strip()


class Impresora:
    def __init__(self):
        self.papel = ""

    def imprimir(self, contenido):
        self.papel += contenido
        print(f"Imprimiendo: {contenido}")

    def obtener_impresiones(self):
        return self.papel


# Clase que simula el controlador de dispositivos
class ControladorDeDispositivos:
    def __init__(self, teclado, disco_duro, impresora):
        self.teclado = teclado
        self.disco_duro = disco_duro
        self.impresora = impresora

    def manejar_comunicacion(self):
        # El usuario presiona una tecla
        tecla = self.teclado.obtener_tecla()
        # El sistema guarda los datos en el disco duro
        if tecla:
            self.disco_duro.guardar_datos(tecla)
        # Luego, el sistema manda a imprimir el carácter presionado
        self.impresora.imprimir(tecla)


# Simulamos el uso del sistema

# Creamos los dispositivos
teclado = Teclado()
disco_duro = DiscoDuro()
impresora = Impresora()

# Creamos el controlador de dispositivos
controlador = ControladorDeDispositivos(teclado, disco_duro, impresora)

# Simulamos que el usuario presiona varias teclas
teclas_a_presionar = ['H', 'o', 'l', 'a', ' ', 'M', 'u', 'n', 'd', 'o']

# El usuario presiona cada tecla y el controlador maneja la comunicación
for tecla in teclas_a_presionar:
    print()
    teclado.presionar_tecla(tecla)
    controlador.manejar_comunicacion()

# Mostramos el contenido completo que ha sido impreso
print("\nContenido impreso completo:", impresora.obtener_impresiones())
