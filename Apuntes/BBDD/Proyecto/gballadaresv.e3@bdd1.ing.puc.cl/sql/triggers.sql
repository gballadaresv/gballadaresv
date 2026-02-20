CREATE OR REPLACE FUNCTION trigger_agregar_puntos()
RETURNS TRIGGER AS $$
DECLARE
    correo TEXT;
BEGIN
    SELECT correo_usuario INTO correo FROM agenda WHERE id = NEW.agenda_id;
    IF NEW.estado_disponibilidad = 'No disponible' AND OLD.estado_disponibilidad = 'Disponible' THEN
        PERFORM agregar_puntos(NEW.monto, correo);
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER agregar_puntos_trigger
AFTER UPDATE ON reserva
FOR EACH ROW
EXECUTE FUNCTION trigger_agregar_puntos();