# Simulación de la Lectura de un Archivo desde un Disco Magnético

Diseña un flujo que describa el proceso de lectura de un archivo desde un disco magnético. Acompáñalo con un programa básico que simule el proceso.

## Código para Simular la Lectura de un Archivo desde un Disco Magnético

```python
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
            print(f"Leyendo archivo '{nombre_archivo}' desde el disco magnético...")
            print(f"Contenido del archivo '{nombre_archivo}': [Datos del archivo]")
        else:
            print(f"El archivo '{nombre_archivo}' no se encuentra en el disco.")


# Ejemplo de uso
if __name__ == "__main__":
    # Inicializamos el disco magnético con algunos archivos
    disco = DiscoMagnetico(["documento.txt", "imagen.jpg", "excel.xlsx", "video.mp4"])

    # Mostramos los archivos disponibles en el disco
    print("\nArchivos disponibles en el disco:")
    disco.mostrar_archivos()

    # Leemos un archivo específico
    print("\nIntentando leer el archivo 'documento.txt':")
    disco.leer_archivo("documento.txt")

    # Intentamos leer un archivo que no existe
    print("\nIntentando leer el archivo 'no_existe.txt':")
    disco.leer_archivo("no_existe.txt")
```

## Descripción Paso a Paso

1. **Inicialización del Disco Magnético**:

   - Acción: Crear una instancia de `DiscoMagnetico` con una lista de archivos.
   - Estado del Disco: Contiene los archivos "documento.txt", "imagen.jpg", "excel.xlsx", "video.mp4".
   - Salida en Pantalla:
     - "Disco Magnético inicializado con archivos:"
     - " - documento.txt"
     - " - imagen.jpg"
     - " - excel.xlsx"
     - " - video.mp4"

2. **Mostrar Archivos Disponibles**:

   - Acción: Mostrar todos los archivos almacenados en el disco.
   - Estado del Disco: Lista de archivos sin cambios.
   - Salida en Pantalla:
     - "Archivos disponibles en el disco:"
     - " - documento.txt"
     - " - imagen.jpg"
     - " - excel.xlsx"
     - " - video.mp4"

3. **Leer un Archivo Existente**:

   - Acción: Leer el archivo "documento.txt" desde el disco.
   - Estado del Disco: Sin cambios.
   - Salida en Pantalla:
     - "Leyendo archivo 'documento.txt' desde el disco magnético..."
     - "Contenido del archivo 'documento.txt': [Datos del archivo]"

4. **Intentar Leer un Archivo Inexistente**:

   - Acción: Intentar leer el archivo "no_existe.txt".
   - Estado del Disco: Sin cambios.
   - Salida en Pantalla:
     - "El archivo 'no_existe.txt' no se encuentra en el disco."
