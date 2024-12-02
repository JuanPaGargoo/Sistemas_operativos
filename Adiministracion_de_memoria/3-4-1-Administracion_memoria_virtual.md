# Algoritmo de Reemplazo de Página Least Recently Used (LRU)

Escribe un código que implemente el algoritmo de reemplazo de página "Least Recently Used" (LRU).

## Código para Implementar el Algoritmo LRU

```python
def reemplazo_pagina_lru(paginas, capacidad):
    cache = []
    cargas_pagina = 0

    for pagina in paginas:
        if pagina not in cache:
            # Eliminar la página que lleva más tiempo sin ser utilizada
            if len(cache) >= capacidad:
                cache.pop(0)
            cache.append(pagina)
            # Incrementar el contador de cargas de página cuando la página no está en caché
            cargas_pagina += 1
        else:
            # Si la página ya está en la caché, moverla al final
            cache.remove(pagina)
            cache.append(pagina)

        print(f"Estado de la caché: {cache}")

    return cargas_pagina


# Ejemplo de uso
paginas = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3]
capacidad = 3
cargas = reemplazo_pagina_lru(paginas, capacidad)
print(f"Total de cargas de página: {cargas}")
```

## Descripción Paso a Paso

1. **Inicialización del Algoritmo LRU**:

   - Acción: Definir una caché con una capacidad determinada y una lista de páginas a acceder.
   - Estado del Sistema: Caché vacía inicialmente, lista de páginas definida.

2. **Acceso a las Páginas**:

   - Acción: Iterar sobre cada página para decidir si se debe cargar en la caché o si ya está presente.
   - Flujo de Comunicación:
     - Si la página no está en la caché y la caché está llena, eliminar la página menos recientemente usada.
     - Añadir la nueva página a la caché.
     - Si la página ya está en la caché, moverla al final para marcarla como la más recientemente usada.
   - Salida en Pantalla:
     - Estado de la caché en cada iteración.

3. **Resultado Final**:

   - Acción: Contar el número total de cargas de página necesarias.
   - Estado del Sistema: Mostrar la cantidad de veces que se cargaron páginas en la caché.
   - Salida en Pantalla:
     - Estado final de la caché y el número total de cargas de página.
