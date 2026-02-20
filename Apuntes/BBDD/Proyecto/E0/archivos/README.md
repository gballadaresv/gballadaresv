# Entrega 0 - Bases de datos IIC2413

**Nombre:** Gonzalo Andrés Balladares Velásquez
**Número de Alumno:** 2262595J
### Credenciales de acceso
**Usuario Uc** gballadaresv.uc@bdd1.ing.puc.cl
**Contraseña** 2262595J


## Contenido del Informe

### 1. Análisis de los datos entregados en los archivos

- Archivo `funciones.php`: Contiene las funciones utilizadas para formatear los datos solicitados.
- Archivo `main.php`: Recibe los datos y llama a als funciones de `funciones.php`.
- Archivo `empleados_rescatados.csv`: Contiene los datos rescatados de los empleados.
- Archivo `usuarios_rescatados.csv`: Contiene los datos rescatados de los usuarios.
- Archivo `personasOK.csv`: Contiene los datos limpiados relativos a todas las personas, se guardan sólo si contiene un correo válido, run y número de teléfono.
- Archivo `usuariosOK.csv`: Contiene los datos limpiados relacionados a los usuarios, se guardan bajo los mismos criterios que en `personasOK.csv`.
- Archivo `empleadosOK.csv`: Contiene los datos limpiados relacionados a los empleados, criterios similares a los de usuario, pero además se verifica que tenga contraseña.
- Archivo `agendaOK.csv`: Contiene todos los datos limpiados relacionados a las agendas, se guarda si tiene correo y código de agenda.
- Archivo `reservasOK.csv`: Contiene todos los datos limpiados relacionados las reservas, debe tener código de reserva y monto.
- Archivo `trasportesOK.csv`: Contiene todos los datos limpiados relacionados a los transportes, se revisa que tenga asociado un correo, código de reserva, número de viaje y monto.
- Archivo `busesOK.csv`: Contiene los datos limpiados de los buses, similar a transportes, pero debe tener tipo de bus.
- Archivo `trenes.csv`: Contiene los datos limpiados de los trenes, similar a transportes, pero debe tener estaciones.
- Archivo `aviones.csv`: Contiene los datos limpiados de los aviones, similar a transportes, pero debe tener clase.
- Archivo `datos_descartados_usuarios.csv`: Contiene los datos de usuarios que fueron descartados, se descartan la tupla si sus datos no sirven en ningún otro archivo.
- Archivo `datos_descartados_empleados.csv`: Contiene los datos de empleados que fueron descartados, se descarta la tupla si sus datos no sirven en ningún otro archivo.




### 2. Tipos de errores de datos detectados por el programa y forma de solución utilizada

Archivo `usuarios_rescatados.csv`:
- Dv faltantes: Debido a las reglas de negocio, el dígito verificador debe ser no nulo.
    - Solución: Se calculó el Dv a partir del run.

- Run faltantes: Debido a las reglas de negocio, no se admiten tuplas con run nulo.
    - Solución: En tuplas con run faltante, se inserto el run `00000000` que representa un run nulo.

- Correos inválidos o faltantes: Los correos deben seguir un formato en específico.
    - Solución: Si había un correo inválido o faltante, se guardaba el correo `invalido@null.nill` que representa un correo nulo o inválido.

- Teléfonos de contacto inválidos o faltantes: Los números de teléfono deben seguir un formato en específico.
    - Solución: Se formatearon los números de teléfono a un formato estándar válido, si una tupla no tenía teléfono de contacto, se insertaba el número `+00 0 0000 0000` que representa un número nulo.

- Códigos de agenda faltantes: Según las reglas de negocio, en el archivo de usuarios no podían haber códigos de agenda nulos.
    - Solución: A las tuplas que carecían de código de agenda se les asignó el valor `00000` que representa un código de agenda nulo.

- Montos negativos: Se encontraron montos con valores negativos.
    - Solución: Se guardó el mismo valor del monto, con valor positivo, si no había monto se guardaba con valor 0.

- Fechas con formato incorrecto: Se encontraron fechas que no estaban el en formato solicitado.
    - Solución: Se formateó el formato de las fechas según las reglas de negocio.


Archivo `empleados_rescatados.csv`:
- Dv faltantes: Debido a las reglas de negocio, el dígito verificador debe ser no nulo.
    - Solución: Se calculó el Dv a partir del run.

- Run faltantes: Debido a las reglas de negocio, no se admiten tuplas con run nulo.
    - Solución: En tuplas con run faltante, se inserto el run `00000000` que representa un run nulo.

- Correos inválidos o faltantes: Los correos deben seguir un formato en específico.
    - Solución: Si había un correo inválido o faltante, se guardaba el correo `invalido@null.nill` que representa un correo nulo o inválido.

- Teléfonos de contacto inválidos o faltantes: Los números de teléfono deben seguir un formato en específico.
    - Solución: Se formatearon los números de teléfono a un formato estándar válido, si una tupla no tenía teléfono de contacto, se insertaba el número `+00 0 0000 0000` que representa un número nulo.

- Reservas nulas: Se encontraron tuplas sin código de reserva siendo que no admiten nulos.
    - Solución: Se le asignó el código de reserva `000000` que representa un código nulo.

- Fechas con formato incorrecto: Se encontraron fechas que no estaban el en formato solicitado.
    - Solución: Se formateó el formato de las fechas según las reglas de negocio.

- Montos negativos: Se encontraron montos con valores negativos.
    - Solución: Se guardó el mismo valor del monto, con valor positivo, si no había monto se guardaba con valor 0.

- Números de viaje nulos: Se encontraron números de viaje nulos, cuando las reglas de negocio no lo admite.
    - Solución: Se le asignó el número de viaje `0` que representa nulo.


### 3. Nombre de los archivos de salida y explicación de su contenido
En esta sección se deben listar los archivos generados por el programa y describir su contenido. Por ejemplo:

- Archivo `usuarios_rescatados.csv`: contiene los datos de los usuarios antes de la limpieza.
- Archivo `empleados_rescatados.csv`: contiene los datos de los empleados antes de la limpieza.
- Archivo `personasOK.csv`: contiene los datos de las personas después de la limpieza, con las columnas de `nombre`, `run`, `dv`, `correo`, `contrasena`, `nombre_usuario` y `telefono_contacto`.
- Archivo `usuariosOK.csv`: contiene los datos de usuarios después de la limpieza, con las mismas columnas del archivo de personas, y `puntos`.
- Archivo `empleadosOK.csv`: contiene los datos de los empleados después de la limpieza, con las mismas columnas del archivo de personas, y `jornada`, `isapre` y `contrato`.
- Archivo `agendaOK.csv`: contiene los datos de las agendas después de la limpieza, con las columnas de `correo_usuario`, `codigo_agenda` y `etiqueta`.
- Archivo `transporteOK.csv`: contiene los datos de los transportes después de la limpieza, con las columnas de `correo_empleado` ,`codigo_reserva`, `numero_viaje`,  `lugar_origen`, `lugar_llegada`, `capacidad`, `tiempo_estimado`, `precio_asiento`, `empresa`, `fecha_salida` y `fecha_llegada`.
- Archivo `avionesOK.csv`: contiene los datos de los aviones después de la limpieza, con los mismos datos del archivo de transportes, y `escalas` y `clase`.
- Archivo `busesOK.csv`: contiene los datos de los buses después de la limpieza, con los mismos datos del archivo de transportes, y `tipo_de_bus` y `comodidades`.
- Archivo `trenesOK.csv`: contiene los datos de los trenes después de la limpieza, con los mismos datos del archivo de transportes, y `comodidades` y `paradas`.
- Archivo `datos_descartados_usuarios`: contiene los datos de los usuarios que están tan dañados que no pudo rescatarse para ningún archivo, tiene las mismas columnas que el de usuarios rescatados.
- Archivo `datos_descartados_empleados`: contiene los datos de los empleados que están tan dañados que no pudo rescatarse para ningún archivo, tiene las mismas columnas que el de empleados rescatados.
- Archivo `funciones.php`: contiene funciones usadas para formatear los datos en el archivo principal.
- Archivo `main.php`: es el archivo principal, con este ejecutamos el programa para la limpieza de datos. 

### 4. Instrucciones para ejecutar el programa
Es fundamental proporcionar instrucciones claras para ejecutar el programa (absolutamente todos los pasos necesarios, como si fueras a ejecutarlo de cero). Por ejemplo:

1. Credenciales para conectar al servidor:
    usuario: gballadaresv
    contraseña: 2262595J
2. Conexión al servidor mediante ssh:
    ejecutar el comando ssh gballadaresv@bdd1.ing.puc.cl
    colocar contraseña
3. Ejecutar el archivo main.php
    dirigirse a ./Sites/E0/archivos/
    ejecutar el comando: php main.php
    esperar a que termine el proceso
