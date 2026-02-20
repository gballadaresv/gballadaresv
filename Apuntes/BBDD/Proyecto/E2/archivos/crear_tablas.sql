DROP TABLE IF EXISTS Persona CASCADE;
DROP TABLE IF EXISTS Seguro CASCADE;
DROP TABLE IF EXISTS Reviews CASCADE;
DROP TABLE IF EXISTS Transporte CASCADE;
DROP TABLE IF EXISTS Agenda CASCADE;
DROP TABLE IF EXISTS Reserva CASCADE;
DROP TABLE IF EXISTS Participante CASCADE;
DROP TABLE IF EXISTS Habitacion CASCADE;


CREATE TABLE IF NOT EXISTS Persona(
    nombre VARCHAR(40),
    correo VARCHAR(50) PRIMARY KEY NOT NULL UNIQUE,
    contrasena VARCHAR(40),
    username VARCHAR(40) UNIQUE,
    telefono_contacto VARCHAR(15),
    run VARCHAR(10) NOT NULL,
    dv VARCHAR(1) NOT NULL
);

CREATE TABLE IF NOT EXISTS Empleado(
    jornada VARCHAR(20),
    isapre VARCHAR(20) NOT NULL,
    contrato VARCHAR(20)
) INHERITS (Persona);

CREATE TABLE IF NOT EXISTS Usuario(
    puntos INT
) INHERITS (Persona);

CREATE TABLE IF NOT EXISTS Agenda(
    id INT PRIMARY KEY,
    correo_usuario VARCHAR(50),
    etiqueta VARCHAR(20),
    FOREIGN KEY (correo_usuario) REFERENCES Persona(correo)
);

CREATE TABLE IF NOT EXISTS Reserva(
    id INT PRIMARY KEY,
    agenda_id INT,
    fecha DATE,
    monto INT,
    cantidad_personas INT,
    estado_disponibilidad VARCHAR(15),
    puntos_booked INT,
    FOREIGN KEY (agenda_id) REFERENCES Agenda(id)
);

CREATE TABLE IF NOT EXISTS Seguro(
    id SERIAL PRIMARY KEY,
    correo_usuario VARCHAR(50) NOT NULL,
    reserva_id INT UNIQUE,
    tipo VARCHAR(50) NOT NULL,
    valor INT NOT NULL,
    clausula VARCHAR(200) NOT NULL,
    empresa VARCHAR(100) NOT NULL,
    FOREIGN KEY (correo_usuario) REFERENCES Persona(correo),
    FOREIGN KEY (reserva_id) REFERENCES Reserva(id)
);

CREATE TABLE IF NOT EXISTS Reviews(
    id SERIAL PRIMARY KEY,
    correo_usuario VARCHAR(50) NOT NULL,
    reserva_id INT UNIQUE,
    estrellas INT NOT NULL,
    descripcion VARCHAR(200),
    FOREIGN KEY (correo_usuario) REFERENCES Persona(correo),
    FOREIGN KEY (reserva_id) REFERENCES Reserva(id)
);

CREATE TABLE IF NOT EXISTS Panorama(
    empresa VARCHAR(100),
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(200),
    ubicacion VARCHAR(50),
    duracion INT NOT NULL,
    precio_persona INT NOT NULL,
    capacidad INT,
    restricciones VARCHAR(200),
    fecha_panorama DATE NOT NULL
) INHERITS (Reserva);

CREATE TABLE IF NOT EXISTS Participante(
    id_panorama INT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    edad INT,
    FOREIGN KEY (id_panorama) REFERENCES Reserva(id),
    PRIMARY KEY (id_panorama, nombre)
);

CREATE TABLE IF NOT EXISTS Hospedaje(
    nombre VARCHAR(50),
    ubicacion VARCHAR(50) NOT NULL,
    precio_noche INT NOT NULL,
    estrellas INT NOT NULL,
    comodidades VARCHAR(200),
    fecha_checkin DATE NOT NULL,
    fecha_checkout DATE
) INHERITS (Reserva);

CREATE TABLE IF NOT EXISTS Airbnb(
    nombre_anfitrion VARCHAR(50) NOT NULL,
    contacto_anfitrion VARCHAR(15) NOT NULL,
    descripcion VARCHAR(200) NOT NULL,
    piezas INT NOT NULL,
    camas INT NOT NULL,
    banos INT NOT NULL
) INHERITS (Hospedaje);

CREATE TABLE IF NOT EXISTS Hotel(
    politicas VARCHAR(200) NOT NULL
) INHERITS (Hospedaje);

CREATE TABLE IF NOT EXISTS Habitacion(
    id_hotel INT NOT NULL,
    numero_habitacion INT NOT NULL,
    tipo VARCHAR(20),
    FOREIGN KEY (id_hotel) REFERENCES Reserva(id),
    PRIMARY KEY (id_hotel, numero_habitacion)
);

CREATE TABLE IF NOT EXISTS Transporte(
    correo_empleado VARCHAR(50) NOT NULL UNIQUE,
    lugar_origen VARCHAR(50),
    lugar_llegada VARCHAR(50),
    capacidad INT,
    tiempo_estimado INT NOT NULL,
    precio_asiento INT NOT NULL,
    empresa VARCHAR(100),
    fecha_salida DATE NOT NULL,
    fecha_llegada DATE,
    FOREIGN KEY (correo_empleado) REFERENCES Persona(correo)
) INHERITS (Reserva);

CREATE TABLE IF NOT EXISTS Tren(
    comodidades VARCHAR(200),
    paradas VARCHAR(200) NOT NULL
) INHERITS (Transporte);

CREATE TABLE IF NOT EXISTS Bus(
    comodidades VARCHAR(200),
    tipo VARCHAR(20) NOT NULL
) INHERITS (Transporte);

CREATE TABLE IF NOT EXISTS Avion(
    clase VARCHAR(20) NOT NULL,
    escalas VARCHAR(200) NOT NULL
) INHERITS (Transporte);