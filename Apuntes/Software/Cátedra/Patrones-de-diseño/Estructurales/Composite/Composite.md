### Resumen
Se utiliza cuando la estructura del diseño se puede representar como un árbol. Tiene un comportamiento recursivo a medida que se baja por las ramas hasta llegar a las hojas.

Cada vez que se haga una request, son los padres los que se encargan de pasarla a los hijos.

La clase abstracta Component define la interfaz (estructura con la que se definirán las subclases), define el comportamiento de tanto los elementos complejos (ramas) como de los simples (hojas).

La clase Leaf representa los objetos finales que van al término de las ramas del árbol, nótese que no tiene más sub-elementos, generalmente son quienes hacen todo el trabajo lógico.

La clase Composite (contenedor) es un elemento que tiene sub-elementos (hojas u otros contenedores). No sabe ni le interesa la clase de sus hijos, debe ser capaz de agregar hijos, eliminar hijos, delegar requests y retornar el resultado final.

### Observaciones
* No es tan relevante conocer los objetos que componen el árbol, tampoco saber si un nodo tiene hijos o si es hoja.

* Los objetos Composite se limitan al manejo de hijos, pasar las requests y retornar el resultado.  