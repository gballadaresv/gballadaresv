<?php
session_start();
require_once 'utils.php';

$usuario = $_POST['usuario'] ?? '';
$contrasena = $_POST['contrasena'] ?? '';

$db = conectarBD();

// Revisar que la persona exista
$query = "SELECT * FROM persona WHERE username = :usuario";
$stmt = $db->prepare($query);
$stmt->bindParam(':usuario', $usuario);
$stmt->execute();

$resultado = $stmt->fetch();

// Revisar que la contraseña sea correcta
$query2 = "SELECT * FROM persona WHERE username = :usuario AND contrasena = :contrasena";
$stmt2 = $db->prepare($query2);
$stmt2->bindParam(':usuario', $usuario);
$stmt2->bindParam(':contrasena', $contrasena);
$stmt2->execute();
$resultado2 = $stmt2->fetch();

// Validar que la persona sea usuario
$query3 = "SELECT * FROM usuario WHERE correo = :correo";
$stmt3 = $db->prepare($query3);
$stmt3->bindParam(':correo', $resultado['correo']);
$stmt3->execute();
$resultado3 = $stmt3->fetch();

if ($resultado && $resultado2 && $resultado3) {
    $_SESSION['usuario'] = $usuario;
    header('Location: main.php');
    exit();
} elseif (!$resultado || !$resultado3) {
    header('Location: index.php?error=Usuario no existe');
    exit();
} elseif ($resultado && !$resultado2) {
    header('Location: index.php?error=Contraseña incorrecta');
    exit();
}
?>
