# Operaciones de Entrada/Salida Asíncronas con Archivos

Implementa un programa en Python que realice operaciones de entrada/salida asíncronas usando archivos.

## Código para Operaciones Asíncronas con Archivos

```python
import asyncio
import os


async def leer_archivo_asincrono(nombre_archivo):
    try:
        # Simulamos la lectura asíncrona de un archivo
        print(f"Iniciando la lectura del archivo '{nombre_archivo}'...")
        await asyncio.sleep(1)  # Simulamos una operación de E/S con espera
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
        print(f"Contenido del archivo '{nombre_archivo}':\n{contenido}\n")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encuentra.")


async def escribir_archivo_asincrono(nombre_archivo, contenido):
    # Simulamos la escritura asíncrona de un archivo
    print(f"Iniciando la escritura en el archivo '{nombre_archivo}'...")
    await asyncio.sleep(1)  # Simulamos una operación de E/S con espera
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido)
    print(f"Se ha escrito en el archivo '{nombre_archivo}' correctamente.\n")


async def main():
    # Escritura y lectura de archivos de manera asíncrona
    await escribir_archivo_asincrono("Administracion_Entrada-Salida/4-4-2-archivo2.txt", "Hola desde el archivo 2.")
    await leer_archivo_asincrono("Administracion_Entrada-Salida/4-4-2-archivo1.txt")

    # Intentar leer un archivo que no existe
    await leer_archivo_asincrono("no_existe.txt")


# Ejecutar el bucle de eventos asincrónico
if __name__ == "__main__":
    asyncio.run(main())
```

## Descripción Paso a Paso

1. **Inicialización del Programa**:

   - Acción: Ejecutar el programa para iniciar operaciones asíncronas de lectura y escritura de archivos.

2. **Escritura Asíncrona en un Archivo**:

   - Acción: Escribir el contenido "Hola desde el archivo 2." en el archivo `4-4-2-archivo2.txt`.
   - Estado del Archivo: El archivo `4-4-2-archivo2.txt` es creado y contiene el mensaje indicado.
   - Salida en Pantalla:
     - "Iniciando la escritura en el archivo '4-4-2-archivo2.txt'..."
     - "Se ha escrito en el archivo '4-4-2-archivo2.txt' correctamente."

3. **Lectura Asíncrona de un Archivo Existente**:

   - Acción: Leer el contenido del archivo `4-4-2-archivo1.txt`.
   - Estado del Archivo: Sin cambios.
   - Salida en Pantalla (si el archivo existe):
     - "Iniciando la lectura del archivo '4-4-2-archivo1.txt'..."
     - "Contenido del archivo '4-4-2-archivo1.txt': [Datos del archivo]"
   - En caso de no encontrar el archivo:
     - "El archivo '4-4-2-archivo1.txt' no se encuentra."

4. **Intentar Leer un Archivo Inexistente**:

   - Acción: Intentar leer el archivo `no_existe.txt`.
   - Estado del Archivo: El archivo no existe.
   - Salida en Pantalla:
     - "Iniciando la lectura del archivo 'no_existe.txt'..."
     - "El archivo 'no_existe.txt' no se encuentra."
