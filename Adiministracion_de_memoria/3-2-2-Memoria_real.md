# Algoritmo de Primera Cabida para Asignación de Memoria

Diseña un algoritmo para calcular qué procesos pueden ser asignados a un sistema con memoria real limitada utilizando el algoritmo de "primera cabida".

## Código para Implementar el Algoritmo de Primera Cabida

```python
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
```

## Descripción Paso a Paso

1. **Inicialización de Memoria y Procesos**:

   - Acción: Definir particiones de memoria disponibles y procesos que requieren asignación.
   - Estado del Sistema: Listas `memoria` y `procesos` inicializadas con los tamaños correspondientes.

2. **Asignación de Procesos a Memoria**:

   - Acción: Iterar sobre cada proceso e intentar asignarlo a la primera partición libre con suficiente espacio.
   - Flujo de Comunicación:
     - Cada proceso se asigna a la primera partición donde cabe.
     - Si no hay una partición adecuada, el proceso no es asignado.
   - Salida en Pantalla:
     - Mensajes que muestran la asignación de procesos a particiones o la falta de espacio disponible.

3. **Mostrar Procesos No Asignados**:

   - Acción: Listar los procesos que no pudieron ser asignados a ninguna partición.
   - Estado del Sistema: Los procesos que no encontraron una partición adecuada permanecen sin asignar.
   - Salida en Pantalla:
     - Lista de procesos no asignados.

4. **Mostrar Estado Final de la Memoria**:

   - Acción: Mostrar la memoria restante en cada partición después de la asignación.
   - Estado del Sistema: Cada partición muestra cuánta memoria libre queda.
   - Salida en Pantalla:
     - Detalles de cada partición, indicando cuánta memoria queda disponible.
