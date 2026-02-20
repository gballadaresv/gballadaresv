### Resumen
El patrón observer permite que un objeto Subject notifique a los objetos Observer cada vez que haya un cambio en su estado. Puede añadir, eliminar y notificar observadores.

La clase Observer define la interfaz de actualización de los observers. Generalmente consiste de sólo un método update con algunos parámetros opcionales.

La clase ConcreteObserver implementa la lógica detrás de la observación de eventos y reacciona ante los mismos

### Observaciones
* La lista de suscriptores (observadores) es dinámica.