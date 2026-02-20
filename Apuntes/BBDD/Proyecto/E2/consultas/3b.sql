SELECT
    p.nombre AS nombre_panorama,
    AVG(r.estrellas) AS prom_estrellas,
    COUNT(r.id) AS cant_reviews,
    (
        SELECT rv.descripcion
        FROM Panorama AS pm
        JOIN Reviews AS rv ON pm.id = rv.reserva_id
        WHERE pm.nombre = p.nombre
            AND rv.descripcion IS NOT NULL
        ORDER BY rv.id DESC
        LIMIT 1
    ) AS ult_comentario
FROM Panorama AS p
JOIN Reviews AS r ON p.id = r.reserva_id
GROUP BY p.nombre;