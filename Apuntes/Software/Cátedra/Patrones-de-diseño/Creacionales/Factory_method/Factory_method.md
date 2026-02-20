### Resumen
Consiste en una superclase abstracta Factory que establece los métodos que se implementearán en las subclases, puede implementar un poco de lógica para quitar carga de las subclases, pero no crea productos.

Son las subclases FactoryX las que se encargan de efectivamente crear los productos, hace override de los métodos de la Factory original (no necesariamente crea nuevas instantias cada vez, también puede retornar objetos existentes). 

La superclase Product declara la interfaz que todos los productos concretos deberán implementar.

Las subclases ProductX son los productos creados a partir de cada FactoryX, es lo que efectivamente es retornado al cliente y el paso final de ejecución. 

*Nótese que el cliente nunca interactúa con la Factory, sino que interactúa directamente con las FactoryX para obtener el ProductX.

*Nótese que aparte de las herencias, la clase Product dependerá de la clase Factory, si bien son las subclases las que interactúan, al haber herencia se denota que son Factory y Product las que poseen una relación de dependencia.

### Observaciones

* Tiene alta cohesión, pues las funciones de crear objeto (factoring) es dedicada a las clases FactoryX y se separa de los productos.

* Es fácilmente extendible, pues basta con agregar las subclases correspondientes sin tener que editar clases anteriores.

* Puede volverse complejo debido a la cantidad de clases que involucra.

* Con interfaz se refieren a la estructura que tendrá la clase, por lo general se define como una clase abstracta.