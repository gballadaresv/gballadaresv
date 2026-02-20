<?php
session_start();
require_once 'utils.php';

if (!isset($_SESSION['usuario'])) {
    header('Location: index.php?error=Debes iniciar sesión primero');
    exit();
}

$db = conectarBD();
$usuario = $_SESSION['usuario'];
$agenda_option = $_POST['agenda_option'] ?? '';

$stmt0 = $db->prepare("SELECT correo FROM persona WHERE username = :usuario");
$stmt0->bindParam(':usuario', $usuario);
$stmt0->execute();
$correo_usuario = $stmt0->fetchColumn();
$_SESSION['correo_usuario'] = $correo_usuario;

$mensaje = '';

// Crear nueva agenda
if ($agenda_option === 'nueva') {
    $etiqueta = $_POST['nombre'] ?? '';
    if (empty($etiqueta)) {
        $mensaje = 'El nombre del viaje no puede estar vacío';
        header('Location: crear_viaje.php?mensaje=' . urlencode($mensaje));
        exit();
    } else {
        try {
            $stmt = $db->prepare("INSERT INTO agenda(id, correo_usuario, etiqueta) 
            VALUES (nextval('agenda_id_seq'), :correo_usuario, :etiqueta)");
            $stmt->bindParam(':etiqueta', $etiqueta);
            $stmt->bindParam(':correo_usuario', $correo_usuario);
            $stmt->execute();
            $_SESSION["mensaje"] = 'Agenda creada correctamente';
            $_SESSION['agenda_id'] = $db->lastInsertId();
            header('Location: agregar_reserva.php?agenda_id=' . urlencode($db->lastInsertId()));
            exit();
        } catch (PDOException $e) {
            $mensaje = 'Error al crear la agenda: ' . $e->getMessage();
            header('Location: crear_viaje.php?mensaje=' . urlencode($mensaje));
        }
    }

// Agenda existente
} elseif ($agenda_option === 'existente') {
    $agenda_id = $_POST['agenda_id'] ?? '';
    if (empty($agenda_id)) {
        $mensaje = 'El ID de la agenda no puede estar vacío.';
        header('Location: crear_viaje.php?mensaje=' . urlencode($mensaje));
        exit();
    } else {
        try {
            $stmt = $db->prepare("SELECT * FROM agenda WHERE id = :id AND correo_usuario = :correo_usuario");
            $stmt->bindParam(':id', $agenda_id);
            $stmt->bindParam(':correo_usuario', $correo_usuario);
            $stmt->execute();
            if ($stmt->fetch()) {
                $_SESSION["mensaje"] = 'Agenda encontrada';
                $_SESSION['agenda_id'] = $agenda_id;
                header('Location: agregar_reserva.php?agenda_id=' . urlencode($agenda_id));
                exit();
            } else {
                $mensaje = 'La agenda no existe o no te pertenece';
                header('Location: crear_viaje.php?mensaje=' . urlencode($mensaje));
                exit();
            }
        } catch (PDOException $e) {
            $mensaje = 'Error al procesar la agenda: ' . $e->getMessage();
        }
    }
} else {
    $mensaje = 'Opción de agenda no válida';
}

?>