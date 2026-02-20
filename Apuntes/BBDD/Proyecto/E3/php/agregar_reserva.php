<?php
session_start();
if (!isset($_SESSION['usuario'])) {
    header('Location: index.php?error=Debes iniciar sesión');
    exit();
}
$mensaje = $_SESSION["mensaje"] ?? null;
$agenda_id = $_GET['agenda_id'] ?? null;
$form_data = $_SESSION['form_data'] ?? [];
unset($_SESSION['form_data']);
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Agregar Reserva</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <div class="container">
        <h1>Agregar nueva reserva en agenda de id <?= htmlspecialchars($agenda_id) ?> </h1>
        <p class="success"><?= htmlspecialchars($mensaje) ?></p>
        <form action="procesar_agregar_reserva.php" method="POST" class="formulario">
            <input type="hidden" name="agenda_id" value="<?= htmlspecialchars($agenda_id) ?>">

            <!-- Selección del tipo de reserva -->
            <label for="tipo_reserva">Tipo de reserva:</label>
            <select id="tipo_reserva" name="tipo_reserva" required onchange="toggleReservaFields()">
                <option value="">Selecciona un tipo</option>
                <option value="hospedaje" <?= (isset($form_data['tipo_reserva']) && $form_data['tipo_reserva'] == 'hospedaje') ? 'selected' : '' ?>>Hospedaje</option>
                <option value="transporte" <?= (isset($form_data['tipo_reserva']) && $form_data['tipo_reserva'] == 'transporte') ? 'selected' : '' ?>>Transporte</option>
                <option value="panorama" <?= (isset($form_data['tipo_reserva']) && $form_data['tipo_reserva'] == 'panorama') ? 'selected' : '' ?>>Panorama</option>
            </select>

                <!-- Hospedaje -->
                <div id="hospedaje_fields" style="display:none;">
                    <label for="nombre_hospedaje">Nombre del hotel: </label>
                    <input type="text" name="nombre_hospedaje" value="<?= htmlspecialchars($form_data['nombre_hospedaje'] ?? '') ?>">

                    <label for="ubicacion_hospedaje">Ubicación: </label>
                    <input type="text" name="ubicacion_hospedaje" value="<?= htmlspecialchars($form_data['ubicacion_hospedaje'] ?? '') ?>">

                    <label for="fecha_checkin">Fecha checkin: </label>
                    <input type="date" name="fecha_checkin" value="<?= htmlspecialchars($form_data['fecha_checkin'] ?? '') ?>">

                    <label for="fecha_checkout">Fecha checkout: </label>
                    <input type="date" id="fecha_checkout" name="fecha_checkout" value="<?= htmlspecialchars($form_data['fecha_checkout'] ?? '') ?>">
                </div>


                <!-- Transporte -->
                <div id="transporte_fields" style="display:none;">
                    <label for="lugar_origen">Lugar de origen:</label>
                    <input type="text" id="lugar_origen" name="lugar_origen">

                    <label for="lugar_llegada">Lugar de destino:</label>
                    <input type="text" id="lugar_llegada" name="lugar_llegada">

                    <label for="cantidad_personas_transporte">Cantidad de personas:</label>
                    <input type="number" id="cantidad_personas_transporte" name="cantidad_personas" min="1" value="<?= htmlspecialchars($form_data['cantidad_personas']) ?>">

                    <label for="fecha_salida">Fecha de salida:</label>
                    <input type="date" id="fecha_salida" name="fecha_salida">

                    <label for="fecha_llegada">Fecha de llegada:</label>
                    <input type="date" id="fecha_llegada" name="fecha_llegada">
                </div>


                <!-- Panorama -->
                <div id="panorama_fields" style="display:none;">
                    <label for="nombre_panorama">Nombre de la actividad:</label>
                    <input type="text" id="nombre_panorama" name="nombre_panorama">

                    <label for="ubicacion_panorama">Ubicación:</label>
                    <input type="text" id="ubicacion_panorama" name="ubicacion_panorama">

                    <label for="cantidad_personas_panorama">Cantidad de personas:</label>
                    <input type="number" id="cantidad_personas_panorama" name="cantidad_personas" min="1" value="<?= htmlspecialchars($form_data['cantidad_personas']) ?>">

                    <label for="fecha_panorama">Fecha de la actividad:</label>
                    <input type="date" id="fecha_panorama" name="fecha_panorama">

                    <div id="participantes_container"></div>
                </div>


            <button type="submit">Agregar reserva</button>
        </form>

<script>
function toggleReservaFields() {
    var tipo = document.getElementById('tipo_reserva').value;
    document.getElementById('hospedaje_fields').style.display = (tipo === 'hospedaje') ? 'block' : 'none';
    document.getElementById('transporte_fields').style.display = (tipo === 'transporte') ? 'block' : 'none';
    document.getElementById('panorama_fields').style.display = (tipo === 'panorama') ? 'block' : 'none';
    if (tipo === 'panorama') updateParticipantes();
}
</script>

<script>
function updateParticipantes() {
    var cantidad = parseInt(document.getElementById('cantidad_personas_panorama').value) || 0;
    var container = document.getElementById('participantes_container');
    container.innerHTML = '';
    for (let i = 1; i <= cantidad; i++) {
    container.innerHTML += `
        <div class="participante">
            <div class="participante-titulo">Participante ${i}</div>
            <div class="participante-campos">
                <label>Nombre</label>
                <input type="text" name="participantes[${i}][nombre]">
                <label>Edad</label>
                <input type="number" name="participantes[${i}][edad]" min="0">
            </div>
        </div>
    `;}
}
window.onload = toggleReservaFields;
document.getElementById('cantidad_personas_panorama').addEventListener('input', updateParticipantes);
</script>

        <p><a href="main.php">Volver al inicio</a></p>
    </div>
</body>
</html>