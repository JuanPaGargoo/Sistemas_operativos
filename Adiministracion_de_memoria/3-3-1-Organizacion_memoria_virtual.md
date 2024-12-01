# Paginación y Segmentación

## Paginación

La paginación es una técnica que divide la memoria en pequeños bloques de tamaño fijo, llamados páginas. La memoria física (RAM) también se divide en bloques del mismo tamaño, llamados marcos de página. Cada página de un proceso se almacena en un marco disponible, sin importar si los marcos están juntos o separados en la memoria.

### Ventajas de la Paginación

- **Elimina la fragmentación externa**: Los bloques son del mismo tamaño, por lo que la memoria se usa de manera eficiente.
- **Facilita la asignación de memoria**: Los procesos se dividen en páginas pequeñas, que se pueden ubicar en cualquier parte de la memoria disponible.

### Desventajas de la Paginación

- **Fragmentación interna**: Como los marcos tienen un tamaño fijo, puede haber espacio desperdiciado si el proceso no llena completamente una página.
- **Sobrecarga de tablas**: Cada proceso necesita una tabla que relacione sus páginas con los marcos de la memoria, lo que consume espacio adicional.

## Segmentación

La segmentación divide la memoria en segmentos de tamaño variable, cada uno representando una parte lógica del programa, como el código, los datos o la pila. Cada segmento tiene un tamaño diferente, y los procesos se dividen según su estructura lógica, no en partes iguales.

### Ventajas de la Segmentación

- **Mejor organización lógica**: Los segmentos representan partes lógicas del programa, lo cual hace que la memoria sea más fácil de gestionar desde el punto de vista del programador.
- **No hay fragmentación interna**: Como los segmentos tienen un tamaño variable, no hay espacio desperdiciado dentro de cada segmento.

### Desventajas de la Segmentación

- **Fragmentación externa**: Al tener segmentos de diferentes tamaños, es posible que queden huecos entre segmentos, lo que dificulta el uso eficiente de la memoria.
- **Complejidad de gestión**: Necesita una tabla de segmentos que contenga la dirección y el tamaño de cada segmento, lo cual puede complicar la gestión de la memoria.
