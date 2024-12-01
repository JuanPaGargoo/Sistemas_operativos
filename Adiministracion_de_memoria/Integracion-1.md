# Análisis de la Administración de Memoria Virtual en Windows

## Introducción

Windows utiliza memoria virtual para gestionar los recursos de manera eficiente, permitiendo que cada proceso tenga su propio espacio de direcciones, aunque la memoria física esté dividida.

## Páginas y Segmentos de Memoria

Windows usa paginación para administrar la memoria virtual dividiendo el espacio de direcciones en páginas (generalmente 4 KB) que se asignan a la memoria física según la demanda. Si la RAM está llena, Windows usa un archivo llamado pagefile.sys para mover datos y liberar RAM.

## Mecanismos de Administración

Windows gestiona la memoria virtual mediante varios mecanismos:

1. **Paginación por Demanda**: Carga en RAM una página que no está en memoria física cuando se necesita.

2. **Reemplazo de Páginas**: Usa un algoritmo **LRU** para mover páginas menos usadas al archivo de paginación cuando la RAM está llena.

3. **Mapeo de Archivos**: Permite acceder al contenido de archivos como si fueran parte de la memoria.

4. **Reserva y Compromiso de Memoria**: Reservar memoria significa asignar direcciones sin respaldarla físicamente. Comprometer memoria implica respaldarla con RAM o el archivo de paginación.

## Administración del Archivo de Paginación

El archivo de paginación (pagefile.sys) permite que el sistema siga funcionando cuando la RAM está llena, evitando errores de falta de memoria. Su tamaño se puede configurar automáticamente o manualmente.
