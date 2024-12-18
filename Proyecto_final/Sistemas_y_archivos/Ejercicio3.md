**Organización Lógica y Física de Archivos**

**1. Árbol Jerárquico de la Organización Lógica de Archivos**

La organización lógica de archivos es una forma de organizar y clasificar los archivos en carpetas y subcarpetas, similar a un árbol con muchas ramas. La parte más alta de este árbol se llama "raíz" (root) y de ella se desprenden varias carpetas principales.

**Ejemplo de estructura de carpetas:**

```
Raíz (/)
├── home
│   ├── usuario1
│   │   ├── documentos
│   │   │   ├── trabajo.docx
│   │   ├── fotos
│   │       ├── vacaciones.jpg
│   ├── usuario2
│       ├── descargas
│           ├── software.zip
├── var
│   ├── log
│   │   ├── system.log
│   ├── www
│       ├── index.html
├── etc
│   ├── config.conf
├── bin
    ├── bash
    ├── ls
```

En esta estructura, la raíz ("/") contiene las carpetas principales como `/home`, `/var`, `/etc` y `/bin`. Dentro de estas carpetas hay subcarpetas y archivos.

---

**2. Cómo se traduce la dirección lógica a la dirección física**

Aunque la estructura lógica parece sencilla, la forma en que los archivos se almacenan en el disco es diferente. Los sistemas de archivos (FAT32, NTFS, ext4, etc.) se encargan de convertir la dirección lógica (como `/home/usuario1/documentos/trabajo.docx`) en una ubicación real en el disco duro.

**Cómo funciona este proceso:**

1. **Ruta Lógica**: Se busca el archivo usando su ruta, por ejemplo, `/home/usuario1/documentos/trabajo.docx`.
2. **Sistema de Archivos**: El sistema de archivos consulta una "tabla de ubicaciones" para saber en qué parte del disco está el archivo.
3. **Inodo o Entrada de la Tabla**: Se usa una especie de "identificador" que indica dónde se guardó el archivo en el disco.
4. **Ubicación Física**: Se encuentran los bloques o sectores específicos del disco donde está la información.

**Ejemplo práctico:**

- Ruta Lógica: `/home/usuario1/documentos/trabajo.docx`
- El sistema encuentra que el archivo está guardado en los sectores 100, 101 y 150 del disco duro.

---

**3. Ejemplo práctico de almacenamiento de un archivo**

Imaginemos que tenemos un archivo llamado `trabajo.docx` con un tamaño de 10 KB. El sistema de archivos (por ejemplo, ext4) usa bloques de 4 KB para almacenar la información.

**Paso 1: Creación de la entrada de inodo**

- Se crea un "inodo" para el archivo `trabajo.docx`, que contiene información importante, como:
  - Nombre del archivo: trabajo.docx
  - Tamaño: 10 KB
  - Fecha de creación y modificación.
  - Ubicación de los bloques: [34, 35, 78]

**Paso 2: Asignación de los bloques de disco**

- El archivo ocupa 10 KB. Como cada bloque tiene 4 KB, se necesitan 3 bloques.
  - Bloque 34 (4 KB)
  - Bloque 35 (4 KB)
  - Bloque 78 (2 KB)

**Paso 3: Escritura de los datos en los bloques**

- Los primeros 4 KB de `trabajo.docx` se escriben en el bloque 34.
- Los siguientes 4 KB se escriben en el bloque 35.
- Los últimos 2 KB se escriben en el bloque 78.

**Paso 4: Relación entre dirección lógica y física**

- Ruta lógica: `/home/usuario1/documentos/trabajo.docx`
- Dirección física: Bloques 34, 35 y 78 en el disco.
