SELECT
    TO_CHAR(fecha, 'MM-YYYY') AS mes,
    COUNT(id) AS cantidad_reservas,
    SUM(monto) AS monto_total
FROM Reserva
WHERE estado_disponibilidad = 'No disponible'
GROUP BY TO_CHAR(fecha, 'MM-YYYY');