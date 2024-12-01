'''
Escribe un código que implemente el algoritmo de reemplazo de página
"Least Recently Used" (LRU).

'''


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
'''
En este ejemplo, las páginas se vuelven a cargar varias veces cuando ya estaban en la caché.
Esto se puede ver en las iteraciones donde las páginas ya habían sido utilizadas anteriormente.
'''
capacidad = 3
cargas = reemplazo_pagina_lru(paginas, capacidad)
print(f"Total de cargas de página: {cargas}")
