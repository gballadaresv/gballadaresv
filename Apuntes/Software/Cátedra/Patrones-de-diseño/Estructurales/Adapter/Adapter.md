### Resumen
Es un objeto que permite adaptar el formato de "algo" a un formato compatible al resto del código. No necesariamente son sólo datos, 
también puede adaptar una interfaz o incluso requests a otro objeto.

El cliente es el que trae la lógica del programa, la clase Target define la interfaz (estructura) del retorno esperado por el usuario, (puede implementar algo de lógica).

La clase Adaptee contiene al objeto que ha de ser adaptado, mientras que Adapter (que hereda de Target) es la clase que efectivamente se encarga de hacer la traducción, notar que existe una agregación desde Adapter hacia Adaptee.

### Observaciones
* Es posible crear un adaptador bidireccional que transforme en ambas direcciones.

* Hay 2 tipos de adaptadores:

    - Adaptador de objetos: 
        Usa el principio de composición de objetos. Guarda la instancia de 

    - Adaptador de clase: 
        Sólo se puede implementar en lenguajes que soporten multiherencia. 