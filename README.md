# proyecto-final
Este proyecto es un sistema modular en Python que permite gestionar registros, almacenarlos de forma persistente y proteger el acceso mediante una **Contraseña Maestra** y validaciones de seguridad.

##  Estructura del proyecto

El ZIP contiene los siguientes módulos:

- **main.py**  Punto de entrada del programa; maneja los menús y el flujo general.
- **gestion_datos.py**  Funciones para crear, buscar, editar y eliminar registros.
- **persistencia.py**  Manejo de archivos, carga y guardado seguro de datos.
- **seguridad.py** Validación de la contraseña maestra y verificación de políticas de seguridad.
- **analisis.py**  Módulo opcional para análisis de datos registrados.
- **utilidades.py**  Funciones auxiliares comunes para todo el proyecto.

---

## Instrucciones de Uso

1. **Ejecutar el archivo principal**
   ```bash
   python main.py
   ```

2. **Configurar la Contraseña Maestra**
   - La primera vez que se inicia, se pedirá crear una Contraseña Maestra.
   - Esta será requerida en futuras ejecuciones.

3. **Menú Principal**
   Una vez dentro del sistema podrás:
   - Agregar un nuevo registro
   - Buscar registros existentes
   - Editar información
   - Eliminar registros
   - Analizar datos (si el módulo lo permite)
   - Guardar cambios y salir

4. **Estructura de un registro**
   Normalmente contiene:
   - Usuario
   - Correo
   - Fecha de creación
   - Datos específicos definidos por el usuario

5. **Persistencia**
   - Los datos se guardan automáticamente en un archivo llamado `boveda.dat`.
   - Si el archivo está corrupto, el sistema creará uno nuevo.

---

##  Casos de Prueba

### ✔ Caso 1: Crear un registro válido
**Entrada:**
- Usuario: `carlos23`
- Correo: `carlos23@mail.com`

**Resultado esperado:**
- Registro guardado exitosamente.
- Fecha asignada automáticamente.

---

###  Caso 2: Búsqueda de un registro existente
**Entrada:**
- Buscar por usuario: `carlos23`

**Resultado esperado:**
- Se muestra la información completa del registro.

---

###  Caso 3: Intento de creación de registro con campos vacíos
**Entrada:**
- Usuario: `""`
- Correo: `correo@mail.com`

**Resultado esperado:**
- Mensaje de advertencia: "Los campos no pueden estar vacíos."

---

###  Caso 4: Contraseña Maestra incorrecta
**Entrada:**
- Se ingresa una contraseña errónea 3 veces.

**Resultado esperado:**
- Bloqueo temporal con mensaje: "El sistema ha sido bloqueado por fallos de Contraseña Maestra."

---

###  Caso 5: Archivo corrupto
**Entrada:**
- `boveda.dat` modificado manualmente.

**Resultado esperado:**
- Mensaje de error y creación de nueva bóveda vacía.

---

##  Notas finales
- Todo el proyecto está modularizado.



