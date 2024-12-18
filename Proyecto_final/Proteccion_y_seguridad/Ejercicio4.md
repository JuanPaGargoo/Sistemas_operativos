# **Qué es una Matriz de Acceso**

## **Diseño de la Matriz de Acceso**

Una matriz de acceso es una tabla que muestra qué permisos tiene cada usuario sobre los recursos de un sistema. Los usuarios están en las filas y los recursos en las columnas. Los permisos pueden ser **leer (R)**, **escribir (W)**, **ejecutar (X)** o no tener acceso (**-**).

### **Ejemplo de Matriz de Acceso**

| **Usuario \ Recurso** | **Recurso 1** | **Recurso 2** | **Recurso 3** | **Recurso 4** |
| --------------------- | ------------- | ------------- | ------------- | ------------- |
| **Usuario 1**         | R, W          | R             | -             | R, W, X       |
| **Usuario 2**         | R             | R, W          | X             | -             |
| **Usuario 3**         | -             | -             | R, X          | R             |

### **Explicación de la Matriz**

- **Usuario 1** puede leer y escribir en el Recurso 1, solo leer el Recurso 2, no tiene acceso al Recurso 3, y puede leer, escribir y ejecutar el Recurso 4.
- **Usuario 2** puede leer el Recurso 1, leer y escribir en el Recurso 2, ejecutar el Recurso 3, y no tiene acceso al Recurso 4.
- **Usuario 3** no tiene acceso al Recurso 1 ni al Recurso 2, pero puede leer y ejecutar el Recurso 3 y solo leer el Recurso 4.

---

## **Cómo se Usa la Matriz para Controlar el Acceso**

El sistema operativo usa la matriz de acceso para decidir si un usuario puede hacer algo con un recurso. Cuando un usuario pide acceso, el sistema sigue estos pasos:

1. **Identificación del Usuario**: El sistema identifica quién es el usuario (por ejemplo, con un nombre de usuario y contraseña).
2. **Verificación del Recurso**: El sistema identifica qué recurso quiere usar el usuario.
3. **Consulta de la Matriz de Acceso**: El sistema busca la intersección de la fila del usuario y la columna del recurso.
4. **Decisión de Acceso**: El sistema decide si permite o no la acción dependiendo de los permisos que estén en la matriz.

Este proceso ocurre de forma rápida cada vez que un usuario intenta acceder a un recurso.

---

## **Simulación de Acceso No Permitido**

### **Escenario**

El **Usuario 3** intenta **escribir** en el **Recurso 2**.

1. **Identificación**: El sistema identifica al solicitante como **Usuario 3**.
2. **Verificación del Recurso**: El sistema verifica que el recurso solicitado es el **Recurso 2**.
3. **Consulta de la Matriz de Acceso**: Se busca la intersección entre la fila del **Usuario 3** y la columna del **Recurso 2**. Según la matriz, el valor es **-**, lo que significa que el usuario no tiene acceso a este recurso.
4. **Acción del Sistema**: El sistema bloquea la acción y muestra un mensaje de error al usuario.

### **Mensaje del Sistema**

```
Error: No tienes permisos para escribir en el Recurso 2.
```
