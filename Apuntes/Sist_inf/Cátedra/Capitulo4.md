# Procesos de negocios y áreas funcionales.

### Matriz RACI
- Responsable: aquel que ejecuta la tarea.
- Aprobador: aquel que supervisa la tarea.
- Consultor: aquel que asesora en la tarea.
- Informado: aquel al que se informa de la tarea.

### Diagrama SIPOC
- Suppliers. (proveen inputs)
- Inputs.
- Processes.
- Outputs.
- Customers. (reciben outputs)

# Modelos de procesos de negocios

### Tipos de modelos de procesos
##### BPMN (Buisness Process Model and Notation):
Es como un UML para modelar procesos.

Eventos iniciales se modelan en un círculo con borde delgado, los eventos intermedios con doble borde, y los eventos finales con un borde grueso.

Las tareas se representan como rectángulos de bordes redondeados, y los subprocesos se representan como tareas, con un cuadradito con un signo "+" abajo.

Las secuencias son flechas, las asociaciones con líneas punteadas, y los flujos de mensajes con  una línea punteada con un círculo y un triángulo en los bordes.

Las compuretas de enlace se representan con rombos:
- Vacío: No
- X: Si
- Círculo: Inclusivo
- +: Paralelo
- *: Complejo
- Con un evento: Basado en evento.

*Después de una compuerta de eventos necesariamente tienen que haber eventos.

Importante: contexto, alcance, modelo, entender el problema (estudiar).

Los procesos se modelan en un "pool", como un environment que indica el nombre del proceso, y se puede dividir en swimlanes.

Pueden haber artefactos (elementos que pueden ser parte del proceso, como un documento o una bbdd)

*También se pueden modelar errores (con un rayo) y escalamientos (como una flecha de waze con borde punteado).
*Se le pueden poner "decoraciones" a las actividades.
*Cuando uno indica un subproceso, eventualmente se tendrá que modelar también, pues se está "referenciando".


