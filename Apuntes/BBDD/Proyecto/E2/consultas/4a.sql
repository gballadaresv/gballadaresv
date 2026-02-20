SELECT 
    TO_CHAR(pm.fecha, 'MM-YYYY') AS mes,
    COUNT(DISTINCT pm.id) AS cantidad_panoramas,
    COUNT(pt.nombre) AS cantidad_participantes,
    SUM(pm.precio_persona) AS monto_ganado
FROM Panorama AS pm
JOIN Participante AS pt ON pm.id = pt.id_panorama
WHERE pm.estado_disponibilidad = 'No disponible'
GROUP BY TO_CHAR(pm.fecha, 'MM-YYYY')
ORDER BY cantidad_panoramas DESC
LIMIT 3;