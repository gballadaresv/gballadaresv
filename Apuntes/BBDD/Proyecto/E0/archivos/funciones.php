<?php

function str_formatter($str){
    $str = str_replace("\"", "", $str);
    return $str;
}

// run (no nulo)
function run_formatter($run){
    $format1 = "/^\d{1,2}\.?\d{3}\.?\d{3}$/";
    $format2 = "/^\d{1,8}$/";
    if (preg_match($format1, $run)){
        return str_replace(".", "", $run);
    } elseif (preg_match($format2, $run)){
        return $run;
    } else {
        return "00000000";
    }
}


// dv (no nulo)
function dv_formatter($run, $dv){
    if ($dv != "") {
        return $dv;
    }
    $run_a = str_split(strrev($run));
    $sum = 0;
    $len = count($run_a);
    $i = 0;
    $p = 2;
    while ($i < $len){
        $sum += intval($run_a[$i]) * $p;
        if ($p == 7){
            $p = 2;
        } else {
            $p++;
        }
        $i++;
    }
    $div = intdiv($sum, 11);
    $mod = $sum % 11;
    $dv = 11 - $mod;
    if ($dv == 11){
        return strval(0);
    } elseif ($dv == 10){
        return "K";
    } else {
        return strval($dv);
    }
}

// correo (no nulo)
function email_formatter($email){
    $format = "/^[a-zA-Z0-9._-]*[a-zA-Z]+[a-zA-Z0-9._-]*$/";
    $domains = [
        "viajes.cl",
        "tourket.com",
        "wass.com",
        "marmol.com",
        "edbus.cal",
        "outluc.com",
        "viajesanma.com"
    ];
    if (substr_count($email, "@") == 1){
        $parts = explode("@", $email);
        $body = $parts[0];
        $domain = end($parts);
        if (preg_match($format, $body) and in_array($domain, $domains)){
            return $email;
        } else {
            return "invalid@null.nill";
        }
    } else {
        return "invalid@null.nill";
    }
}


// telefono (no nulo)
function phone_formatter($phone){
    $format1 = "/^\+\d{1,3} \d \d{4} \d{4}$/";
    $format2 = "/^\+\d{1,3}-\d-\d{4}-\d{4}$/";
    if (preg_match($format1, $phone)){
        return $phone;
    } elseif (preg_match($format2, $phone)){
        return str_replace("-", " ", $phone);
    } else {
        return "+00 0 0000 0000";
    }
}

// codigo agenda (no nulo)
function check_agenda($agenda){
    if ($agenda != ""){
        return $agenda;
    }
    return 00000;
}


// codigo reserva (no nulo)
function check_reservation($reservation){
    if ($reservation != ""){
        return $reservation;
    }
    return 000000;
}

// fecha
function date_formatter($date){
    $format1 = "/^\d{4}-\d{2}-\d{2}$/";
    $format2 = "/^\d{4}\/\d{2}\/\d{2}$/";
    if (preg_match($format1, $date)){
        return $date;
    } elseif (preg_match($format2, $date)){
        return str_replace("/", "-", $date);
    } else {
        return "0000-00-00";
    }
}


// monto (no nulo)
function price_valid($price){
    if ($price == ""){
        return 0;
    }elseif (floatval($price) >= 0) {
        return $price;
    } else {
        return $price * -1;
    }
}


// numero viaje (no nulo)
function check_trip($trip){
    if (intval($trip) >= 0){
        return $trip;
    } else {
        return 0;
    }
}


// precio asiento (no nulo)
function seat_price_valid($price){
    if (intval($price) >= 0) {
        return $price;
    } else {
        return 0;
    }
}

function str_valid($str){
    $format = "/^[a-zA-Z]*$/";
    if (preg_match($format, $str)){
        return $str;
    } else {
        return "";
    }
}

// validaciones
function person_ok($person){
    if ($person[1] == "00000000" ||
        $person[3] == "invalid@null.nill" ||
        $person[6] == "+00 0 0000 0000"){
        return false;
    } else {
        return true;
    }
}

function agenda_ok($agenda){
    if ($agenda[0] == "invalid@null.nill" || $agenda[1] == 000000){
        return false;
    } else {
        return true;
    }
}

function employee_ok($employee){
    if ($employee[1] == "00000000" ||
        $employee[3] == "invalid@null.nill" ||
        $employee[5] == "" ||
        $employee[6] == "+00 0 0000 0000"){
        return false;
    } else {
        return true;
    }
}

function reserve_ok($reserve){
    if ($reserve[1] == 000000 ||
        $reserve[3] == 0){
        return false;
    } else {
        return true;
    }
}

function transport_ok($transport){
    if ($transport[0] == "ingalid@null.nill" ||
        $transport[1] == 000000 ||
        $transport[2] == 0 ||
        $transport[7] == 0){
        return false;
    } else {
        return true;
    }
}

?>