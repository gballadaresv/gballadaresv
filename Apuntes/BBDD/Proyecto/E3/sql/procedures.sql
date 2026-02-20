DROP FUNCTION IF EXISTS agregar_puntos(monto INT, correo_usuario TEXT);

CREATE OR REPLACE FUNCTION agregar_puntos(monto INT, correo_usuario TEXT)
RETURNS VOID AS $$
BEGIN
    UPDATE usuario
    SET puntos = puntos + (monto / 1000)
    WHERE correo = correo_usuario;
END;
$$ LANGUAGE plpgsql;