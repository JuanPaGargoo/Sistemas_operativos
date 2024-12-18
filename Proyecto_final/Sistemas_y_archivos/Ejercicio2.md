**Componentes de un sistema de archivos**

**1. Componentes Clave de un Sistema de Archivos**

Un sistema de archivos se encarga de organizar, almacenar, acceder y controlar los datos en dispositivos como discos duros y memorias USB. Los componentes principales de un sistema de archivos son:

1. **Estructura de Directorios**: Es la forma en que los archivos y carpetas se organizan en una estructura de árbol con directorios (carpetas) y subdirectorios.
2. **Bloques de Datos**: Son las partes donde se guarda la información de los archivos. Cada archivo se divide en bloques.
3. **Metadatos**: Información que describe cada archivo, como su nombre, tamaño, permisos y la fecha de modificación.
4. **Tablas de Asignación de Archivos**: Mapa que indica cuáles bloques están ocupados y a qué archivos pertenecen.
5. **Gestor de Espacio Libre**: Sistema que controla cuáles bloques de almacenamiento están disponibles para ser usados.
6. **Registro de Transacciones (Journal)**: Registro de cambios para ayudar a recuperar el sistema en caso de fallos o errores.

---

**2. Cuadro Comparativo: EXT4 vs NTFS**

| **Componente**                | **EXT4 (Linux)**                                                  | **NTFS (Windows)**                                                           |
| ----------------------------- | ----------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **Estructura de Directorios** | Se organiza como un árbol con carpetas y subcarpetas.             | Usa la MFT (Master File Table) para organizar carpetas y archivos.           |
| **Bloques de Datos**          | Usa bloques de 4KB por defecto.                                   | Usa clústeres de tamaño variable.                                            |
| **Metadatos**                 | Usa "inodos" para guardar la información de los archivos.         | Los metadatos se guardan en la MFT.                                          |
| **Tablas de Asignación**      | Usa un mapa de bits para controlar los bloques ocupados y libres. | La MFT también gestiona la asignación de archivos y carpetas.                |
| **Gestor de Espacio Libre**   | Usa un mapa de bits para ver cuáles bloques están libres.         | Los registros en la MFT controlan el espacio disponible.                     |
| **Registro de Transacciones** | Usa un registro de cambios para proteger la información.          | Usa un sistema de registro de transacciones para prevenir pérdidas de datos. |

---

**3. Ventajas y Desventajas de EXT4 y NTFS**

| **Aspecto**     | **EXT4**                                            | **NTFS**                                                 |
| --------------- | --------------------------------------------------- | -------------------------------------------------------- |
| **Ventajas**    | - Rápido en lectura y escritura.                    | - Compatible con la mayoría de los dispositivos Windows. |
|                 | - Soporta archivos de hasta 16TB.                   | - Ofrece más seguridad con cifrado de archivos.          |
|                 | - Registro de cambios eficiente.                    | - Registro de transacciones más avanzado.                |
| **Desventajas** | - No es compatible con Windows sin programas extra. | - Puede ser más lento que EXT4 en algunas tareas.        |
|                 | - Tamaño máximo de archivo menor.                   | - Más complejo, con mayor carga de metadatos.            |
