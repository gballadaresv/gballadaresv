### Resumen
La idea del patrón decorator es extender el comportamiento de un objeto de forma dinámica, sin abusar de la herencia.

La clase Component define la interfaz común tanto para los wrappers como para los wrappeds.

La clase ConcreteComponent es la clase de los objetos que serán decorados, define la estructura del objeto "stock".

La clase Decorator posee una relación de agregación con Component, delega todo el trabajo al objeto decorado. 

La clase ConcreteDecorator es la que define las extensiones de comportamiento del objeto. Pueden hacer override de métodos del decorador base y ejecutar su propio comportamiento antes o después de llamar a su método padre.

### Observaciones
* No requiere modificar la estructura original del objeto.

* Permite representar estructuras compuestas por capas

* Es difícil eliminar un decorador en particular de la lista de decoradores. 

* Es difícil implementar un decorador tal que no dependa del orden de los decoradores previos.

* Los llamados sobre las operaciones sobre los decoradores es secuencial.