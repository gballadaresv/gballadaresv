const fs = require('fs').promises;

function readargs(argv = process.argv.slice(2)) {
    if (argv.length < 2) {
        console.error("Uso: node tarea2_2262595J.js <archivo1.json> <archivo2.json>");
        process.exit(1);
    }
    return argv;
}

function libro_valid(libro) {
    if (!("autor" in libro) || !("titulo" in libro)) {
        return false;
    } else if (typeof libro.autor !== "string" || typeof libro.titulo !== "string") {
        return false;
    } else if (libro.autor.length === 0 || libro.titulo.length === 0) {
        return false;
    } else {
        return true;
    }
}

function remove_duplicates(libros) {
    const uniques = [];

    for (const libro of libros) {
        const exists = uniques.find(l => l.autor === libro.autor && l.titulo === libro.titulo);
        if (!exists) {
            uniques.push(libro);
        }
    }
    return uniques;
}

async function main() {
    const [file1, file2] = readargs();
    const libros1_json = await fs.readFile(file1, 'utf8');
    const libros2_json = await fs.readFile(file2, 'utf8');

    const libros1 = JSON.parse(libros1_json);
    const libros2 = JSON.parse(libros2_json);

    const qread1 = libros1.length;
    const qread2 = libros2.length;

    const libros = [...libros1, ...libros2];

    const libros_unique = remove_duplicates(libros);

    const qduplicates = (qread1 + qread2) - libros_unique.length;

    const libros_validos = libros_unique.filter(libro => libro_valid(libro));

    const autores = libros_validos.map(libro => libro.autor);

    await fs.writeFile('./respuestaTarea.json', JSON.stringify(libros_validos));

    console.log("Cantidad de libros leidos del primer archivo:", qread1);
    console.log("Cantidad de libros leidos del segundo archivo:", qread2);
    console.log("Cantidad de libros repetidos totales:", qduplicates);
    
    for (const autor of autores) {
        const q = libros_validos.filter(libro => libro.autor === autor).length;
        // Se consideran sólo libros válidos (con autor y título no vacíos)
        console.log("Cantidad de libros no repetidos del autor", autor + ":", q);
    }

    console.log("Cantidad total de libros en el archivo final:", libros_validos.length);
}

main();

/* 
process.argv es un array de la ruta del archivo ejecutado y los argumentos entregados en la línea de comando 
al ejecutar el archivo, similar a sys.argv en Python.

process.exit() interrumpe y termina la ejecución del programa, con un código que indica si fue terminado 
de forma exitosa o con error.
*/