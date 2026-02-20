CREATE TEMP TABLE agenda_reserva_tmp(
    agenda_id INT,
    etiqueta VARCHAR(20),
    id INT,
    fecha DATE,
    monto INT,
    cantidad_personas INT,
    estado_disponibilidad VARCHAR(15),
    puntos INT,
    correo_empleado VARCHAR(50),
    lugar_origen VARCHAR(50),
    lugar_llegada VARCHAR(50),
    capacidad INT,
    tiempo_estimado INT,
    precio_asiento INT,
    empresa VARCHAR(100),
    fecha_salida DATE,
    fecha_llegada DATE,
    tipo_bus VARCHAR(20),
    comodidades VARCHAR(200),
    escalas VARCHAR(200),
    clase VARCHAR(20),
    paradas VARCHAR(200),
    nombre_hospedaje VARCHAR(50),
    ubicacion VARCHAR(50),
    precio_noche INT,
    estrellas INT,
    fecha_checkin DATE,
    fecha_checkout DATE,
    politicas VARCHAR(200),
    nombre_anfitrion VARCHAR(50),
    contacto_anfitrion VARCHAR(15),
    descripcion_airbnb VARCHAR(200),
    piezas INT,
    camas INT,
    banos INT,
    nombre_panorama VARCHAR(50),
    duracion INT,
    precio_persona INT,
    restricciones VARCHAR(200),
    fecha_panorama DATE
);

CREATE TEMP TABLE habitaciones_tmp(
    hotel_id INT,
    numero_habitacion INT,
    tipo VARCHAR(20)
);

CREATE TEMP TABLE participantes_tmp(
    panorama_id INT,
    nombre VARCHAR(50),
    edad INT
);

CREATE TEMP TABLE personas_tmp(
    nombre VARCHAR(40),
    correo VARCHAR(50),
    contrasena VARCHAR(40),
    username VARCHAR(40),
    telefono_contacto VARCHAR(15),
    run VARCHAR(10),
    puntos INT,
    jornada VARCHAR(20),
    isapre VARCHAR(20),
    contrato VARCHAR(20),
    dv VARCHAR(1)
);

CREATE TEMP TABLE review_seguro_tmp(
    correo_usuario VARCHAR(50),
    puntos INT,
    reserva_id INT,
    tipo_seguro VARCHAR(50),
    valor_seguro INT,
    clausula VARCHAR(200),
    empresa_seguro VARCHAR(50),
    estrellas INT,
    descripcion VARCHAR(200)
);

CREATE TEMP TABLE agenda_correo_tmp(
    agenda_id INT,
    reserva_id INT,
    correo_usuario VARCHAR(50)
);


\copy agenda_reserva_tmp FROM '../csv/agenda_reserva.csv' DELIMITER ',' CSV HEADER;
\copy habitaciones_tmp FROM '../csv/habitaciones.csv' DELIMITER ',' CSV HEADER;
\copy participantes_tmp FROM '../csv/participantes.csv' DELIMITER ',' CSV HEADER;
\copy personas_tmp FROM '../csv/personas.csv' DELIMITER ',' CSV HEADER;
\copy review_seguro_tmp FROM '../csv/review_seguro.csv' DELIMITER ',' CSV HEADER;

INSERT INTO agenda_correo_tmp(agenda_id, reserva_id, correo_usuario)
SELECT
    agenda_id, reserva_id, correo_usuario
FROM agenda_reserva_tmp, review_seguro_tmp
WHERE agenda_reserva_tmp.id = review_seguro_tmp.reserva_id;



-- Personas
INSERT INTO Persona(nombre, correo, contrasena, username, telefono_contacto, run, dv)
SELECT DISTINCT ON (correo)
    nombre, correo, contrasena, username, telefono_contacto, run, dv
FROM personas_tmp
WHERE correo IS NOT NULL 
    AND username IS NOT NULL 
    AND run IS NOT NULL 
    AND dv IS NOT NULL;

CREATE TEMP TABLE personas_ds(
    nombre VARCHAR(40),
    correo VARCHAR(50),
    contrasena VARCHAR(40),
    username VARCHAR(40),
    telefono_contacto VARCHAR(15),
    run VARCHAR(10),
    dv VARCHAR(1)
);

INSERT INTO personas_ds(nombre, correo, contrasena, username, telefono_contacto, run, dv)
SELECT nombre, correo, contrasena, username, telefono_contacto, run, dv
FROM personas_tmp
WHERE correo IS NULL
    OR username IS NULL
    OR run IS NULL
    OR dv IS NULL
    OR correo IN (SELECT correo FROM personas_tmp GROUP BY correo HAVING COUNT(*) > 1)
    OR username IN (SELECT username FROM personas_tmp GROUP BY username HAVING COUNT(*) > 1);

\copy (SELECT * FROM personas_ds) TO '../descartados/personas_descartados.csv' CSV HEADER;


-- Empleados
INSERT INTO Empleado(nombre, correo, contrasena, username, telefono_contacto, run, dv, jornada, isapre, contrato)
SELECT DISTINCT ON (correo)
    nombre, correo, contrasena, username, telefono_contacto, run, dv, jornada, isapre, contrato
FROM personas_tmp
WHERE correo IS NOT NULL 
    AND username IS NOT NULL 
    AND run IS NOT NULL 
    AND dv IS NOT NULL 
    AND isapre IS NOT NULL
    AND jornada IN ('Diurno', 'Nocturno') 
    AND contrato IN ('Full time', 'Part time');

CREATE TEMP TABLE empleados_ds(
    nombre VARCHAR(40),
    correo VARCHAR(50),
    contrasena VARCHAR(40),
    username VARCHAR(40),
    telefono_contacto VARCHAR(15),
    run VARCHAR(10),
    dv VARCHAR(1),
    jornada VARCHAR(20),
    isapre VARCHAR(20),
    contrato VARCHAR(20)
);

INSERT INTO empleados_ds(nombre, correo, contrasena, username, telefono_contacto, run, dv, jornada, isapre, contrato)
SELECT nombre, correo, contrasena, username, telefono_contacto, run, dv, jornada, isapre, contrato
FROM personas_tmp
WHERE correo IS NULL 
    OR username IS NULL 
    OR run IS NULL 
    OR dv IS NULL 
    OR jornada IS NULL 
    OR isapre IS NULL 
    OR jornada NOT IN ('Diurno', 'Nocturno') 
    OR contrato NOT IN ('Full time', 'part time')
    OR correo IN (SELECT correo FROM personas_tmp GROUP BY correo HAVING COUNT(*) > 1)
    OR username IN (SELECT username FROM personas_tmp GROUP BY username HAVING COUNT(*) > 1);

\copy (SELECT * FROM empleados_ds) TO '../descartados/empleados_descartados.csv' CSV HEADER;


-- Usuarios
INSERT INTO Usuario(nombre, correo, contrasena, username, telefono_contacto, run, dv, puntos)
SELECT DISTINCT ON (correo)
    nombre, correo, contrasena, username, telefono_contacto, run, dv, puntos
FROM personas_tmp
WHERE correo IS NOT NULL 
    AND username IS NOT NULL 
    AND run IS NOT NULL 
    AND dv IS NOT NULL
    AND puntos >= 0;

CREATE TEMP TABLE usuarios_ds(
    nombre VARCHAR(40),
    correo VARCHAR(50),
    contrasena VARCHAR(40),
    username VARCHAR(40),
    telefono_contacto VARCHAR(15),
    run VARCHAR(10),
    dv VARCHAR(1),
    puntos INT
);

INSERT INTO usuarios_ds(nombre, correo, contrasena, username, telefono_contacto, run, dv, puntos)
SELECT nombre, correo, contrasena, username, telefono_contacto, run, dv, puntos
FROM personas_tmp
WHERE correo IS NULL 
    OR username IS NULL 
    OR run IS NULL 
    OR dv IS NULL 
    OR puntos IS NULL
    OR puntos < 0
    OR correo IN (SELECT correo FROM personas_tmp GROUP BY correo HAVING COUNT(*) > 1);

\copy (SELECT * FROM usuarios_ds) TO '../descartados/usuarios_descartados.csv' CSV HEADER;

-- Agenda
INSERT INTO Agenda(id, correo_usuario, etiqueta)
SELECT DISTINCT ON (ar.agenda_id)
    ar.agenda_id, correo_usuario, etiqueta
FROM agenda_reserva_tmp AS ar JOIN agenda_correo_tmp AS ac
ON ar.id = ac.reserva_id
WHERE ac.agenda_id IS NOT NULL 
    AND ac.correo_usuario IN (SELECT correo FROM Usuario);

CREATE TEMP TABLE agenda_ds(
    agenda_id INT,
    correo_usuario VARCHAR(50),
    etiqueta VARCHAR(20)
);

INSERT INTO agenda_ds(agenda_id, correo_usuario, etiqueta)
SELECT ar.agenda_id, correo_usuario, etiqueta
FROM agenda_reserva_tmp AS ar JOIN agenda_correo_tmp AS ac
ON ar.id = ac.reserva_id
WHERE ac.agenda_id IS NULL 
    OR ac.correo_usuario NOT IN (SELECT correo FROM Usuario)
    OR ar.agenda_id IN (SELECT agenda_id FROM agenda_correo_tmp GROUP BY agenda_id HAVING COUNT(*) > 1);

\copy (SELECT * FROM agenda_ds) TO '../descartados/agendas_descartados.csv' CSV HEADER;


-- Reserva
INSERT INTO Reserva(id, agenda_id, fecha, monto, cantidad_personas, estado_disponibilidad, puntos_booked)
SELECT id, agenda_id, fecha, monto, cantidad_personas, estado_disponibilidad, puntos
FROM agenda_reserva_tmp
WHERE (
    id IS NOT NULL 
    AND fecha IS NOT NULL
    AND estado_disponibilidad = 'No disponible'
    AND cantidad_personas IS NOT NULL 
    AND monto > 0 
    AND puntos > 0
    AND agenda_id IN (SELECT id FROM Agenda)
) OR (
    id IS NOT NULL
    AND puntos = 0
    AND estado_disponibilidad = 'Disponible'
    AND agenda_id IS NULL
);

CREATE TEMP TABLE reserva_ds(
    id INT,
    agenda_id INT,
    fecha DATE,
    monto INT,
    cantidad_personas INT,
    estado_disponibilidad VARCHAR(15),
    puntos_booked INT
);

INSERT INTO reserva_ds(id, agenda_id, fecha, monto, cantidad_personas, estado_disponibilidad, puntos_booked)
SELECT id, agenda_id, fecha, monto, cantidad_personas, estado_disponibilidad, puntos
FROM agenda_reserva_tmp
WHERE id IS NULL
    OR estado_disponibilidad NOT IN ('No disponible', 'Disponible')
    OR estado_disponibilidad IS NULL
    OR (estado_disponibilidad = 'No disponible'
        AND (cantidad_personas IS NULL
            OR fecha IS NULL
            OR monto IS NULL
            OR monto <= 0
            OR puntos IS NULL
            OR puntos <= 0
            OR agenda_id IS NULL
            OR agenda_id NOT IN (SELECT id FROM Agenda)))
    OR (estado_disponibilidad = 'Disponible'
        AND (puntos IS NULL
            OR puntos != 0));

\copy (SELECT * FROM reserva_ds) TO '../descartados/reservas_descartados.csv' CSV HEADER;


-- Seguro
INSERT INTO Seguro(correo_usuario, reserva_id, tipo, valor, clausula, empresa)
SELECT DISTINCT ON (reserva_id)
    correo_usuario, reserva_id, tipo_seguro, valor_seguro, clausula, empresa_seguro
FROM review_seguro_tmp
WHERE reserva_id IS NOT NULL
    AND tipo_seguro IS NOT NULL
    AND valor_seguro IS NOT NULL
    AND clausula IS NOT NULL
    AND empresa_seguro IS NOT NULL
    AND valor_seguro > 0
    AND EXISTS (SELECT correo FROM Usuario WHERE correo = correo_usuario)
    AND EXISTS (SELECT id FROM Reserva WHERE id = reserva_id);

CREATE TEMP TABLE seguro_ds(
    correo_usuario VARCHAR(50),
    reserva_id INT,
    tipo_seguro VARCHAR(50),
    valor_seguro INT,
    clausula VARCHAR(200),
    empresa_seguro VARCHAR(50)
);

INSERT INTO seguro_ds(correo_usuario, reserva_id, tipo_seguro, valor_seguro, clausula, empresa_seguro)
SELECT correo_usuario, reserva_id, tipo_seguro, valor_seguro, clausula, empresa_seguro
FROM review_seguro_tmp
WHERE reserva_id IS NULL
    OR tipo_seguro IS NULL
    OR valor_seguro IS NULL
    OR clausula IS NULL
    OR empresa_seguro IS NULL
    OR valor_seguro <= 0
    OR correo_usuario NOT IN (SELECT correo FROM Usuario)
    OR reserva_id NOT IN (SELECT id FROM Reserva);

\copy (SELECT * FROM seguro_ds) TO '../descartados/seguros_descartados.csv' CSV HEADER;


-- Review
INSERT INTO Reviews(correo_usuario, reserva_id, estrellas, descripcion)
SELECT DISTINCT ON (reserva_id)
    correo_usuario, reserva_id, estrellas, descripcion
FROM review_seguro_tmp
WHERE estrellas >= 0
    AND estrellas <= 5
    AND EXISTS (SELECT correo FROM Usuario WHERE correo = correo_usuario)
    AND EXISTS (SELECT id FROM Reserva WHERE id = reserva_id);

CREATE TEMP TABLE review_ds(
    correo_usuario VARCHAR(50),
    reserva_id INT,
    estrellas INT,
    descripcion VARCHAR(200)
);

INSERT INTO review_ds(correo_usuario, reserva_id, estrellas, descripcion)
SELECT correo_usuario, reserva_id, estrellas, descripcion
FROM review_seguro_tmp
WHERE estrellas IS NULL
    OR estrellas < 0
    OR estrellas > 5
    OR correo_usuario NOT IN (SELECT correo FROM Usuario)
    OR reserva_id NOT IN (SELECT id FROM Reserva);

\copy (SELECT * FROM review_ds) TO '../descartados/reviews_descartados.csv' CSV HEADER;


-- Panorama
INSERT INTO Panorama(id, agenda_id, fecha, monto, cantidad_personas, estado_disponibilidad,
    puntos_booked, empresa, nombre, descripcion, ubicacion, duracion, precio_persona, capacidad, restricciones, fecha_panorama)
SELECT ar.id, ar.agenda_id, ar.fecha, ar.monto, ar.cantidad_personas, ar.estado_disponibilidad,
    ar.puntos, ar.empresa, ar.nombre_panorama, ar.descripcion_airbnb, ar.ubicacion, ar.duracion, ar.precio_persona,
    ar.capacidad, ar.restricciones, ar.fecha_panorama
FROM agenda_reserva_tmp AS ar JOIN Reserva ON ar.id = Reserva.id
WHERE ar.nombre_panorama IS NOT NULL
    AND ar.fecha_panorama IS NOT NULL
    AND ar.duracion IS NOT NULL
    AND ar.precio_persona IS NOT NULL
    AND ar.precio_persona > 0;

CREATE TEMP TABLE panorama_ds(
    id INT,
    agenda_id INT,
    fecha DATE,
    monto INT,
    cantidad_personas INT,
    estado_disponibilidad VARCHAR(15),
    puntos_booked INT,
    empresa VARCHAR(100),
    nombre VARCHAR(50),
    descripcion VARCHAR(200),
    ubicacion VARCHAR(50),
    duracion INT,
    precio_persona INT,
    capacidad INT,
    restricciones VARCHAR(200),
    fecha_panorama DATE
);

INSERT INTO panorama_ds(id, agenda_id, fecha, monto, cantidad_personas, estado_disponibilidad,
    puntos_booked, empresa, nombre, descripcion, ubicacion, duracion, precio_persona, capacidad, restricciones, fecha_panorama)
SELECT ar.id, ar.agenda_id, ar.fecha, ar.monto, ar.cantidad_personas, ar.estado_disponibilidad,
    ar.puntos, ar.empresa, ar.nombre_panorama, ar.descripcion_airbnb, ar.ubicacion, ar.duracion, ar.precio_persona,
    ar.capacidad, ar.restricciones, ar.fecha_panorama
FROM agenda_reserva_tmp AS ar JOIN Reserva ON ar.id = Reserva.id
WHERE ar.nombre_panorama IS NULL
    OR ar.fecha_panorama IS NULL
    OR ar.duracion IS NULL
    OR ar.precio_persona IS NULL;

\copy (SELECT * FROM panorama_ds) TO '../descartados/panoramas_descartados.csv' CSV HEADER;


-- Participante
INSERT INTO Participante(id_panorama, nombre, edad)
SELECT panorama_id, nombre, edad
FROM participantes_tmp
WHERE nombre IS NOT NULL
    AND edad > 0
    AND panorama_id IN (SELECT id FROM Panorama);

CREATE TEMP TABLE participantes_ds(
    panorama_id INT,
    nombre VARCHAR(50),
    edad INT
);

INSERT INTO participantes_ds(panorama_id, nombre, edad)
SELECT panorama_id, nombre, edad
FROM participantes_tmp
WHERE nombre IS NULL
    OR edad IS NULL
    OR edad <= 0
    OR panorama_id NOT IN (SELECT id FROM Panorama);

\copy (SELECT * FROM participantes_ds) TO '../descartados/participantes_descartados.csv' CSV HEADER;


-- Hospedaje
INSERT INTO Hospedaje(id, agenda_id, fecha, monto, cantidad_personas, estado_disponibilidad, puntos_booked,
    nombre, ubicacion, precio_noche, estrellas, fecha_checkin, fecha_checkout)
SELECT ar.id, ar.agenda_id, ar.fecha, ar.monto, ar.cantidad_personas, ar.estado_disponibilidad,
    ar.puntos, ar.nombre_hospedaje, ar.ubicacion, ar.precio_noche, ar.estrellas, ar.fecha_checkin, ar.fecha_checkout
FROM agenda_reserva_tmp AS ar JOIN Reserva ON ar.id = Reserva.id
WHERE ar.ubicacion IS NOT NULL
    AND ar.precio_noche IS NOT NULL
    AND ar.precio_noche > 0
    AND ar.estrellas >= 0
    AND ar.estrellas <= 5
    AND ar.fecha_checkin IS NOT NULL;

CREATE TEMP TABLE hospedaje_ds(
    id INT,
    agenda_id INT,
    fecha DATE,
    monto INT,
    cantidad_personas INT,
    estado_disponibilidad VARCHAR(15),
    puntos_booked INT,
    nombre VARCHAR(50),
    ubicacion VARCHAR(50),
    precio_noche INT,
    estrellas INT,
    fecha_checkin DATE,
    fecha_checkout DATE
);

INSERT INTO hospedaje_ds(id, agenda_id, fecha, monto, cantidad_personas, estado_disponibilidad, puntos_booked,
    nombre, ubicacion, precio_noche, estrellas, fecha_checkin, fecha_checkout)
SELECT ar.id, ar.agenda_id, ar.fecha, ar.monto, ar.cantidad_personas, ar.estado_disponibilidad,
    ar.puntos, ar.nombre_hospedaje, ar.ubicacion, ar.precio_noche, ar.estrellas, ar.fecha_checkin, ar.fecha_checkout
FROM agenda_reserva_tmp AS ar JOIN Reserva ON ar.id = Reserva.id
WHERE ar.ubicacion IS NULL
    OR ar.precio_noche IS NULL
    OR ar.precio_noche <= 0
    OR ar.estrellas IS NULL
    OR ar.estrellas < 0
    OR ar.estrellas > 5
    OR ar.fecha_checkin IS NULL;

\copy (SELECT * FROM hospedaje_ds) TO '../descartados/hospedajes_descartados.csv' CSV HEADER;


-- Airbnb
INSERT INTO Airbnb(id, agenda_id, fecha, monto, cantidad_personas, estado_disponibilidad, puntos_booked,
    nombre, ubicacion, precio_noche, estrellas, fecha_checkin, fecha_checkout, nombre_anfitrion, contacto_anfitrion,
    descripcion, piezas, camas, banos)
SELECT ar.id, ar.agenda_id, ar.fecha, ar.monto, ar.cantidad_personas, ar.estado_disponibilidad,
    ar.puntos, ar.nombre_hospedaje, ar.ubicacion, ar.precio_noche, ar.estrellas, ar.fecha_checkin, ar.fecha_checkout,
    ar.nombre_anfitrion, ar.contacto_anfitrion, ar.descripcion_airbnb, ar.piezas, ar.camas, ar.banos
FROM agenda_reserva_tmp AS ar JOIN Hospedaje ON ar.id = Hospedaje.id
WHERE ar.nombre_anfitrion IS NOT NULL
    AND ar.contacto_anfitrion IS NOT NULL
    AND ar.descripcion_airbnb IS NOT NULL
    AND ar.piezas IS NOT NULL
    AND ar.camas IS NOT NULL
    AND ar.banos IS NOT NULL
    AND ar.piezas >= 0
    AND ar.camas >= 0
    AND ar.banos >= 0;

CREATE TEMP TABLE airbnb_ds(
    id INT,
    agenda_id INT,
    fecha DATE,
    monto INT,
    cantidad_personas INT,
    estado_disponibilidad VARCHAR(15),
    puntos_booked INT,
    nombre VARCHAR(50),
    ubicacion VARCHAR(50),
    precio_noche INT,
    estrellas INT,
    fecha_checkin DATE,
    fecha_checkout DATE,
    nombre_anfitrion VARCHAR(50),
    contacto_anfitrion VARCHAR(15),
    descripcion VARCHAR(200),
    piezas INT,
    camas INT,
    banos INT
);

INSERT INTO airbnb_ds(id, agenda_id, fecha, monto, cantidad_personas, estado_disponibilidad, puntos_booked,
    nombre, ubicacion, precio_noche, estrellas, fecha_checkin, fecha_checkout, nombre_anfitrion, contacto_anfitrion,
    descripcion, piezas, camas, banos)
SELECT ar.id, ar.agenda_id, ar.fecha, ar.monto, ar.cantidad_personas, ar.estado_disponibilidad,
    ar.puntos, ar.nombre_hospedaje, ar.ubicacion, ar.precio_noche, ar.estrellas, ar.fecha_checkin, ar.fecha_checkout,
    ar.nombre_anfitrion, ar.contacto_anfitrion, ar.descripcion_airbnb, ar.piezas, ar.camas, ar.banos
FROM agenda_reserva_tmp AS ar JOIN Hospedaje ON ar.id = Hospedaje.id
WHERE ar.nombre_anfitrion IS NULL
    OR ar.contacto_anfitrion IS NULL
    OR ar.descripcion_airbnb IS NULL
    OR ar.piezas IS NULL
    OR ar.camas IS NULL
    OR ar.banos IS NULL
    OR ar.piezas < 0
    OR ar.camas < 0
    OR ar.banos < 0;

\copy (SELECT * FROM airbnb_ds) TO '../descartados/airbnb_descartados.csv' CSV HEADER;


-- Hotel
INSERT INTO Hotel(id, agenda_id, fecha, monto, cantidad_personas, estado_disponibilidad, puntos_booked,
    nombre, ubicacion, precio_noche, estrellas, fecha_checkin, fecha_checkout, politicas)
SELECT ar.id, ar.agenda_id, ar.fecha, ar.monto, ar.cantidad_personas, ar.estado_disponibilidad,
    ar.puntos, ar.nombre_hospedaje, ar.ubicacion, ar.precio_noche, ar.estrellas, ar.fecha_checkin, ar.fecha_checkout, ar.politicas
FROM agenda_reserva_tmp AS ar JOIN Hospedaje ON ar.id = Hospedaje.id
WHERE ar.politicas IS NOT NULL;

CREATE TEMP TABLE hotel_ds(
    id INT,
    agenda_id INT,
    fecha DATE,
    monto INT,
    cantidad_personas INT,
    estado_disponibilidad VARCHAR(15),
    puntos_booked INT,
    nombre VARCHAR(50),
    ubicacion VARCHAR(50),
    precio_noche INT,
    estrellas INT,
    fecha_checkin DATE,
    fecha_checkout DATE,
    politicas VARCHAR(200)
);

INSERT INTO hotel_ds(id, agenda_id, fecha, monto, cantidad_personas, estado_disponibilidad, puntos_booked,
    nombre, ubicacion, precio_noche, estrellas, fecha_checkin, fecha_checkout, politicas)
SELECT ar.id, ar.agenda_id, ar.fecha, ar.monto, ar.cantidad_personas, ar.estado_disponibilidad,
    ar.puntos, ar.nombre_hospedaje, ar.ubicacion, ar.precio_noche, ar.estrellas, ar.fecha_checkin, ar.fecha_checkout, ar.politicas
FROM agenda_reserva_tmp AS ar JOIN Hospedaje ON ar.id = Hospedaje.id
WHERE ar.politicas IS NULL;

\copy (SELECT * FROM hotel_ds) TO '../descartados/hoteles_descartados.csv' CSV HEADER;


-- Habitacion
INSERT INTO Habitacion(id_hotel, numero_habitacion, tipo)
SELECT DISTINCT ON (hotel_id, numero_habitacion)
    hotel_id, numero_habitacion, tipo
FROM habitaciones_tmp
WHERE numero_habitacion IS NOT NULL
    AND hotel_id IN (SELECT id FROM Hotel);

CREATE TEMP TABLE habitaciones_ds(
    hotel_id INT,
    numero_habitacion INT,
    tipo VARCHAR(20)
);

INSERT INTO habitaciones_ds(hotel_id, numero_habitacion, tipo)
SELECT hotel_id, numero_habitacion, tipo
FROM habitaciones_tmp
WHERE numero_habitacion IS NULL
    OR hotel_id IS NULL
    OR hotel_id NOT IN (SELECT id FROM Hotel);

\copy (SELECT * FROM habitaciones_ds) TO '../descartados/habitaciones_descartadas.csv' CSV HEADER;


-- Transporte
INSERT INTO Transporte(id, agenda_id, fecha, monto, cantidad_personas, estado_disponibilidad, puntos_booked,
    correo_empleado, lugar_origen, lugar_llegada, capacidad, tiempo_estimado, precio_asiento, empresa, fecha_salida, fecha_llegada)
SELECT DISTINCT ON (correo_empleado) 
    ar.id, ar.agenda_id, ar.fecha, ar.monto, ar.cantidad_personas, ar.estado_disponibilidad,
    ar.puntos, ar.correo_empleado, ar.lugar_origen, ar.lugar_llegada, ar.capacidad, ar.tiempo_estimado,
    ar.precio_asiento, ar.empresa, ar.fecha_salida, ar.fecha_llegada
FROM agenda_reserva_tmp AS ar JOIN Reserva ON ar.id = Reserva.id
WHERE ar.tiempo_estimado IS NOT NULL
    AND ar.precio_asiento > 0
    AND ar.fecha_salida IS NOT NULL
    AND ar.correo_empleado IN (SELECT correo FROM Empleado);

CREATE TEMP TABLE transporte_ds(
    id INT,
    agenda_id INT,
    fecha DATE,
    monto INT,
    cantidad_personas INT,
    estado_disponibilidad VARCHAR(15),
    puntos_booked INT,
    correo_empleado VARCHAR(50),
    lugar_origen VARCHAR(50),
    lugar_llegada VARCHAR(50),
    capacidad INT,
    tiempo_estimado INT,
    precio_asiento INT,
    empresa VARCHAR(100),
    fecha_salida DATE,
    fecha_llegada DATE
);

INSERT INTO transporte_ds(id, agenda_id, fecha, monto, cantidad_personas, estado_disponibilidad, puntos_booked,
    correo_empleado, lugar_origen, lugar_llegada, capacidad, tiempo_estimado, precio_asiento, empresa, fecha_salida, fecha_llegada)
SELECT ar.id, ar.agenda_id, ar.fecha, ar.monto, ar.cantidad_personas, ar.estado_disponibilidad,
    ar.puntos, ar.correo_empleado, ar.lugar_origen, ar.lugar_llegada, ar.capacidad, ar.tiempo_estimado,
    ar.precio_asiento, ar.empresa, ar.fecha_salida, ar.fecha_llegada
FROM agenda_reserva_tmp AS ar JOIN Reserva ON ar.id = Reserva.id
WHERE ar.tiempo_estimado IS NULL
    OR ar.precio_asiento <= 0
    OR ar.precio_asiento IS NULL
    OR ar.fecha_salida IS NULL
    OR ar.correo_empleado NOT IN (SELECT correo FROM Empleado);

\copy (SELECT * FROM transporte_ds) TO '../descartados/transportes_descartados.csv' CSV HEADER;


-- Tren
INSERT INTO Tren(id, agenda_id, fecha, monto, cantidad_personas, estado_disponibilidad, puntos_booked,
    correo_empleado, lugar_origen, lugar_llegada, capacidad, tiempo_estimado, precio_asiento, empresa, fecha_salida, fecha_llegada, 
    comodidades, paradas)
SELECT DISTINCT ON (correo_empleado)
    ar.id, ar.agenda_id, ar.fecha, ar.monto, ar.cantidad_personas, ar.estado_disponibilidad,
    ar.puntos, ar.correo_empleado, ar.lugar_origen, ar.lugar_llegada, ar.capacidad, ar.tiempo_estimado,
    ar.precio_asiento, ar.empresa, ar.fecha_salida, ar.fecha_llegada, ar.comodidades, ar.paradas
FROM agenda_reserva_tmp AS ar JOIN Transporte ON ar.id = Transporte.id
WHERE ar.paradas IS NOT NULL;

CREATE TEMP TABLE tren_ds(
    id INT,
    agenda_id INT,
    fecha DATE,
    monto INT,
    cantidad_personas INT,
    estado_disponibilidad VARCHAR(15),
    puntos_booked INT,
    correo_empleado VARCHAR(50),
    lugar_origen VARCHAR(50),
    lugar_llegada VARCHAR(50),
    capacidad INT,
    tiempo_estimado INT,
    precio_asiento INT,
    empresa VARCHAR(100),
    fecha_salida DATE,
    fecha_llegada DATE,
    comodidades VARCHAR(200),
    paradas VARCHAR(200)
);

INSERT INTO tren_ds(id, agenda_id, fecha, monto, cantidad_personas, estado_disponibilidad, puntos_booked,
    correo_empleado, lugar_origen, lugar_llegada, capacidad, tiempo_estimado, precio_asiento, empresa, fecha_salida, fecha_llegada,
    comodidades, paradas)
SELECT ar.id, ar.agenda_id, ar.fecha, ar.monto, ar.cantidad_personas, ar.estado_disponibilidad,
    ar.puntos, ar.correo_empleado, ar.lugar_origen, ar.lugar_llegada, ar.capacidad, ar.tiempo_estimado,
    ar.precio_asiento, ar.empresa, ar.fecha_salida, ar.fecha_llegada, ar.comodidades, ar.paradas
FROM agenda_reserva_tmp AS ar JOIN Transporte ON ar.id = Transporte.id
WHERE ar.paradas IS NULL;

\copy (SELECT * FROM tren_ds) TO '../descartados/trenes_descartados.csv' CSV HEADER;



-- Bus
INSERT INTO Bus(id, agenda_id, fecha, monto, cantidad_personas, estado_disponibilidad, puntos_booked,
    correo_empleado, lugar_origen, lugar_llegada, capacidad, tiempo_estimado, precio_asiento, empresa, fecha_salida, fecha_llegada,
    comodidades, tipo)
SELECT DISTINCT ON (correo_empleado)
    ar.id, ar.agenda_id, ar.fecha, ar.monto, ar.cantidad_personas, ar.estado_disponibilidad,
    ar.puntos, ar.correo_empleado, ar.lugar_origen, ar.lugar_llegada, ar.capacidad, ar.tiempo_estimado,
    ar.precio_asiento, ar.empresa, ar.fecha_salida, ar.fecha_llegada, ar.comodidades, ar.tipo_bus
FROM agenda_reserva_tmp AS ar JOIN Transporte ON ar.id = Transporte.id
WHERE ar.tipo_bus IS NOT NULL;

CREATE TEMP TABLE bus_ds(
    id INT,
    agenda_id INT,
    fecha DATE,
    monto INT,
    cantidad_personas INT,
    estado_disponibilidad VARCHAR(15),
    puntos_booked INT,
    correo_empleado VARCHAR(50),
    lugar_origen VARCHAR(50),
    lugar_llegada VARCHAR(50),
    capacidad INT,
    tiempo_estimado INT,
    precio_asiento INT,
    empresa VARCHAR(100),
    fecha_salida DATE,
    fecha_llegada DATE,
    comodidades VARCHAR(200),
    tipo_bus VARCHAR(20)
);

INSERT INTO bus_ds(id, agenda_id, fecha, monto, cantidad_personas, estado_disponibilidad, puntos_booked,
    correo_empleado, lugar_origen, lugar_llegada, capacidad, tiempo_estimado, precio_asiento, empresa, fecha_salida, fecha_llegada,
    comodidades, tipo_bus)
SELECT ar.id, ar.agenda_id, ar.fecha, ar.monto, ar.cantidad_personas, ar.estado_disponibilidad,
    ar.puntos, ar.correo_empleado, ar.lugar_origen, ar.lugar_llegada, ar.capacidad, ar.tiempo_estimado,
    ar.precio_asiento, ar.empresa, ar.fecha_salida, ar.fecha_llegada, ar.comodidades, ar.tipo_bus
FROM agenda_reserva_tmp AS ar JOIN Transporte ON ar.id = Transporte.id
WHERE ar.tipo_bus IS NULL;

\copy (SELECT * FROM bus_ds) TO '../descartados/buses_descartados.csv' CSV HEADER;

-- Avion
INSERT INTO Avion(id, agenda_id, fecha, monto, cantidad_personas, estado_disponibilidad, puntos_booked,
    correo_empleado, lugar_origen, lugar_llegada, capacidad, tiempo_estimado, precio_asiento, empresa, fecha_salida, fecha_llegada,
    clase, escalas)
SELECT DISTINCT ON (correo_empleado)
    ar.id, ar.agenda_id, ar.fecha, ar.monto, ar.cantidad_personas, ar.estado_disponibilidad,
    ar.puntos, ar.correo_empleado, ar.lugar_origen, ar.lugar_llegada, ar.capacidad, ar.tiempo_estimado,
    ar.precio_asiento, ar.empresa, ar.fecha_salida, ar.fecha_llegada, ar.clase, ar.escalas
FROM agenda_reserva_tmp AS ar JOIN Transporte ON ar.id = Transporte.id
WHERE ar.clase IS NOT NULL
    AND ar.escalas IS NOT NULL;

CREATE TEMP TABLE avion_ds(
    id INT,
    agenda_id INT,
    fecha DATE,
    monto INT,
    cantidad_personas INT,
    estado_disponibilidad VARCHAR(15),
    puntos_booked INT,
    correo_empleado VARCHAR(50),
    lugar_origen VARCHAR(50),
    lugar_llegada VARCHAR(50),
    capacidad INT,
    tiempo_estimado INT,
    precio_asiento INT,
    empresa VARCHAR(100),
    fecha_salida DATE,
    fecha_llegada DATE,
    clase VARCHAR(20),
    escalas VARCHAR(200)
);

INSERT INTO avion_ds(id, agenda_id, fecha, monto, cantidad_personas, estado_disponibilidad, puntos_booked,
    correo_empleado, lugar_origen, lugar_llegada, capacidad, tiempo_estimado, precio_asiento, empresa, fecha_salida, fecha_llegada,
    clase, escalas)
SELECT ar.id, ar.agenda_id, ar.fecha, ar.monto, ar.cantidad_personas, ar.estado_disponibilidad,
    ar.puntos, ar.correo_empleado, ar.lugar_origen, ar.lugar_llegada, ar.capacidad, ar.tiempo_estimado,
    ar.precio_asiento, ar.empresa, ar.fecha_salida, ar.fecha_llegada, ar.clase, ar.escalas
FROM agenda_reserva_tmp AS ar JOIN Transporte ON ar.id = Transporte.id
WHERE ar.clase IS NULL
    OR ar.escalas IS NULL;

\copy (SELECT * FROM avion_ds) TO '../descartados/aviones_descartados.csv' CSV HEADER;
