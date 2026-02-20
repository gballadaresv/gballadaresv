# Esquema

## Entidades

#### Personas

Persona(id(PK), nombre, correo, nombre_de_usuario, telefono_de_contacto, run, dv)

Usuario(P_id(PK, FK), P_correo, agenda, reserva, reseña, seguro)

Empleado(P_id(PK, FK), P_correo, jornada, contrato, isapre)

#### Agenda

Agenda(numero_agenda(PK), etiqueta)

#### Reserva

Reserva(numero_reserva(PK), fecha, monto, cantidad_de_personas, estado_disponibilidad)

Review(review_id(PK), estrellas, descripcion, reserva)

Transporte(transporte_id(PK), numero_reserva(FK), lugar_origen, lugar_llegada, capacidad, tiempo_estimado, precio_por_asiento, empresa, fecha_de_salida, fecha_de_llegada)

Panorama(panorama_id(PK), numero_reserva(FK), nombre, empresa, descripcion, ubicacion, duracion, precio_por_persona, capacidad_maxima, lista_de_restricciones, fecha)

Hospedaje(hospedaje_id(PK),  numero_reserva(FK), nombre, ubicacion, precio_por_noche, estrellas, comodidades, fecha_check_in, fecha_check_out)

Seguros(seguro_id(PK), valor, tipo, clausula, empresa)

Airbnb(H_id(PK, FK), nombre, numero_de_contacto, descripcion, cantidad_de_piezas, cantidad_de_camas, cantidad_de_baños)

Hotel(H_id(PK, FK), registro_de_habitaciones, tipo, normativa)

Tren(T_id(PK, FK), lista_de_comodidades, lista_de_paradas)

Bus(T_id(PK, FK), lista_de_comodidades, tipo)

Avion(T_id(PK, FK), clase, lista_de_escalas)


## Relaciones

<!-- Un usuario crea agendas -->
Crea(U_id, numero_agenda)

<!-- Un usuario toma reservas -->
Toma(U_id, numero_reserva)

<!-- Un usuario deja reviews -->
Deja(U_id, review_id)

<!-- Un usuario contrata seguros -->
Contrata(U_id, seguro_id)

<!-- Una agenda contiene multiples reservas -->
Contiene(numero_agenda, numero_reserva)

<!-- Un usuario deja reviews -->
Deja(U_id, review_id)

<!-- Una reserva tiene reviews -->
Tiene(numero_reserva, review_id)

<!-- Un seguro se asocia a una reserva -->
Asocia(numero_reserva, seguro_id)

<!-- 
Cambiar:
Registro de habitaciones en hotel,
Agregar entidad habitación,
Separar lista comodidades de bus y tren,
Separar lista_escalas de avion
-->