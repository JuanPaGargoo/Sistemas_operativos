'''
Diseña un flujo que describa el proceso de lectura de un archivo desde
un disco magnético. Acompáñalo con un programa básico que simule
el proceso.

'''


class DiscoMagnetico:
    def __init__(self, archivos):
        # Inicializamos el disco con una lista de archivos disponibles
        self.archivos = archivos
        print("Disco Magnético inicializado con archivos: ")
        self.mostrar_archivos()

    def mostrar_archivos(self):
        # Mostrar los archivos almacenados en el disco
        if self.archivos:
            for archivo in self.archivos:
                print(f" - {archivo}")
        else:
            print("El disco está vacío.")

    def leer_archivo(self, nombre_archivo):
        # Simulamos la lectura de un archivo del disco magnético
        if nombre_archivo in self.archivos:
            print(f"Leyendo archivo '{
                  nombre_archivo}' desde el disco magnético...")
            print(f"Contenido del archivo '{
                  nombre_archivo}': [Datos del archivo]")
        else:
            print(f"El archivo '{
                  nombre_archivo}' no se encuentra en el disco.")


# Ejemplo de uso
if __name__ == "__main__":
    # Inicializamos el disco magnético con algunos archivos
    disco = DiscoMagnetico(
        ["documento.txt", "imagen.jpg", "excel.xlsx", "video.mp4"])

    # Mostramos los archivos disponibles en el disco
    print("\nArchivos disponibles en el disco:")
    disco.mostrar_archivos()

    # Leemos un archivo específico
    print("\nIntentando leer el archivo 'documento1.txt':")
    disco.leer_archivo("documento.txt")

    # Intentamos leer un archivo que no existe
    print("\nIntentando leer el archivo 'no_existe.txt':")
    disco.leer_archivo("no_existe.txt")
