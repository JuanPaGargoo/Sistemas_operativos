# Simulación de un Manejador de Dispositivos con Tabla de Estructuras

Escribe un programa que simule las operaciones de un manejador de dispositivos utilizando una tabla de estructuras.

## Código del Manejador de Dispositivos

```python
class ManejadorDispositivos:
    def __init__(self):
        # La tabla será una lista de diccionarios, cada uno representando un dispositivo
        self.tabla_dispositivos = []

    def registrar_dispositivo(self, id_dispositivo, nombre, estado):
        # Agregamos un nuevo dispositivo a la tabla
        dispositivo = {
            'ID': id_dispositivo,
            'Nombre': nombre,
            'Estado': estado
        }
        self.tabla_dispositivos.append(dispositivo)
        print(f"Dispositivo '{nombre}' (ID: {id_dispositivo}) registrado con estado '{estado}'.")

    def actualizar_estado(self, id_dispositivo, nuevo_estado):
        # Actualizamos el estado de un dispositivo existente
        for dispositivo in self.tabla_dispositivos:
            if dispositivo['ID'] == id_dispositivo:
                dispositivo['Estado'] = nuevo_estado
                print(f"Estado del dispositivo '{dispositivo['Nombre']}' actualizado a '{nuevo_estado}'.")
                return
        print(f"Dispositivo con ID {id_dispositivo} no encontrado.")

    def mostrar_dispositivos(self):
        # Mostramos la información de todos los dispositivos registrados
        if self.tabla_dispositivos:
            print("Tabla de Dispositivos Registrados:")
            for dispositivo in self.tabla_dispositivos:
                print(f"ID: {dispositivo['ID']}, Nombre: {dispositivo['Nombre']}, Estado: {dispositivo['Estado']}")
        else:
            print("No hay dispositivos registrados.")

    def eliminar_dispositivo(self, id_dispositivo):
        # Eliminamos un dispositivo de la tabla
        for dispositivo in self.tabla_dispositivos:
            if dispositivo['ID'] == id_dispositivo:
                self.tabla_dispositivos.remove(dispositivo)
                print(f"Dispositivo '{dispositivo['Nombre']}' (ID: {id_dispositivo}) eliminado de la tabla.")
                return
        print(f"Dispositivo con ID {id_dispositivo} no encontrado.")


# Ejemplo de uso
if __name__ == "__main__":
    manejador = ManejadorDispositivos()
    manejador.registrar_dispositivo(1, "Impresora", "Inactivo")
    manejador.registrar_dispositivo(2, "Escáner", "Activo")
    manejador.registrar_dispositivo(3, "Monitor", "Inactivo")
    print()
    manejador.mostrar_dispositivos()
    print()
    manejador.actualizar_estado(2, "En mantenimiento")
    manejador.eliminar_dispositivo(1)
    print()
    manejador.mostrar_dispositivos()
```

## Descripción Paso a Paso

1. **Registrar dispositivos**:

   - Acción: Registrar varios dispositivos con diferentes estados.
   - Estado de la Tabla: Cada dispositivo se almacena como un diccionario en la lista `tabla_dispositivos`.
   - Salida en Pantalla:
     - "Dispositivo 'Impresora' (ID: 1) registrado con estado 'Inactivo'."
     - "Dispositivo 'Escáner' (ID: 2) registrado con estado 'Activo'."
     - "Dispositivo 'Monitor' (ID: 3) registrado con estado 'Inactivo'."

2. **Mostrar los dispositivos registrados**:

   - Acción: Mostrar todos los dispositivos registrados en la tabla.
   - Estado de la Tabla: Lista de todos los dispositivos registrados.
   - Salida en Pantalla:
     - "Tabla de Dispositivos Registrados:"
     - "ID: 1, Nombre: Impresora, Estado: Inactivo"
     - "ID: 2, Nombre: Escáner, Estado: Activo"
     - "ID: 3, Nombre: Monitor, Estado: Inactivo"

3. **Actualizar el estado de un dispositivo**:

   - Acción: Actualizar el estado del dispositivo con ID 2 a "En mantenimiento".
   - Estado de la Tabla: Se actualiza el estado del dispositivo correspondiente.
   - Salida en Pantalla:
     - "Estado del dispositivo 'Escáner' actualizado a 'En mantenimiento'."

4. **Eliminar un dispositivo**:

   - Acción: Eliminar el dispositivo con ID 1.
   - Estado de la Tabla: Se elimina el dispositivo correspondiente de la lista.
   - Salida en Pantalla:
     - "Dispositivo 'Impresora' (ID: 1) eliminado de la tabla."

5. **Mostrar los dispositivos después de las modificaciones**:

   - Acción: Mostrar los dispositivos restantes en la tabla.
   - Estado de la Tabla: Lista de los dispositivos que quedan después de las operaciones.
   - Salida en Pantalla:
     - "Tabla de Dispositivos Registrados:"
     - "ID: 2, Nombre: Escáner, Estado: En mantenimiento"
     - "ID: 3, Nombre: Monitor, Estado: Inactivo"
