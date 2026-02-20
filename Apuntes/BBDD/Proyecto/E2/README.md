# Entrega 2 - Bases de datos IIC2413

### Datos del Alumno
| **Nombre Completo** | **Número de Alumno** |
|---------------------|----------------------|
| Gonzalo Balladares  |             2262595J |


### Credenciales de acceso

| **Usuario Uc**                  | **Valor** |
|---------------------------------|-----------|
| gballadaresv.uc@bdd1.ing.puc.cl | 2262595J  |


### Restricciones de integridad


#### 1. Persona, Empleado y Usuario

- La llave primaria en __Persona__ es __correo__ ya que según se menciona en el enunciado, las personas se identifican por su correo, lo mismo es cierto para __Empleado__ y __Usuario__, que heredan de __Persona__, con lo que dicho atributo es tanto llave primaria como llave foránea.

- También se menciona que __username__ debe ser único, con lo que se agregó una restricción de unicidad a dicho atributo para las 3 entidades.

- Los atributos __run__ y __dv__ se agregaron restricciones de unicidad, pues se indica que no pueden ser nulos.

- Para __Empleado__ adicionalmente se considera el atributo __isapre__ como no nulo.

#### 2. Agenda

- Se utiliza su __id__ como llave primaria.

- Tiene __correo_usuario__ como llave foránea referenciando a la tabla de __Usuario__.

#### 3. Reserva

- Se utiliza su __id__ como llave primaria.

- Se hace una distinción si las reservas están tomadas o no, si la reserva no está disponible, se exige que __id__, __fecha__ y __cantidad_personas__ no sean nulos, así como también se pide que __monto__ y __puntos__ sean valores enteros positivos. Finalmente se utiliza como llave foránea __agenda_id__ para validar la existencia del id de agenda en su respectiva tabla.

- En el caso que la reserva esté disponible, se verifica de igual manera que __id__ sea no nulo, y además se verifica por consistencia que __puntos__ sea 0 y que __agenda_id__ sea efectivamente nulo.


#### 4. Seguro

- Como llave primaria de __Seguro__ se genera __id__ como atributo serial.

- Se verifica que __correo_usuario__ sea no nulo y exista en la tabla __Usuario__.

- Se verifica que __reserva_id__ sea único y exista en la tabla __Reserva__.

- Se verifica que __tipo__, __clausula__, __empresa__ y __valor__ sean no nulos, y que este último sea entero positivo.

#### 5. Review

- Como llave primaria de __Review__ se genera __id__ como atributo serial.

- Se verifica que __correo_usuario__ sea no nulo y exista en la tabla __Usuario__.

- Se verifica que __reserva_id__ sea único y exista en la tabla __Reserva__.

- Se verifica que __estrellas__ sea no nulo y sea un valor entero entre 0 y 5 inclusive.

#### 6. Panorama

- Al heredar de __Reserva__, __id__ es tanto llave primaria como llave foránea.

- Al heredar de __Reserva__ se mantienen todas las validaciones asociadas.

- Además, se valida que __nombre__, __fecha__, __duracion__ y __precio_persona__ sean no nulos, y que este último sea un entero positivo.

#### 6. Participante

- Se utiliza como primary key una llave compuesta dada por __id_panorama__ y __nombre__

- Se verifica que __id_panorama__ sea no nulo y exista en __Reserva__.

- Se verifica que __nombre__ sea no nulo y que __edad__ sea un entero positivo.

#### 7. Hospedaje

- Al heredar de __Reserva__, se mantienen las restricciones y llaves primarias propias de dicha entidad.

- Se verifica que __ubicacion__, __precio_noche__, __estrellas__ y __fecha_checkin__ sean no negativos.

- Adicionalmente, se verifica que __precio_noche__ esa entero positivo y __estrellas__ sea un número entero entre 0 y 5 inclusive.

#### 8. Airbnb

- Al heredar de __Hospedaje__, se mantienen las restricciones y llaves primarias propias de dicha entidad.

- Adicionalmente, se exige que todos los atributos propios de __Airbnb__ sean no nulos, esto incluye __nombre_anfitrion__, __contacto_anfitrion__, __descripcion__, __piezas__, __camas__ y __banos__.

- Finalmente, se verifica que __piezas__, __camas__ y __banos__ sean numeros enteros no negativos.

#### 9. Hotel

- Al heredar de __Hospedaje__, se mantienen las restricciones y llaves primarias propias de dicha entidad.

- Se verifica que __politicas__ sea no nulo.

#### 10. Habitacion

- Se utiliza como primary key una llave compuesta dada por __id_hotel__ y __numero_habitacion__.

- Se verifica que __id_hotel__ y __numero_habitacion__ sean no nulos.

#### 11. Transporte

- Al heredar de __Reserva__, se mantienen las restricciones y llaves primarias propias de dicha entidad.

- Se verifica que __tiempo_estimado__, __fecha_salida__ y __precio_asiento__ sean no nulos, y que este ultimo sea mayor a 0.

- Se verifica que __correo_empleado__ exista en la tabla __Empleado__.

#### 12. Tren

- Al heredar de __Transporte__, se mantienen las restricciones y llaves primarias propias de dicha entidad.

- Se verifica que __paradas__ sea no nulo.

#### 13. Bus

- Al heredar de __Transporte__, se mantienen las restricciones y llaves primarias propias de dicha entidad.

- Se verifica que __tipo__ sea no nulo.

#### 14. Avion

- Al heredar de __Transporte__, se mantienen las restricciones y llaves primarias propias de dicha entidad.

- Se verifica que __clase__ y __escalas__ sean no nulos.
