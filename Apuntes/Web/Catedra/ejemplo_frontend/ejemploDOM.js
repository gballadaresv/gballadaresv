
/**************************************************************************************************************
Pequeño programa que mezcla HTML con JS y CSS y muestra su comportamiento
**************************************************************************************************************/


/*
 Reviso si hay cambios guardados y los muestro inmediatamente en el HTML que se presenta.
 Para eso uso la función cargarCambios(). Nota: la invoco antes de que se defina... comentarios?
*/

cargarCambios();

/*
 En nuestro HTML tenemos varios botones, para manejarlos los asocio a variables,
 para identificarlos SIN ambigüedad cada botón tiee un ID único y ese es el que buscamos,
 para eso, la magia la hace "document.getElementById".
*/

let botonCreaDivNuevo    = document.getElementById("creadivnuevo");
let botonCreaLiEnOl      = document.getElementById("crealienol");       
let botonCreaTxtNuevo    = document.getElementById("creatextonuevo");   
let botonMuestaInnerHTML = document.getElementById("muestrainnerhtml"); 
let botonMuestaInnerText = document.getElementById("muestrainnertext"); 
let botonGrabaCambios    = document.getElementById("grabaloscambios");  

/* 
Para saber cuando se hace click en algún botón, hay que asociar ese elemento, almacenado en una variable,
a un "listener" específico. Este "listener" estará escuchando hasta que alguien haga algo, es ecir hasta que se emita 
un evento. Hay decenas de eventos, pero nosotros lo asociamos al evento "click" sobre el elemento.
Al hacer "click", se llama a la funcion que está declarada.
La magia lo hace el método addEventListener que recibe el evento y lo asocia a la función a invocar cuando ocurra el evento.
*/

//Agregamos listener al click a todos los botones y les asociamos funciones (para que pase algo!)

botonCreaDivNuevo.addEventListener("click", creaElementoDIV);
botonCreaLiEnOl.addEventListener("click", creaLienOl);
botonCreaTxtNuevo.addEventListener("click", agregaTextoDiv);
botonMuestaInnerHTML.addEventListener("click", muestraInnerHTML);
botonMuestaInnerText.addEventListener("click", muestraInnerText);
botonGrabaCambios.addEventListener("click", grabaCambios);

// Hay otros eventos, como "mouseover", "mouseout", "keydown", "keyup", "load", "dblclick", etc.
// Para un drag and drop hay varios eventos asociados, como "dragstart", "dragover", "drop", etc.

//El objetivo es crear un nuevo DIV en nuestra página

function creaElementoDIV() {

// el Div lo dejaremos asociado  fuera del área de trabajo.
    let nuevoDiv = document.createElement("div");
    
    document.body.appendChild(nuevoDiv);
    nuevoDiv.id = "EsteEsnuevo";
    /*let nuevoTexto = document.createTextNode(varTexto);
    var entradaTexto = document.getElementById("textoIngresado");
    var textoEnElemento = entradaTexto.value;
    
    nuevaEntradaEnLista(textoEnElemento, false);*/
}


function creaLienOl() {

   // A la lista ordenada la asociamos a una variable:

    let lista= document.getElementById("lista");

	//La lista se creará como lista ordenada. Se añade un elemento "li" pues hay una nueva linea/elemento.

    let nuevoLi = document.createElement("li");
    nuevoLi.id = "nuevo"

    /*
    En JavaScript, un textNode es un contenedor para texto que se asociará a un elemento HTML.
    En este caso, el nodo se cargará con la información del parámetro "varTexto"
    */

    let nuevoTexto = document.createTextNode("Un nuevo elemento desde JS - DOM");
    
    /*
     Tenemos este nuevo elemento "li" y nuestro nodo de texto lo añadimos al elemento. 
     es algo asi como decir <li> = "texto"
    */
    
    nuevoLi.appendChild(nuevoTexto);
    
    // ese li esta "dando vueltas en el universo" asi que lo asociamos el li que corresponde

    lista.appendChild(nuevoLi); //El elemento <li> se añade o inserta en la lista ordenda.
}

function agregaTextoDiv() {

    // Se atreven? Se parece a nuestro nuevo li en ol
}


//La siguiente funcion, Borra los elementos con clase borrable.

function muestraInnerHTML() {


   let lista = document.getElementById("lista");

   alert(lista.innerHTML)

}

function muestraInnerText() {


   let lista = document.getElementById("lista");

   alert(lista.innerText)

}

//Almacenemos la lista utilizando LocalStorage...que eso es equivalente a almacenar en el cliente...

/*Primero: almacenemos la lista y para eso usaremos un objeto Array() y su metodo push() que ya vimos.
Luego una funcion recorrerá el arreglo y grabará. 
*/

function grabaCambios() {

    let arrCambios = new Array(); //usamos new! para un objeto.

    let lista = document.getElementById("lista"); // La lista ordenada <ol> que tiene elementos guardables.

    for (let i = 0; i < lista.children.length; i++) {

        let el_LI = lista.children.item(i); //Obtengo el <li> del <ol>

        if (el_LI.id === "nuevo") { //Solo para los elementos nuevos

        //Creamos un objeto
            let objetoParaGrabar = {
              texto: el_LI.innerText, 
              id: el_LI.id
            }; 
    
            arrCambios.push(objetoParaGrabar); //se agrega al arreglo de cambios un objeto.
        }

    } // fin del ciclo for

    //El metodo stringyfy transforma arreglo y lo deja como string de tipo JSON.

    localStorage.setItem("ejemploDOM", JSON.stringify(arrCambios)); // localStorage
    
}

//Esto recupera lo que tengamos grabado en localStorage bajo el nombre "ejemploDOM"

function cargarCambios() { 

  if (localStorage.getItem("ejemploDOM") != null) {
  	
      let objListado = JSON.parse(localStorage.getItem("ejemploDOM")); 
      
      let lista= document.getElementById("lista");

        for (let i = 0; i < objListado.length; i++) {
             
            let elementoLI = objListado[i];  // el elementoLI es un objeto, no olvidar. 
            if (elementoLI.id === "nuevo") {
                
                let nuevoLi = document.createElement("li");
                nuevoLi.id = elementoLI.id;
                nuevoLi.innerText = elementoLI.texto;
                lista.appendChild(nuevoLi)
            }
             
        }
    }
}