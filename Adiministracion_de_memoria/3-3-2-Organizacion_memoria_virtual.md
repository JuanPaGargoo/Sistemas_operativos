# Simulación de una Tabla de Páginas para Procesos con Acceso Aleatorio a Memoria Virtual

Escribe un programa que simule una tabla de páginas para procesos con acceso aleatorio a memoria virtual.

## Código para Simular una Tabla de Páginas

```python
import random

# Configuración de memoria y tabla de páginas
TAMANO_MEMORIA = 1024  # Tamaño de la memoria
TAMANO_PAGINA = 64     # Tamaño de cada página
NUM_PAGINAS = TAMANO_MEMORIA // TAMANO_PAGINA

# Inicializamos la memoria física
memoria = [None] * NUM_PAGINAS

# Tabla de páginas (un diccionario para asociar procesos con sus páginas)
tabla_paginas = {}

# Función para crear un proceso
def crear_proceso(id_proceso, num_paginas):

    # Si el proceso ya existe
    if id_proceso in tabla_paginas:
        print(f"El proceso {id_proceso} ya existe.")
        return

    paginas_asignadas = []
    # Se obtiene una lista de todas las páginas disponibles en la memoria
    paginas_disponibles = [i for i in range(NUM_PAGINAS) if memoria[i] is None]
    # Si no hay suficientes páginas disponibles
    if len(paginas_disponibles) < num_paginas:
        print("No hay suficiente memoria para el proceso.")
        return

    # Se asignan aleatoriamente las páginas necesarias al proceso
    for _ in range(num_paginas):
        # Se elige una página disponible al azar
        pagina = random.choice(paginas_disponibles)
        # Se elimina de la lista de disponibles
        paginas_disponibles.remove(pagina)
        # Se asigna la página al proceso en la memoria
        memoria[pagina] = id_proceso
        # Se añade a la lista de páginas asignadas
        paginas_asignadas.append(pagina)

    # Se guarda la información del proceso en la tabla de páginas
    tabla_paginas[id_proceso] = paginas_asignadas
    print(f"Proceso {id_proceso} creado con las páginas: {paginas_asignadas}")

# Función para acceder a una página de un proceso
def acceder_memoria(id_proceso, numero_pagina):

    # Si el proceso no existe
    if id_proceso not in tabla_paginas:
        print(f"El proceso {id_proceso} no existe.")
        return

    # Si el número de página no es válido
    if numero_pagina < 0 or numero_pagina >= len(tabla_paginas[id_proceso]):
        print(f"El proceso {id_proceso} no tiene la página {numero_pagina}.")
        return

    # Se obtiene la página física que corresponde a la página del proceso
    pagina_fisica = tabla_paginas[id_proceso][numero_pagina]
    print(f"Accediendo a la página {numero_pagina} del proceso {id_proceso}, que está en la página física {pagina_fisica}.")

# Función para finalizar un proceso y liberar sus páginas
def finalizar_proceso(id_proceso):

    # Si el proceso no existe
    if id_proceso not in tabla_paginas:
        print(f"El proceso {id_proceso} no existe.")
        return

    # Se liberan todas las páginas ocupadas por el proceso
    for pagina in tabla_paginas[id_proceso]:
        memoria[pagina] = None
    # Se elimina el proceso de la tabla de páginas
    del tabla_paginas[id_proceso]
    print(f"Proceso {id_proceso} finalizado y memoria liberada.")

# Ejemplo de uso
crear_proceso("A", 3)  # Crear proceso A con 3 páginas
crear_proceso("B", 5)  # Crear proceso B con 5 páginas
acceder_memoria("A", 1)  # Acceder a la página 1 del proceso A
acceder_memoria("B", 4)  # Acceder a la página 4 del proceso B
finalizar_proceso("A")  # Finalizar proceso A y liberar su memoria
crear_proceso("C", 2)  # Crear proceso C con 2 páginas
acceder_memoria("C", 0)  # Acceder a la página 0 del proceso C
finalizar_proceso("B")  # Finalizar proceso B y liberar su memoria
```

## Descripción Paso a Paso

1. **Inicialización de la Memoria y la Tabla de Páginas**:

   - Acción: Definir el tamaño de la memoria y la página, calcular el número de páginas disponibles.
   - Estado del Sistema: Memoria física inicializada con todas las páginas libres, tabla de páginas vacía.

2. **Creación de Procesos y Asignación de Páginas**:

   - Acción: Crear un proceso y asignar aleatoriamente las páginas necesarias.
   - Flujo de Comunicación:
     - Comprobar si hay suficientes páginas disponibles.
     - Asignar aleatoriamente las páginas y actualizar la memoria y la tabla de páginas.
   - Salida en Pantalla:
     - Mensajes que indican qué páginas han sido asignadas a cada proceso.

3. **Acceso a Memoria de un Proceso**:

   - Acción: Acceder a una página específica de un proceso.
   - Estado del Sistema: Mostrar la ubicación física de la página solicitada.
   - Salida en Pantalla:
     - Mensaje indicando la página del proceso y la ubicación física correspondiente.

4. **Finalización de un Proceso y Liberación de Memoria**:

   - Acción: Finalizar un proceso y liberar sus páginas asignadas.
   - Estado del Sistema: Memoria actualizada para reflejar las páginas liberadas, eliminación del proceso de la tabla de páginas.
   - Salida en Pantalla:
     - Mensaje indicando que el proceso ha sido finalizado y sus páginas han sido liberadas.
