SELECT
    nombre,
    ubicacion,
    estrellas,
    precio_noche
FROM Hotel
WHERE estado_disponibilidad = 'Disponible' 
    AND politicas != '{}'
    AND nombre IS NOT NULL
ORDER BY estrellas DESC, precio_noche ASC;