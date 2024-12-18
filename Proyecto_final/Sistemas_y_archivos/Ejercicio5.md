**Modelo jerárquico y mecanismos de recuperación en caso de falla**

---

**1. Modelo jerárquico para un sistema de archivos**

Un sistema de archivos se organiza de forma jerárquica, con carpetas que contienen otras carpetas y archivos. Este es un ejemplo con tres niveles de carpetas:

```
/ (Raíz)
|
|--- /home
|    |
|    |--- /usuario1
|    |     |
|    |     |--- /documentos
|    |     |     |--- archivo1.txt
|    |     |     |--- archivo2.docx
|    |     |
|    |     |--- /imagenes
|    |           |--- imagen1.jpg
|    |           |--- imagen2.png
|    |
|    |--- /usuario2
|          |
|          |--- /documentos
|          |     |--- reporte.pdf
|          |
|          |--- /videos
|                |--- video1.mp4
|                |--- video2.mkv
|
|--- /var
|    |
|    |--- /log
|    |     |--- system.log
|    |     |--- error.log
|    |
|    |--- /backup
|          |--- respaldo_20231212.tar.gz
|
|--- /etc
     |
     |--- /config
     |     |--- sistema.conf
     |     |--- usuario.conf
     |
     |--- /seguridad
           |--- firewall.rules
           |--- permisos.conf
```

En esta estructura, el directorio principal (/) tiene tres subdirectorios principales: **/home**, **/var**, y **/etc**. Cada uno de estos tiene subdirectorios adicionales que forman tres niveles o más.

---

**2. Simulación de una falla en el sistema**

**Escenario de la falla:**

- Ocurre una falla en la carpeta `/home/usuario1/documentos/` debido a un problema con el disco.
- Los archivos **archivo1.txt** y **archivo2.docx** se pierden o no se pueden abrir.

**Pasos para la recuperación:**

1. **Detectar la falla:**

   - Revisar los mensajes de error en el archivo de registros (`/var/log/error.log`).
   - Los usuarios informan que no pueden acceder a los archivos de `/home/usuario1/documentos/`.

2. **Aislar la falla:**

   - Usar la herramienta `fsck` para revisar si el disco tiene errores.
   - Identificar si el problema es lógico (error en el sistema de archivos) o físico (daño en el disco duro).

3. **Recuperar los archivos:**

   - Si el problema es lógico, usar herramientas como `extundelete` o `photorec` para recuperar archivos eliminados.
   - Si el problema es físico, usar `ddrescue` para copiar los sectores dañados y luego recuperar los archivos.

4. **Restaurar desde la copia de seguridad (backup):**

   - Si los archivos no se pueden recuperar, se usan los respaldos.
   - Se extrae la última copia de seguridad (`/var/backup/respaldo_20231212.tar.gz`).
   - Usar el comando `tar -xzvf respaldo_20231212.tar.gz -C /home/usuario1/` para restaurar los archivos.

5. **Verificar la recuperación:**

   - Comprobar que los archivos se pueden abrir y usar.
   - Probar el acceso a los archivos recuperados.

---

**3. Herramientas y técnicas de respaldo (backup)**

Para evitar la pérdida de datos, se recomienda usar una estrategia de respaldo que incluya estas herramientas y técnicas:

1. **Tipos de respaldo:**

   - **Respaldo completo:** Copia todo el sistema de archivos. Es más lento y ocupa más espacio, pero permite una recuperación rápida.
   - **Respaldo incremental:** Solo copia los archivos que cambiaron desde el último respaldo. Requiere menos espacio, pero la recuperación es más lenta.
   - **Respaldo diferencial:** Copia los archivos que cambiaron desde el último respaldo completo. Es más rápido que un respaldo completo, pero más lento que uno incremental.

2. **Herramientas de respaldo:**

   - **rsync**: Sincroniza archivos y carpetas entre computadoras.
   - **tar**: Empaqueta y comprime carpetas en un solo archivo, facilitando su almacenamiento y restauración.
   - **cron**: Automatiza tareas de respaldo en horarios definidos.
   - **dd**: Copia discos completos sector por sector.
   - **backupninja**: Configura tareas automáticas de respaldo.

3. **Frecuencia de los respaldos:**

   - **Diario:** Para archivos críticos que cambian con frecuencia.
   - **Semanal:** Para archivos de menos importancia.
   - **Mensual:** Para archivos antiguos o de referencia.

4. **Pruebas periódicas:**

   - Probar regularmente la restauración de los respaldos para asegurar que se puedan recuperar los archivos.

5. **Ubicación de los respaldos:**

   - Guardar copias de respaldo en otros lugares (como la nube) para protegerse contra desastres.

6. **Políticas de retención de datos:**

   - Decidir cuánto tiempo se guardarán los respaldos antes de eliminarlos.
