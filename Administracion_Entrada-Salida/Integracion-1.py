'''
Escribe un programa que implemente Escribe un programa que implemente el algoritmo de planificación de
discos "Elevator (SCAN)"
'''


def elevator_scan(cabezal_inicial, solicitudes, tamaño_disco):
    """
    cabezal_inicial: La posición inicial del cabezal del disco.
    solicitudes: Lista de solicitudes de lectura de discos.
    """
    # Ordenamos las solicitudes en orden ascendente
    solicitudes.sort()

    # Separamos las solicitudes que están a la izquierda y a la derecha del cabezal
    izquierda = [
        solicitud for solicitud in solicitudes if solicitud < cabezal_inicial]
    derecha = [
        solicitud for solicitud in solicitudes if solicitud > cabezal_inicial]

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
