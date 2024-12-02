# Sistema Básico de Simulación con Interrupciones

Escribe un programa que utilice el manejo de interrupciones en un sistema básico de simulación.

## Código del Sistema Básico de Simulación con Interrupciones

```python
import time
import threading


class SistemaSimulado:
    def __init__(self):
        self.ejecutando = True
        self.interrupcion_pendiente = False

    def tarea_principal(self):
        while self.ejecutando:
            print("Ejecutando tarea principal...")
            time.sleep(1)
            # Simular la espera de una operación de E/S
            if self.interrupcion_pendiente:
                self.manejador_interrupcion()

    def solicitar_interrupcion(self):
        # Simula una interrupción por E/S después de un tiempo
        time.sleep(3)
        print("Interrupción generada por dispositivo de E/S.")
        self.interrupcion_pendiente = True

    def manejador_interrupcion(self):
        # Maneja la interrupción cuando es recibida
        print("Interrupción recibida. Guardando estado del proceso actual...")
        time.sleep(1)
        print("Atendiendo solicitud de E/S...")
        time.sleep(2)
        print("Restaurando estado del proceso y reanudando ejecución.")
        self.interrupcion_pendiente = False

    def detener_sistema(self):
        # Detener la simulación
        self.ejecutando = False
        print("Sistema detenido.")


# Ejemplo de uso
if __name__ == "__main__":
    sistema = SistemaSimulado()
    # Crear un hilo para simular la solicitud de interrupción
    hilo_interrupcion = threading.Thread(target=sistema.solicitar_interrupcion)
    hilo_interrupcion.start()

    try:
        # Ejecutar la tarea principal
        sistema.tarea_principal()
    except KeyboardInterrupt:
        # Detener el sistema cuando el usuario interrumpe manualmente con Ctrl+C
        sistema.detener_sistema()
```

## Descripción Paso a Paso

1. **Iniciar la simulación del sistema**:

   - Acción: Crear una instancia de `SistemaSimulado()` y ejecutar `tarea_principal()`.
   - Estado del Sistema: Ejecutando.
   - Salida en Pantalla: "Ejecutando tarea principal..." (repetitivo cada segundo).

2. **Generar una interrupción**:

   - Acción: El hilo `hilo_interrupcion` genera una interrupción después de 3 segundos.
   - Estado del Sistema: Interrupción pendiente.
   - Salida en Pantalla: "Interrupción generada por dispositivo de E/S."

3. **Manejo de la interrupción**:

   - Acción: `manejador_interrupcion()` se invoca automáticamente.
   - Estado del Sistema: Guardando el estado, atendiendo solicitud de E/S, restaurando estado.
   - Salida en Pantalla:
     - "Interrupción recibida. Guardando estado del proceso actual..."
     - "Atendiendo solicitud de E/S..."
     - "Restaurando estado del proceso y reanudando ejecución."

4. **Detener el sistema**:
   - Acción: El usuario interrumpe manualmente con `Ctrl+C`.
   - Estado del Sistema: Detenido.
   - Salida en Pantalla: "Sistema detenido."
