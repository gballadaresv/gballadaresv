// Nombre completo: Gonzalo Andrés Balladares Velásquez
// Numero alumno: 2262595J

//===== Inicio de Programa =======
const readline = require("readline");
// Incluir el archivo JSON con los contactos
const contactos = require("./agenda.json");
//En “contactos” queda una estructura de arreglo de objetos JS

// Interfaz de usuario que aparece en consola
const entrada = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

function mostrarMenu() {
    console.log("\n--- Agenda de Contactos ---");
    console.log("Gonzalo Andres Balladares Velasquez")
    console.log("1. Listar contactos");
    console.log("2. Buscar contacto");
    console.log("3. Salir");
    entrada.question("\nIngrese opción: ", (opcion) => {
        switch (opcion) {
            case "1":
                listarContactos();
                break;
            case "2":
                buscarContacto();
                break;
            case "3":
                console.log("FIN");
                entrada.close();
                break;
            default:
                console.log("Opción no válida, intente otra vez.");
                mostrarMenu();
            }
        }
    );
}

function listarContactos() {
    for (const i of contactos) {
        console.log("- ", i.nombre, ":", i.telefono);
    }
    mostrarMenu();
}

function buscarContacto() {
    // Funcion find() recuperada de:
    // https://mimo.org/glossary/javascript/array-find
    entrada.question("Ingresa el nombre a buscar: ", (nombre) => {
        const contacto = contactos.find(c => c.nombre === nombre);
        if (contacto) {
            console.log("Telefono de", contacto.nombre, ":", contacto.telefono);
        } else {
            console.log("Contacto no encontrado.");
        }
        mostrarMenu();
    });
}

// Iniciar
mostrarMenu();

