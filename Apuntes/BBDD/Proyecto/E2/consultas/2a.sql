SELECT
    nombre,
    ubicacion,
    estrellas,
    precio_noche
FROM Hospedaje
WHERE estado_disponibilidad = 'Disponible'
    AND nombre IS NOT NULL
ORDER BY estrellas DESC;