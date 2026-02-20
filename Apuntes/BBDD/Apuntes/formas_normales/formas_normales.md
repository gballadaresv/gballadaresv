### Redundancia en los datos

Información redundante en las bbdd puede generar:
- Info redundante.
- Anomalías al modificar.
- Anomalías al insertar.
- Anomalías al eliminar.

Como solución se pueden separar las tablas (dependencia funcional).

Para eliminar anomalías minimizando redundancias, se deben averiguar las dependencias q se aplican, y descomponer las tablas en tablas más pequeñas.

### Formas normales

- 1NF: Ningún atributo tiene relaciones como elementos.
- 2NF: 1NF y ninguna llave candidata es funcionalmente dependiente de otra llave candidata.
- 3NF: Para toda dependencia funcional no trivial X -> Y, X es una superllave o Y es parte de una llave minimal.

Algoritmo para 3NF:
1. Para cada dpendencia funcional X -> Y se genera una tabla con esquema X U Y.
2. Si los esquemas resultantes R_1, ..., R_n no tienen una llave de la tabla R, agregar una.

### Relación BCNF

No puedo tener dependencias de cosas que no son llaves.