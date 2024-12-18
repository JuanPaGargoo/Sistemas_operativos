**Validación y Amenazas al Sistema**

**1. Tipos de Amenazas Comunes**

1. **Malware**

   - **Qué es**: Son programas dañinos que buscan causar problemas en la computadora o robar información. Algunos ejemplos son los virus, los gusanos y los troyanos.
   - **Por qué es peligroso**: Puede borrar archivos, robar contraseñas, controlar la computadora a distancia o mostrar anuncios no deseados.
   - **Ejemplo**: Un troyano puede parecer un juego, pero cuando se instala, permite que otra persona controle la computadora de forma remota.

2. **Ataques de Fuerza Bruta**

   - **Qué es**: Es un método en el que se intentan muchas combinaciones de contraseñas hasta encontrar la correcta.
   - **Por qué es peligroso**: Los atacantes pueden entrar en cuentas privadas o acceder a archivos protegidos.
   - **Ejemplo**: Usar un programa automático que prueba miles de contraseñas hasta acertar.

3. **Inyección de Código**

   - **Qué es**: Consiste en introducir instrucciones maliciosas en un sistema para que realice tareas no autorizadas.
   - **Por qué es peligroso**: Los atacantes pueden robar información, modificar bases de datos o tomar control del sistema.
   - **Ejemplo**: Escribir código malicioso en un formulario web para que la base de datos muestre información privada.

**2. Mecanismos de Validación**

1. **Autenticación Multifactor (MFA)**

   - **Qué es**: Se requiere más de una forma de identificarse para entrar a un sistema, no solo la contraseña.
   - **Cómo funciona**:
     - **Algo que sabes**: Contraseña o código PIN.
     - **Algo que tienes**: Código en tu teléfono o una tarjeta especial.
     - **Algo que eres**: Huella dactilar o reconocimiento facial.
   - **Por qué es útil**: Si alguien roba la contraseña, no podrá entrar sin el otro factor de autenticación.

2. **Control de Integridad**

   - **Qué es**: Asegura que los archivos y datos no se modifiquen sin permiso.
   - **Cómo funciona**:
     - **Hash**: Se calcula un "código único" para cada archivo. Si el archivo cambia, el código también.
     - **Firmas digitales**: Sirven para verificar que un archivo es original y no ha sido modificado.
     - **Listas de acceso**: Se define quién puede ver o cambiar archivos importantes.
   - **Por qué es útil**: Permite detectar cambios no autorizados en archivos importantes.

**3. Esquema de Validación para un Sistema Operativo con Múltiples Usuarios**

1. **Acceso de Usuario**

   - **Qué se necesita**: Los usuarios deben identificarse antes de acceder al sistema.
   - **Cómo se hace**:
     - **Autenticación Multifactor (MFA)**: Contraseña y un código generado por una app o mensaje de texto.
     - **Autenticación biométrica**: Usar huellas dactilares o reconocimiento facial.

2. **Control de Acceso por Roles (RBAC)**

   - **Qué es**: Cada usuario tiene un rol (administrador, usuario, invitado) que define lo que puede o no hacer.
   - **Cómo funciona**:
     - Los administradores pueden hacer más cosas que los usuarios normales.
     - Los invitados tienen menos permisos, como solo ver archivos.

3. **Protección de Archivos Críticos**

   - **Qué se necesita**: Los archivos importantes deben estar protegidos contra cambios no autorizados.
   - **Cómo se hace**:
     - **Verificación de archivos**: Se revisa que los archivos críticos no hayan cambiado.
     - **Acceso restringido**: Solo los administradores pueden modificar archivos esenciales.

4. **Monitoreo de la Actividad del Usuario**

   - **Qué es**: Se registran las acciones de los usuarios en el sistema.
   - **Cómo funciona**:
     - **Registros de eventos**: Se anota cada vez que un usuario abre un archivo o accede al sistema.
     - **Análisis de comportamiento**: Se detectan comportamientos extraños, como intentar iniciar sesión muchas veces.

5. **Acciones en Caso de Problema**

   - **Qué hacer**:
     - **Bloqueo de la cuenta**: Si hay muchos intentos fallidos de inicio de sesión, la cuenta se bloquea temporalmente.
     - **Alertas**: Se avisa a los administradores sobre posibles ataques.
     - **Acceso de emergencia**: Se tienen cuentas especiales para emergencias y recuperar el sistema.
