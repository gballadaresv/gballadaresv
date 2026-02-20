<?php
session_start();
if (!isset($_SESSION['usuario'])) {
    header('Location: index.php?error=Debes iniciar sesión');
    exit();
}
$mensaje = $_GET['mensaje'] ?? null;
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Crear Viaje</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <div class="container">
        <h1>Crear nuevo viaje</h1>
        <form action="procesar_crear_viaje.php" method="POST" class="formulario">
            <div class="radio-group">
            <label class="radio-inline">
                <input type="radio" name="agenda_option" value="nueva" checked onclick="toggleAgendaFields()"> Crear nueva agenda
            </label>
            <label class="radio-inline">
                <input type="radio" name="agenda_option" value="existente" onclick="toggleAgendaFields()"> Usar agenda existente
            </label>
            </div>

            <!-- Campos para nueva agenda -->
            <div id="nueva_agenda_fields">
                <label for="nombre">Nombre del viaje:</label>
                <input type="text" id="nombre" name="nombre">
            </div>

            <!-- Campos para agenda existente -->
            <div id="existente_agenda_fields" style="display:none;">
                <label for="agenda_id"> Inserte ID de agenda:</label>
                <input type="number" id="agenda_id" name="agenda_id" min="1">
            </div>

        <button type="submit">Añadir reserva a la agenda</button>
        </form>

        <script>
        function toggleAgendaFields() {
            const nueva = document.querySelector('input[name="agenda_option"][value="nueva"]').checked;
            document.getElementById('nueva_agenda_fields').style.display = nueva ? 'block' : 'none';
            document.getElementById('existente_agenda_fields').style.display = nueva ? 'none' : 'block';
        }
        </script>

        <?php if ($mensaje): ?>
            <p class="error"><?= htmlspecialchars($mensaje) ?></p>
        <?php endif; ?>

        <p><a href="main.php">Volver al inicio</a></p>
    </div>
</body>
</html>
