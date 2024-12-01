'''
Implementa un programa en Python, C o java que realice operaciones
de entrada/salida asíncronas usando archivos.

'''
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
    print("Directorio de trabajo actual:", os.getcwd())
    asyncio.run(main())
