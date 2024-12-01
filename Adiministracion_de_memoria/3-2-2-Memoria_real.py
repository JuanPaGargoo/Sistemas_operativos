'''
Diseña un algoritmo para calcular qué procesos pueden ser asignados
a un sistema con memoria real limitada utilizando el algoritmo de
"primera cabida".

'''


def primera_cabida(memoria, procesos):
    """
    memoria:  Lista que contiene los tamaños de diferentes espacios
              de memoria disponibles.
    procesos: Lista con tamaños de procesos.
    return: Diccionario con asignación de procesos y procesos no asignados.
    """

    # Clonar la lista de memoria para simular el uso de memoria real
    memoria_disponible = memoria[:]
    asignacion = {}
    no_asignados = []

    # Iterar sobre cada proceso para intentar asignarlo a una partición disponible
    for i, proceso in enumerate(procesos):
        asignado = False
        for j, particion in enumerate(memoria_disponible):
            # Si el proceso cabe en la partición
            if proceso <= particion:
                asignacion[f'Proceso_{i+1}'] = f'Partición_{j+1}'
                # Reducir la memoria disponible en esa partición
                memoria_disponible[j] -= proceso
                asignado = True
                break
        if not asignado:
            no_asignados.append(f'Proceso_{i+1}')

    return {
        'Asignación': asignacion,
        'No Asignados': no_asignados,
        'Memoria Final': memoria_disponible
    }


# Ejemplo de uso
if __name__ == "__main__":
    # Tamaño de particiones de memoria
    memoria = [100, 500, 200, 300, 600]
    # Tamaño de procesos
    procesos = [212, 417, 112, 426]

    resultado = primera_cabida(memoria, procesos)

    print("Asignación de procesos:")
    for proceso, particion in resultado['Asignación'].items():
        print(f"  {proceso} → {particion}")

    print("\nProcesos no asignados:")
    for proceso in resultado['No Asignados']:
        print(f"  {proceso}")

    print("\nEstado final de la memoria:")
    for i, memoria_restante in enumerate(resultado['Memoria Final']):
        print(f"  Partición_{i+1}: {memoria_restante} unidades restantes")
