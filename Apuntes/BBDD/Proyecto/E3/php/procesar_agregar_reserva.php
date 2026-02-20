<?php
session_start();
require_once 'utils.php';

if (!isset($_SESSION['usuario'])) {
    header('Location: index.php?error=Debes iniciar sesión primero');
    exit();
}

$db = conectarBD();
$correo_usuario = $_SESSION['correo_usuario'] ?? null;
$tipo_reserva = $_POST['tipo_reserva'] ?? '';
$agenda_id = $_POST['agenda_id'] ?? null;

$mensaje = '';

// hospedaje
if ($tipo_reserva == "hospedaje") {
    $nombre_hospedaje = $_POST['nombre_hospedaje'] ?? '';
    $ubicacion_hospedaje = $_POST['ubicacion_hospedaje'] ?? '';
    $fecha_checkin = $_POST['fecha_checkin'] ?? '';
    $fecha_checkout = $_POST['fecha_checkout'] ?? '';

    $checkin = new DateTime($fecha_checkin);
    $checkout = new DateTime($fecha_checkout);
    $intervalo = $checkin->diff($checkout);
    $noches = $intervalo->days;


    try {
        $stmt = $db->prepare("SELECT * FROM hospedaje
        WHERE nombre_hospedaje = :nombre_hospedaje AND ubicacion = :ubicacion_hospedaje
        AND fecha_checkin = :fecha_checkin AND fecha_checkout = :fecha_checkout");
        $stmt->bindParam(':nombre_hospedaje', $nombre_hospedaje);
        $stmt->bindParam(':ubicacion_hospedaje', $ubicacion_hospedaje);
        $stmt->bindParam(':fecha_checkin', $fecha_checkin);
        $stmt->bindParam(':fecha_checkout', $fecha_checkout);
        $stmt->execute();

        $hospedaje = $stmt->fetch();

        if (!$hospedaje) {
            $_SESSION['form_data'] = $_POST;
            $_SESSION["mensaje"] = 'No se encontró hospedaje con esos datos.';
            header('Location: agregar_reserva.php?agenda_id=' . urlencode($agenda_id));
            exit();
            }

        $reserva_id = $hospedaje['id'] ?? null;
        $fecha = $hospedaje['fecha_checkin'] ?? null;
        $precio_noche = $hospedaje['precio_noche'] ?? null;
        $monto = $precio_noche * $noches;
        $puntos = $monto / 1000;

        $stmt = $db->prepare("UPDATE reserva SET
            fecha = :fecha, monto = :monto, estado_disponibilidad = 'No disponible', puntos = :puntos, agenda_id = :agenda_id
            WHERE id = :reserva_id");
        $stmt->bindParam(':fecha', $fecha);
        $stmt->bindParam(':monto', $monto);
        $stmt->bindParam(':puntos', $puntos);
        $stmt->bindParam(':agenda_id', $agenda_id);
        $stmt->bindParam(':reserva_id', $reserva_id);
        $stmt->execute();

        $_SESSION["mensaje"] = 'Reserva de hospedaje agregada correctamente';
        header('Location: agregar_reserva.php?agenda_id=' . urlencode($agenda_id));
        exit();

    } catch (PDOException $e) {
        $_SESSION['form_data'] = $_POST;
        $_SESSION["mensaje"] = 'Error al agregar la reserva de hospedaje: ' . $e->getMessage();
        header('Location: agregar_reserva.php?mensaje=' . urlencode($mensaje));
        exit();
    }

// transporte
} elseif ($tipo_reserva == "transporte") {
    $origen = $_POST['lugar_origen'] ?? '';
    $destino = $_POST['lugar_llegada'] ?? '';
    $fecha_salida = $_POST['fecha_salida'] ?? '';
    $fecha_llegada = $_POST['fecha_llegada'] ?? '';
    $cantidad_personas = (int)($_POST['cantidad_personas'] ?? 1);
    
    $stmt = $db->prepare("SELECT * FROM transporte WHERE lugar_origen = :origen AND lugar_llegada = :destino
    AND fecha_salida = :fecha_salida AND fecha_llegada = :fecha_llegada");
    $stmt->bindParam(':origen', $origen);
    $stmt->bindParam(':destino', $destino);
    $stmt->bindParam(':fecha_salida', $fecha_salida);
    $stmt->bindParam(':fecha_llegada', $fecha_llegada);
    $stmt->execute();

    $transporte = $stmt->fetch();
    if (!$transporte) {
        $_SESSION['form_data'] = $_POST;
        $_SESSION["mensaje"] = 'No se encontró transporte con esos datos.';
        header('Location: agregar_reserva.php?agenda_id=' . urlencode($agenda_id));
        exit();
    }

    $reserva_id = $transporte['id'] ?? null;
    $fecha = $transporte['fecha_salida'] ?? null;
    $precio_asiento = $transporte['precio_asiento'] ?? null;
    $monto = $precio_asiento * $cantidad_personas;
    $puntos = $monto / 1000;

    try {
    $stmt = $db->prepare("UPDATE reserva SET
        fecha = :fecha, monto = :monto, estado_disponibilidad = 'No disponible', puntos = :puntos, agenda_id = :agenda_id
        WHERE id = :reserva_id");
    $stmt->bindParam(':fecha', $fecha);
    $stmt->bindParam(':monto', $monto);
    $stmt->bindParam(':puntos', $puntos);
    $stmt->bindParam(':agenda_id', $agenda_id);
    $stmt->bindParam(':reserva_id', $reserva_id);
    $stmt->execute();

    $_SESSION["mensaje"] = 'Reserva de transporte agregada correctamente';
    header('Location: agregar_reserva.php?agenda_id=' . urlencode($agenda_id));
    exit();

    } catch (PDOException $e) {
        $_SESSION['form_data'] = $_POST;
        $_SESSION["mensaje"] = 'Error al agregar la reserva de transporte: ' . $e->getMessage();
        header('Location: agregar_reserva.php?mensaje=' . urlencode($mensaje));
        exit();
    }



// panorama
} elseif ($tipo_reserva == "panorama") {

    $nombre_panorama = $_POST['nombre_panorama'] ?? '';
    $ubicacion_panorama = $_POST['ubicacion_panorama'] ?? '';
    $cantidad_personas = (int)($_POST['cantidad_personas'] ?? 1);
    $fecha_panorama = $_POST['fecha_panorama'] ?? '';


    try {
    $stmt = $db->prepare("SELECT * FROM panorama WHERE nombre = :nombre_panorama
        AND ubicacion = :ubicacion_panorama AND fecha_panorama = :fecha_panorama");
    $stmt->bindParam(':nombre_panorama', $nombre_panorama);
    $stmt->bindParam(':ubicacion_panorama', $ubicacion_panorama);
    $stmt->bindParam(':fecha_panorama', $fecha_panorama);
    $stmt->execute();

    $panorama = $stmt->fetch();

    if (!$panorama) {
        $_SESSION['form_data'] = $_POST;
        $_SESSION["mensaje"] = 'No se encontró panorama con esos datos.';
        header('Location: agregar_reserva.php?agenda_id=' . urlencode($agenda_id));
        exit();
    }

    $stmt = $db->prepare("UPDATE reserva SET
    fecha = :fecha,
    monto = :monto,
    puntos = :puntos,
    estado_disponibilidad = 'No disponible',
    agenda_id = :agenda_id
    WHERE id = :reserva_id");
$stmt->bindParam(':fecha', $fecha);
$stmt->bindParam(':monto', $monto);
$stmt->bindParam(':puntos', $puntos);
$stmt->bindParam(':agenda_id', $agenda_id);
$stmt->bindParam(':reserva_id', $reserva_id);
$stmt->execute();


$panorama_id = $panorama['id'];

foreach ($_POST['participantes'] as $participante) {
    $nombre = $participante['nombre'];
    $edad = $participante['edad'];
    
    $stmt2 = $db->prepare("INSERT INTO participante (panorama_id, nombre, edad) VALUES (:panorama_id, :nombre, :edad)");
    $stmt2->bindParam(':panorama_id', $panorama_id);
    $stmt2->bindParam(':nombre', $nombre);
    $stmt2->bindParam(':edad', $edad);
    $stmt2->execute();
}

$_SESSION["mensaje"] = 'Reserva de panorama agregada correctamente';
header('Location: agregar_reserva.php?agenda_id=' . urlencode($agenda_id));
exit();

    } catch (PDOException $e) {
        $_SESSION['form_data'] = $_POST;
        $_SESSION["mensaje"] = 'Error al agregar la reserva de panorama: ' . $e->getMessage();
        header('Location: agregar_reserva.php?mensaje=' . urlencode($mensaje));
        exit();
    }

}


    try {
        $stmt = $db->prepare("SELECT * FROM reserva WHERE id = :reserva_id");
        $stmt->bindParam(':reserva_id', $reserva_id);
        $stmt->execute();

        $reserva = $stmt->fetch();

        if (!$reserva) {
            $_SESSION['form_data'] = $_POST;
            $_SESSION["mensaje"] = 'No se encontró reserva con ese ID.';
            header('Location: agregar_reserva.php?agenda_id=' . urlencode($agenda_id));
            exit();
        }

        // Actualizar la reserva
        $fecha = $reserva['fecha'] ?? null;
        $monto = $reserva['monto'] ?? null;
        $puntos = $monto / 1000;

        $stmt = $db->prepare("UPDATE reserva SET
            fecha = :fecha, monto = :monto, estado_disponibilidad = 'No disponible', puntos = :puntos, agenda_id = :agenda_id
            WHERE id = :reserva_id");
        $stmt->bindParam(':fecha', $fecha);
        $stmt->bindParam(':monto', $monto);
        $stmt->bindParam(':puntos', $puntos);
        $stmt->bindParam(':agenda_id', $agenda_id);
        $stmt->bindParam(':reserva_id', $reserva_id);
        $stmt->execute();

        $_SESSION["mensaje"] = 'Reserva agregada correctamente';
        header('Location: agregar_reserva.php?agenda_id=' . urlencode($agenda_id));
        exit();

    } catch (PDOException $e) {
        $_SESSION['form_data'] = $_POST;
        $_SESSION["mensaje"] = 'Error al agregar la reserva por ID: ' . $e->getMessage();
        header('Location: agregar_reserva.php?mensaje=' . urlencode($mensaje));
        exit();
}
