INSERT INTO Persona(nombre, correo, contrasena, username, telefono_contacto, run, dv)
VALUES
('Luca Brasi', 'luca@viajes.cl', 'luca123', 'lucabrasi', '+56 9 5678 9012', '20321987', '6'),
('Paulie Gatto', 'paulie@viajes.cl', 'piloto123', 'pauliegatto', '+56 9 4567 8901', '20654321', '2'),
('Lucas Viajero', 'lucas@edubus.cal', 'lucas123', 'lucasviajero', '+56 9 3456 7890', '20987654', '3');

INSERT INTO Empleado(jornada, isapre, contrato, nombre, correo, contrasena, username, telefono_contacto, run, dv)
VALUES
('Diurno', 'Colmena', 'Part time', 'Luca Brasi', 'luca@viajes.cl', 'luca123', 'lucabrasi', '+56 9 5678 9012', '20321987', '6'),
('Nocturno', 'Fonasa', 'Full time', 'Paulie Gatto', 'paulie@viajes.cl', 'piloto123', 'pauliegatto', '+56 9 4567 8901', '20654321', '2');

INSERT INTO Usuario(puntos, nombre, correo, contrasena, username, telefono_contacto, run, dv)
VALUES
(0, 'Lucas Viajero', 'lucas@edubus.cal', 'lucas123', 'lucasviajero', '+56 9 3456 7890', '20987654', '3');

INSERT INTO Agenda(id, correo_usuario, etiqueta)
VALUES
(66637, 'lucas@edubus.cal', 'Fin de semestre');

INSERT INTO Reserva(id, agenda_id, fecha, monto, cantidad_personas, estado_disponibilidad, puntos_booked)
VALUES
(69420, 66637, '2025-04-22', 4000, 12, 'No disponible', NULL),
(69421, 66637, '2025-04-22', 4500000, 12, 'No disponible', NULL),
(69422, 66637, '2025-04-22', 3864000, 12, 'No disponible', NULL),
(69423, 66637, '2025-04-22', 252000, 12, 'No disponible', NULL),
(69424, 66637, '2025-04-22', 324000, 12, 'No disponible', NULL),
(69425, 66637, '2025-08-02', 600000, 20, 'No disponible', NULL),
(69426, 66637, '2025-08-03', 500000, 20, 'No disponible', NULL),
(69427, 66637, '2025-08-04', 240000, 20, 'No disponible', NULL),
(69428, 66637, '2025-08-05', 200000, 20, 'No disponible', NULL);

INSERT INTO Airbnb(
    id, agenda_id, fecha, monto, cantidad_personas, estado_disponibilidad, puntos_booked,
    nombre, ubicacion, precio_noche, estrellas, fecha_checkin, fecha_checkout,
    nombre_anfitrion, contacto_anfitrion, descripcion, piezas, camas, banos
)
VALUES (
    69420, 66637, '2025-04-22', 4000, 12, 'No disponible', NULL,
    'La familia', 'Corleone, Sicilia', 1000, 5, '2025-08-02', '2025-08-06',
    'Connie Corleone', '+56 9 4532 7890', 'Clásica villa siciliana con vista al viñedo', 6, 12, 4
);

INSERT INTO Avion(
    id, agenda_id, fecha, monto, cantidad_personas, estado_disponibilidad, puntos_booked,
    correo_empleado, lugar_origen, lugar_llegada, capacidad, tiempo_estimado, precio_asiento, empresa,
    fecha_salida, fecha_llegada, clase, escalas
)
VALUES
(69421, 66637, '2025-04-22', 4500000, 12, 'No disponible', NULL, 'paulie@viajes.cl', 'Santiago', 'Palermo', 200, 1200, 375000, 'AeroPeor', '2025-08-01', '2025-08-01', 'Clase económica', '{Río, Casablanca}'),
(69422, 66637, '2025-04-22', 3864000, 12, 'No disponible', NULL, 'paulie@viajes.cl', 'Palermo', 'Santiago', 200, 1200, 322000, 'AeroPeor', '2025-08-06', '2025-08-06', 'Clase económica', '{Río, Casablanca}');

INSERT INTO Bus(
    id, agenda_id, fecha, monto, cantidad_personas, estado_disponibilidad, puntos_booked,
    correo_empleado, lugar_origen, lugar_llegada, capacidad, tiempo_estimado, precio_asiento, empresa,
    fecha_salida, fecha_llegada, comodidades, tipo
)
VALUES
(69423, 66637, '2025-04-22', 252000, 12, 'No disponible', NULL, 'luca@viajes.cl', 'Palermo', 'Corleone', 15, 120, 21000, 'Viaja con respeto', '2025-08-02', '2025-08-02', 'Aire acondicionado,Wi-Fi,Reclinables,Baño,Cargador USB', 'Semi-cama'),
(69424, 66637, '2025-04-22', 324000, 12, 'No disponible', NULL, 'luca@viajes.cl', 'Corleone', 'Palermo', 15, 120, 27000, 'Viaja con respeto', '2025-08-05', '2025-08-06', 'Aire acondicionado,Wi-Fi,Reclinables,Baño,Cargador USB', 'Semi-cama');

INSERT INTO Panorama(
    id, agenda_id, fecha, monto, cantidad_personas, estado_disponibilidad, puntos_booked,
    nombre, empresa, descripcion, ubicacion, duracion, precio_persona, capacidad, restricciones
)
VALUES
(69425, 66637, '2025-04-22', 600000, 20, 'No disponible', '2025-08-02', 'Vino de Mesa Italiano', 'WineCo', 'Cata de vinos', 'Corleone', 120, 30000, 20, '{18+}'),
(69426, 66637, '2025-04-22', 500000, 20, 'No disponible', '2025-08-03', 'El príncipe di Corleone', 'Ristorante', 'Cena tradicional', 'Corleone', 120, 25000, 20, '{No fumar}'),
(69427, 66637, '2025-04-22', 240000, 20, 'No disponible', '2025-08-04', 'The Godfather''s House', 'Cultura', 'Tour casa Don Corleone', 'Via Candelora, 25, Corleone', 90, 12000, 20, '{}'),
(69428, 66637, '2025-04-22', 200000, 20, 'No disponible', '2025-08-05', 'Movimiento Antimafia CIDMA', 'CIDMA', 'Museo antimafia', 'Corleone', 120, 10000, 20, '{}');

INSERT INTO Participante(id_panorama, nombre, edad)
VALUES
(69425, 'Cata Bienestar', 23),
(69425, 'Jorge Bienestar', 22),
(69425, 'Lucas Viajero', 23),
(69425, 'Martina Tattaglia', 22),
(69425, 'Tomás Barzini', 22),
(69425, 'Vincenzo Martino', 22),
(69425, 'Agustino Beckerini', 23),
(69425, 'Consuelo Inostrozini', 22),
(69425, 'Ignacio Garridelli', 23),
(69425, 'Olivia Llanini', 22),
(69425, 'Paula Contessa', 23),
(69425, 'Sofía "La Paz" Retamalini', 23);

