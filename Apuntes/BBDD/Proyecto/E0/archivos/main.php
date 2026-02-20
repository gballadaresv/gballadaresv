<?php
require "funciones.php";

// create files
$personas = fopen("../CSV_limpios/personasOK.csv", "w");
$usuarios = fopen("../CSV_limpios/usuariosOK.csv", "w");
$empleados = fopen("../CSV_limpios/empleadosOK.csv", "w");
$agendas = fopen("../CSV_limpios/agendaOK.csv", "w");
$reservas = fopen("../CSV_limpios/reservasOK.csv", "w");
$transportes = fopen("../CSV_limpios/transportesOK.csv", "w");
$buses = fopen("../CSV_limpios/busesOK.csv", "w");
$trenes = fopen("../CSV_limpios/trenesOK.csv", "w");
$aviones = fopen("../CSV_limpios/avionesOK.csv", "w");
$u_descartados = fopen("../CSV_limpios/datos_descartados_usuarios.csv", "w");
$e_descartados = fopen("../CSV_limpios/datos_descartados_empleados.csv", "w");

// add headers
fputcsv($personas, ["nombre", "run", "dv", "correo", "contrasena", "nombre_usuario", "telefono_contacto"]);
fputcsv($usuarios, ["nombre", "run", "dv", "correo", "contrasena", "nombre_usuario", "telefono_contacto", "puntos"]);
fputcsv($empleados, ["nombre", "run", "dv", "correo", "contrasena", "nombre_usuario", "telefono_contacto", "jornada",
            "isapre", "contrato"]);
fputcsv($agendas, ["correo_usuario", "codigo_agenda", "etiqueta"]);
fputcsv($reservas, ["codigo_agenda", "codigo_reserva", "fecha", "monto", "cantidad_personas", "estado_disponibilidad"]);
fputcsv($transportes, ["correo_empleado", "codigo_reserva", "numero_viaje", "lugar_origen", "lugar_llegada", "capacidad",
            "tiempo_estimado", "precio_asiento", "empresa", "fecha_salida", "fecha_llegada"]);
fputcsv($buses, ["correo_empleado", "codigo_reserva", "numero_viaje", "lugar_origen", "lugar_llegada", "capacidad",
            "tiempo_estimado", "precio_asiento", "empresa", "tipo_de_bus", "comodidades", "fecha_salida", "fecha_llegada"]);
fputcsv($trenes, ["correo_empleado", "codigo_reserva", "numero_viaje", "lugar_origen", "lugar_llegada", "capacidad",
            "tiempo_estimado", "precio_asiento", "empresa", "comodidades", "paradas", "fecha_salida", "fecha_llegada"]);
fputcsv($aviones, ["correo_empleado", "codigo_reserva", "numero_viaje", "lugar_origen", "lugar_llegada", "capacidad",
            "tiempo_estimado", "precio_asiento", "empresa", "escalas", "clase", "fecha_salida", "fecha_llegada"]);
fputcsv($u_descartados, ["nombre", "run", "dv", "correo", "nombre_usuario", "contrasena", "telefono_contacto", "puntos",
            "codigo_agenda", "etiqueta", "reserva", "fecha", "monto", "cantidad_personas"]);
fputcsv($e_descartados, ["nombre", "run", "dv", "correo", "nombre_usuario", "contrasena", "telefono_contacto", "jornada",
            "isapre", "contrato", "codigo_reserva", "codigo_agenda", "fecha", "monto", "cantidad_personas",
            "estado_disponibilidad", "numero_viaje", "lugar_origen", "lugar_llegada", "fecha_salida", "fecha_llegada",
            "capacidad", "tiempo_estimado", "precio_asiento", "empresa", "tipo_de_bus", "comodidades", "escalas", "paradas"]);



// read users
$users = fopen("../CSV_sucios/usuarios_rescatados.csv", "r");

fgets($users);
while (!feof($users)) {
    $line = fgetcsv($users);
    if ($line == false) {
        continue;
    }

    // extraer datos de usuario
    $name = $line[0];
    $run = $line[1];
    $dv = $line[2];
    $email = $line[3];
    $username = $line[4];
    $password = $line[5];
    $phone = $line[6];
    $points = $line[7];
    $agenda = $line[8];
    $etiqueta = $line[9];
    $reservation = $line[10];
    $date = $line[11];
    $price = $line[12];
    $people = $line[13];

    $send_person = false;
    $send_user = false;
    $send_agenda = false;

    // personas
    $persona = [
        str_formatter($name),
        run_formatter($run),
        dv_formatter($run, $dv),
        email_formatter($email),
        $password,
        $username,
        phone_formatter(str_formatter($phone))
    ];
    if (person_ok($persona)){
        fputcsv($personas, $persona);
        $send_person = true;
    }
    
    // usuarios
    $usuario = [
        str_formatter($name),
        run_formatter($run),
        dv_formatter($run, $dv),
        email_formatter($email),
        $username,
        $password,
        phone_formatter(str_formatter($phone)),
        $points
    ];
    if (person_ok($usuario)){
        fputcsv($usuarios, $usuario);
        $send_user = true;
    }
    
    // agenda
    $c_agenda = [
        email_formatter($email),
        check_agenda($agenda),
        str_formatter($etiqueta)
    ];
    if (agenda_ok($c_agenda)){
        fputcsv($agendas, $c_agenda);
        $send_agenda = true;
    }


    if ($send_person == false && $send_user == false && $send_agenda == false){
        fputcsv($u_descartados, [
            str_formatter($name),
            run_formatter($run),
            dv_formatter($run, $dv),
            email_formatter($email),
            $username,
            $password,
            phone_formatter(str_formatter($phone)),
            $points,
            check_agenda($agenda),
            str_formatter($etiqueta),
            check_reservation($reservation),
            date_formatter($date),
            price_valid($price),
            $people
        ]);
    }
}
fclose($users);


// read employees
$employees = fopen("../CSV_sucios/empleados_rescatados.csv", "r");
fgets($employees);
while (!feof($employees)) {
    $line = fgetcsv($employees);
    if ($line == false) {
        continue;
    }

    $save_person = false;
    $save_employee = false;
    $save_reserve = false;
    $save_transport = false;
    $save_bus = false;
    $save_train = false;
    $save_plane = false;
    
    $name = $line[0];
    $run = $line[1];
    $dv = $line[2];
    $email = $line[3];
    $username = $line[4];
    $password = $line[5];
    $phone = $line[6];
    $shift = $line[7];
    $isapre = $line[8];
    $contract = $line[9];
    $reservation = $line[10];
    $agenda = $line[11]; 
    $date = $line[12];
    $price = $line[13];
    $people = $line[14];
    $available = $line[15];
    $trip = $line[16];
    $origin = $line[17];
    $destination = $line[18];
    $departure_date = $line[19];
    $arrival_date = $line[20];
    $capacity = $line[21];
    $time = $line[22];
    $seat_price = $line[23];
    $company = $line[24];
    $bus_type = $line[25];
    $comodities = $line[26];
    $scales = $line[27];
    $class = $line[28];
    $stations = $line[29];


    // personas
    $persona = [
        str_formatter($name),
        run_formatter($run),
        dv_formatter($run, $dv),
        email_formatter($email),
        $username,
        $password,
        phone_formatter(str_formatter($phone))
    ];
    if (person_ok($persona)){
        fputcsv($personas, $persona);
        $save_person = true;
    }


    // empleados
    $empleado = [
        str_formatter($name),
        run_formatter($run),
        dv_formatter($run, $dv),
        email_formatter($email),
        $username,
        $password,
        phone_formatter(str_formatter($phone)),
        $shift,
        $isapre,
        str_formatter($contract)
    ];
    if (employee_ok($empleado)){
        fputcsv($empleados, $empleado);
        $save_employee = true;
    }


    // reservas
    $reserva = [
        check_agenda($agenda),
        check_reservation($reservation),
        date_formatter($date),
        price_valid($price),
        $people,
        $available
    ];
    if (reserve_ok($reserva)){
        fputcsv($reservas, $reserva);
        $save_reserve = true;
    }


    // transportes
    $transporte = [
        email_formatter($email),
        check_reservation($reservation),
        check_trip($trip),
        str_valid($origin),
        str_valid($destination),
        $capacity,
        $time,
        price_valid($seat_price),
        $company,
        date_formatter($departure_date),
        date_formatter($arrival_date)
    ];
    if (transport_ok($transporte)){
        fputcsv($transportes, $transporte);
        $save_transport = true;
    }


    // buses
    $bus = [
        email_formatter($email),
        check_reservation($reservation),
        check_trip($trip),
        str_valid($origin),
        str_valid($destination),
        $capacity,
        $time,
        price_valid($seat_price),
        $company,
        $bus_type,
        $comodities,
        date_formatter($departure_date),
        date_formatter($arrival_date)
    ];
    if (transport_ok($bus) && $bus[9] != ""){
        fputcsv($buses, $bus);
        $save_bus = true;
    }


    // trenes
    $tren = [
        email_formatter($email),
        check_reservation($reservation),
        check_trip($trip),
        str_valid($origin),
        str_valid($destination),
        $capacity,
        $time,
        price_valid($seat_price),
        $company,
        $comodities,
        $stations,
        date_formatter($departure_date),
        date_formatter($arrival_date)
    ];
    if (transport_ok($tren) && $tren[10] != "{}"){
        fputcsv($trenes, $tren);
        $save_train = true;
    }


    // aviones
    $avion = [
        email_formatter($email),
        check_reservation($reservation),
        check_trip($trip),
        str_valid($origin),
        str_valid($destination),
        $capacity,
        $time,
        price_valid($seat_price),
        $company,
        $scales,
        $class,
        date_formatter($departure_date),
        date_formatter($arrival_date)
    ];
    if (transport_ok($avion) && $avion[10] != ""){
        fputcsv($aviones, $avion);
        $save_plane = true;
    }

    if ($save_person == false && $save_employee == false && $save_reserve == false && $save_transport == false 
        && $save_bus == false && $save_train == false && $save_plane == false){
        fputcsv($e_descartados, [
            str_formatter($name),
            run_formatter($run),
            dv_formatter($run, $dv),
            email_formatter($email),
            $username,
            $password,
            phone_formatter(str_formatter($phone)),
            $shift,
            $isapre,
            str_formatter($contract),
            check_reservation($reservation),
            check_agenda($agenda),
            date_formatter($date),
            price_valid($price),
            $people,
            $available,
            check_trip($trip),
            str_valid($origin),
            str_valid($destination),
            date_formatter($departure_date),
            date_formatter($arrival_date),
            $capacity,
            $time,
            price_valid($seat_price),
            $company,
            str_valid($bus_type),
            str_valid($comodities),
            str_valid($scales),
            str_valid($class),
            str_valid($stations)
        ]);
    }
}
fclose($employees);


// cerrar archivos generados
fclose($personas);
fclose($usuarios);
fclose($empleados);
fclose($agendas);
fclose($reservas);
fclose($transportes);
fclose($buses);
fclose($trenes);
fclose($aviones);
fclose($u_descartados);
fclose($e_descartados);


?>