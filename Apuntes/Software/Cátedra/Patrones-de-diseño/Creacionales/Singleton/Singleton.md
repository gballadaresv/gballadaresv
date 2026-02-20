### Resumen
Singleton es un patrón de diseño creacional que consiste en crear una única instancia de una clase. Esto se logra haciendo que el creador de la instancia sea un método privado y manejando un getter para la instancia

### Observaciones
* La clase debe chequear si es que existe una instancia, de no existir la crea, en caso contrario, debe retornar el objeto.

* Es difícil de testear, pues los tests suelen crear objetos de prueba, por lo que se debe pensar en otra forma de hacer los tests.

* Requiere especial atención en ambientes donde se trabaje con múltilpes threads.

* En Ruby se maneja como una variable de clase (@@), para verificar si la instancia fue creado se puede hacer con el operador ||= (Si es falso, define).

* Recordar  que el contructor (new) debe ser privado.