<?php

// 1
function leer_archivo($archivo) {
    while (!feof($archivo)) {
        $linea = fgets($archivo);
        echo $linea;
    }
}

// 2
function elim_dups($lista){
    $lista2 = [];
    foreach ($lista as $item) {
        if (!in_array($item, $lista2)) {
            $lista2[] = $item;
        }
    }
    return $lista2;
}

// 3
function escribir($nombre, $lista) {
    $archivo = fopen($nombre, "w");
    fputcsv($archivo, $lista);
    fclose($archivo);
}

// 4
function print_lista($lista) {
    echo "lista: [\n";
    foreach ($lista as $item) {
        echo $item . "," , "\n";
    }
    echo "]\n";
}

//1
$archivo = fopen("ayudantia2-1.csv", "r");
leer_archivo($archivo);
fclose($archivo);

//2
$lista = [["Laptop",1200], ["Mouse",20], ["Teclado",50], ["Laptop",1200], ["Monitor",300]];
print_r(elim_dups($lista));
echo "\n";

// 3
$lista = ["Hola mundo", "PHP es genial", "Hello world", "Aprender a programar"];
escribir("Aa.csv", $lista);

// 4
print_lista($lista);

?>