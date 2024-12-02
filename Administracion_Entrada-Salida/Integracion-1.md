# Algoritmo de Planificación de Discos: Elevator (SCAN)

Escribe un programa que implemente el algoritmo de planificación de discos "Elevator (SCAN)".

## Código para Implementar el Algoritmo SCAN

```python
def elevator_scan(cabezal_inicial, solicitudes, tamaño_disco):
    """
    cabezal_inicial: La posición inicial del cabezal del disco.
    solicitudes: Lista de solicitudes de lectura de discos.
    tamaño_disco: Tamaño total del disco.
    """
    # Ordenamos las solicitudes en orden ascendente
    solicitudes.sort()

    # Separamos las solicitudes que están a la izquierda y a la derecha del cabezal
    izquierda = [solicitud for solicitud in solicitudes if solicitud < cabezal_inicial]
    derecha = [solicitud for solicitud in solicitudes if solicitud > cabezal_inicial]

    # Invertimos la lista 'izquierda' para procesar en orden descendente
    izquierda.reverse()

    # Creamos la secuencia de movimientos del cabezal
    secuencia = []

    # Mover hacia la derecha primero
    secuencia += derecha
    # Luego ir al final del disco
    secuencia += [tamaño_disco - 1]
    # Y procesar las solicitudes a la izquierda
    secuencia += izquierda

    # Devolvemos la secuencia de accesos
    return secuencia


# Datos de prueba
cabezal_inicial = 50
solicitudes = [98, 183, 37, 122, 14, 124, 65, 67]
tamaño_disco = 200

# Ejecutamos el algoritmo
secuencia = elevator_scan(cabezal_inicial, solicitudes, tamaño_disco)

# Imprimimos la secuencia de acceso
print("Secuencia de acceso del disco:", secuencia)
```

## Descripción Paso a Paso

1. **Inicialización del Algoritmo SCAN**:

   - Acción: Ordenar las solicitudes en orden ascendente y dividirlas en solicitudes a la izquierda y a la derecha del cabezal inicial.
   - Estado del Cabezal: Cabezal inicial en la posición 50.
   - Solicitudes: [98, 183, 37, 122, 14, 124, 65, 67] (ordenadas y separadas).

2. **Movimiento del Cabezal hacia la Derecha**:

   - Acción: Mover el cabezal hacia la derecha, atendiendo todas las solicitudes en esa dirección.
   - Estado del Disco: Procesando las solicitudes en la dirección derecha hasta llegar al final del disco.
   - Secuencia: [65, 67, 98, 122, 124, 183].

3. **Mover al Final del Disco**:

   - Acción: Mover el cabezal al final del disco (posición 199).
   - Estado del Disco: Cabezal en el final del disco.
   - Secuencia: [199].

4. **Movimiento del Cabezal hacia la Izquierda**:

   - Acción: Atender las solicitudes a la izquierda del cabezal inicial.
   - Estado del Disco: Procesando las solicitudes en orden descendente.
   - Secuencia: [37, 14].
