DROP TABLE IF EXISTS T4;

CREATE TABLE T4 (
    Nomobre TEXT,
    Apellidos TEXT,
    Sexo CHAR(1),
    Edad INT,
    Pais TEXT,
    Fundacion TEXT,
    Razon TEXT,
    Fecha TEXT,
    Frecuencia TEXT
);

\copy T4 FROM 'DatosT4.csv' WITH (FORMAT CSV, HEADER TRUE, DELIMITER ';', ENCODING 'UTF8');