# Preguntas sobre Memoria y Sistemas Operativos

## 1. Diferencia entre fragmentación interna y externa

**Fragmentación Interna:**  
Ocurre cuando se asigna más memoria de la necesaria porque los bloques tienen un tamaño fijo. Por ejemplo, si un programa necesita 3 MB y el bloque es de 4 MB, se pierde 1 MB.

- **Consecuencia:** Se desperdicia espacio dentro de los bloques, lo que reduce la memoria disponible para otros programas.

**Fragmentación Externa:**  
Pasa cuando hay memoria suficiente, pero está repartida en pedazos pequeños no continuos. Esto hace que no se puedan usar esos espacios para programas que necesitan bloques grandes.

- **Consecuencia:** El sistema tiene problemas para asignar memoria y puede ser más lento al tener que reorganizar (compactar) la memoria.

## 2. Políticas de reemplazo de páginas

Cuando la RAM se llena, el sistema necesita decidir qué páginas sacar para liberar espacio. Estas son las políticas más comunes:

1. **FIFO (First in-First Out):**  
   Reemplaza la página que lleva más tiempo en memoria. Es fácil de usar, pero puede sacar páginas que todavía se necesitan.

2. **LRU (Least Recently Used):**  
   Reemplaza la página que lleva más tiempo sin usarse. Es eficiente porque normalmente las páginas que no se usan en mucho tiempo no se necesitarán pronto.

3. **OPT (Optimal):**  
   Reemplaza la página que no se usará por más tiempo en el futuro. Es la mejor en teoría, pero no se puede usar en la vida real porque no podemos saber qué páginas se usarán.

4. **Clock (Second Chance):**  
   Es una mejora de FIFO. Si una página todavía se usa, no se reemplaza de inmediato, sino que se le da una segunda oportunidad.

**¿Cuál es mejor?**  
La más práctica es LRU, porque imita el uso real de las páginas. Aunque OPT sería ideal, no es posible porque el sistema no puede predecir el futuro.
