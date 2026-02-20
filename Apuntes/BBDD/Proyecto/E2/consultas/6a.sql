SELECT
    nombre AS nombre_usuario,
    COUNT(Reserva.id) AS cantidad_reservas,
    SUM(Usuario.puntos) AS puntos
FROM Usuario
JOIN Agenda ON Usuario.correo = Agenda.correo_usuario
JOIN Reserva ON Agenda.id = Reserva.agenda_id
WHERE nombre IS NOT NULL
GROUP BY nombre
HAVING COUNT(Reserva.id) >= 70
    OR SUM(Usuario.puntos) >= 1000
ORDER BY puntos DESC;