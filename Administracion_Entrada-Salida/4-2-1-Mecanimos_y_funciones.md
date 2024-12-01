# Mecanismos y Funciones de los Manejadores de Dispositivos

## Interrupción por E/S

La interrupción por E/S permite que un dispositivo de hardware notifique al sistema operativo cuando necesita atención, evitando que la CPU espere y mejorando la eficiencia.

El sistema operativo administra las interrupciones por E/S mediante un proceso que sigue estos pasos:

1. El dispositivo de hardware genera una interrupción cuando necesita atención.
2. La CPU suspende el proceso actual y guarda su estado.
3. La CPU ejecuta el manejador de interrupción correspondiente para atender al dispositivo.
4. Una vez que la interrupción es atendida, la CPU retoma la ejecución del proceso original.

Este proceso permite al sistema operativo manejar varias tareas a la vez, priorizando las que necesitan respuesta inmediata.

## Ejemplo en Pseudocódigo

```
Proceso principal:
  Ejecutar tarea principal
  Solicitar operación de E/S
  Mientras (operación de E/S no completada):
    Ejecutar otras tareas
  Fin mientras
  Continuar con la tarea principal

Manejador de Interrupción:
  Si (interrupción por E/S recibida):
    Guardar estado del proceso actual
    Atender la solicitud de E/S
    Restaurar estado del proceso
    Reanudar ejecución
Fin manejador
```

El proceso principal realiza otras tareas mientras espera la operación de E/S. Cuando hay una interrupción, el manejador guarda el estado, atiende la solicitud y reanuda el proceso.
