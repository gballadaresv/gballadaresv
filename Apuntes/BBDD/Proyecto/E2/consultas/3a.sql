SELECT
    p.nombre,
    AVG(r.estrellas) AS prom_estrellas,
    COUNT(r.id) AS cant_reviews
FROM Panorama AS p
JOIN Reviews AS r
ON p.id = r.reserva_id
GROUP BY p.nombre;