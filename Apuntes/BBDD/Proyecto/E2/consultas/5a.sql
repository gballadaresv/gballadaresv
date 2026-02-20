SELECT
    u.nombre AS nombre_usuario,
    u.puntos,
    COUNT(r.id) AS cantidad_reservas
FROM Usuario AS u
JOIN Agenda AS a ON u.correo = a.correo_usuario
JOIN Reserva AS r ON a.id = r.agenda_id
WHERE u.nombre IS NOT NULL
    AND r.fecha > '2025-05-27'
GROUP BY u.nombre, u.puntos
ORDER BY u.puntos DESC
LIMIT 5;