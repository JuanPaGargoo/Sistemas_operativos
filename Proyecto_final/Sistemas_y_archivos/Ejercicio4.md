**Mecanismos de acceso a los archivos**

**1. ¿Qué son los mecanismos de acceso a archivos?**

1. **Acceso secuencial**: Este tipo de acceso se usa para leer los archivos desde el principio hasta el final, uno por uno. Es como cuando lees un libro, avanzas de la primera página hasta la última. Se usa cuando necesitamos procesar todos los registros sin importar su orden.

2. **Acceso directo**: Este método permite ir directamente a un registro específico en el archivo. Es como si pudieras abrir un libro y saltar directamente a la página 50 sin tener que pasar por las 49 anteriores. Este tipo de acceso se usa cuando sabemos dónde está la información que necesitamos.

3. **Acceso indexado**: En este método, se usa un índice (parecido a un índice de un libro) que nos dice dónde está cada registro. De esta forma, no tenemos que buscar registro por registro. Este método es útil cuando necesitamos buscar información específica rápidamente.

---

**2. Cómo funcionan estos mecanismos?**

**Acceso secuencial**

```
inicio
    abrir_archivo("archivo.txt", "lectura")
    mientras no fin_de_archivo(archivo)
        registro = leer_siguiente_registro(archivo)
        imprimir(registro)
    fin_mientras
    cerrar_archivo(archivo)
fin
```

**Explicación:** Se abre el archivo para lectura y se leen los registros uno por uno hasta llegar al final del archivo.

---

**Acceso directo**

```
inicio
    posicion = 5  // Queremos ir al registro 5
    tamano_registro = obtener_tamano_registro(archivo)
    abrir_archivo("archivo.txt", "lectura")
    desplazar_cursor(archivo, posicion * tamano_registro) // Mueve el cursor a la posición deseada
    registro = leer_registro_actual(archivo)
    imprimir(registro)
    cerrar_archivo(archivo)
fin
```

**Explicación:** Este código nos permite saltar directamente al registro número 5. Se usa una fórmula que calcula dónde está el registro dentro del archivo.

---

**Acceso indexado**

```
inicio
    clave_busqueda = "12345"  // Queremos buscar un registro con esta clave
    abrir_archivo("indice.txt", "lectura")
    posicion = buscar_en_indice(clave_busqueda, archivo_indice) // Busca la posición en el índice
    si posicion != -1 entonces
        abrir_archivo("archivo.txt", "lectura")
        desplazar_cursor(archivo, posicion)
        registro = leer_registro_actual(archivo)
        imprimir(registro)
        cerrar_archivo(archivo)
    sino
        imprimir("Registro no encontrado")
    fin_si
    cerrar_archivo(archivo_indice)
fin
```

**Explicación:** Primero, se busca la clave en el índice. Si la clave existe, se va directamente a la posición indicada y se lee el registro.

---

**3. ¿Cuál es mejor?**

| **Característica**    | **Acceso Secuencial**              | **Acceso Directo**                          | **Acceso Indexado**                    |
| --------------------- | ---------------------------------- | ------------------------------------------- | -------------------------------------- |
| **Velocidad**         | Lento si el registro está al final | Rápido si se conoce la posición             | Muy rápido con el índice               |
| **Fácil de usar?**    | Sí, muy fácil                      | Necesitas calcular la posición              | Necesitas crear y mantener el índice   |
| **Memoria adicional** | No se necesita                     | No se necesita                              | Necesitas memoria para el índice       |
| **Cuándo usarlo?**    | Para procesar todo el archivo      | Para acceder rápido a registros específicos | Para buscar por claves de forma rápida |
