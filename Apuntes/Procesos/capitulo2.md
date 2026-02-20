# BPMN

(Buisness Process Model Notation)

##### Actividad
Se representa con un rectángulo de bordes redondos, los nombres con verbo en infinitivo + sustantivo.

La mano en la esquina representa una tarea manual

Si un mensaje se envía de forma manual, se puede colocar un sobre negro en la misma actividad (en vez de un evento de envío de mensaje, que sería un envío de mensaje automatizado).

También hay una actividad con recepción de mensaje.

Las tareas de usuario, se representan con una persona, puede ser la combinación de persona con sistema.

Actividades on engranaje represenat un sistema o automatización.

Hay loops (while).

Hay múltiples instancias en paralelo (líneas verticales) y en serie (líneas horizontales). Se pude aplicar a subprocesos.


##### Flujo de secuencia
Una flecha continua muestra el flujo especificando el orden de ejecución de las actividades.
*Cada instancia de ejecución del proceso es un "token" que recorre el diagrama.

*El flujo por default se representa como la flecha de flujo normal con una línea cruzada, si no se sigue ningún otro flujo, se sigue este.

El flujo condicional (rombo) es un flujo condicional.

##### Pools
Agrupan las distintas organizaciones que forman parte del proceso.

*Los pools abstractos son "cajas negras", no nos interesa lo que hay dentro, sólo nos interesa que está.

##### Swimlanes
Representan los roles dentro de cada pool.

##### Eventos
Son cosas que suceden. afectan el flujo del proceso y tienen causa (trigger) o un efecto.

- Start: círculo.
- Intermediate: doble círculo.
- End: círculo de borde grueso.

Se nombran según sustantivo + verbo participio. Esto denota su naturaleza instantánea.
(Ej: llegada de camión cargado)

Hay muchos tipos de eventos, nos concentraremos en:
- Sin trigger (sólo el círculo)
- Mensaje (carta)
- Termporal (reloj)
- Terminación (círculo negro)

Eventos de recepción son con íconos en blanco, de entrega son en negro.

* Catch: la ejecución se detiene a la espera de ocurrencia del evento.
* Throw: se ejecuta el comportamiento especificado mientras la ejecución continúa.

*Los eventos de envío de mensaje se suelen ocupar para mensajes automáticos.

Es posible adjuntar un evento a una actividad, indicando que si un evento ocurre durante la ejecución de la actividad, se interrumpe la ejecución, y se sigue un flujo de secuencia alternativo.
(Se inserta el evento en el borde del rectángulo, y sale una flecha del círculo del evento.)

*Si en la ejecución de uno de los flujos, el proceso completo termina, se debe usar el evento _terminate_. Se suele usar con flujos paralelos.
*Si un terminate se usa en un subproceso, termina el subproceso y sigue el proceso (actúa sobre su scope).

*Con eventos de fin normal, tienen que llegarse a todos los eventos de término para que termine el proceso.

Hay eventos de error, que se ligan a las actividades, que representan una interrupción de la actividad mediante un error, puede salir un flujo de él.

Hay eventos de señales (triángulo), que puede comunicar "por bluetooth" distintas lanes.

Los eventos condicionales (con un doc? rallado) puede verificar si se cumple alguna condición.

Cuando los eventos están adjuntos en una actividad, línea sólida interrumpe la actividad y se va por el flujo del evento. Con línea punteada no interrumpe, se sigue ejecutando al actividad, y además se abre el nuevo flujo del evento.

##### Gateways
Compuertas lógicas que permiten especificar el flujo de secuencias. Se denotan con rombos.

- Exclusive:
    - Basado en datos: (X)
    - Basado en eventos: (Círculo con pentágono) van seguidos de un evento.

- Paralelo: (+)

- Inclusivo: (círculo) 

- Compleja: (*) 


Splits separan flujos, Joins juntan flujos:
- XOR: (X) 
- AND: (+) 
- OR: (círculo) 
*Existen flujos sin control, pero se considera mala práctica.
*Generalmente se evita el uso de OR, se suele usar XOR y AND.

*Las compuertas de eventos se usar para separar flujos, a cada flujo le debe seguir un evento. Dado que le sugien eventos, no se etiqueta.

##### Subprocesos
Permite definir diferentes niveles de detalle en el diagrama, de manera que un mismo modelo sirva a diferentes públicos.

Se denotan como un actividad con un cuadrado con (+) abajo. Luego se debe expandir y explicar el subproceso.

Un proceso se podría definir como varios subprocesos.

*Que un subproceso termine (independiente de cómo termina), indica que el proceso macro continúa su ejecución.*

*Cuando tiene borde delgado es un subproceso simple (embebido), si tiene borde grueso implica múltiples ejecutores (múltiples lanes).

Los subprocesos ad-hoc (~) indican que las actividades no se ejecutan en un orden específico (las actividades **pueden** estar sin flujo), y se ejecutan una cantidad indeterminada de veces (se debe incluir un evento insertado  en el subproceso).

Los subprocesos de eventos se representan con una línea segmentada (no confundir con grupos de actividades, que son -.-.-.-), se ejecuta el subproceso cuando ocurre un evento (su evento de inicio).

Las transacciones se denotan como un subproceso con doble borde con un círculo arriba a la derecha, tiene 2 eventos de interrupción.

Tipos de subprocesos:
- Normal (embebido)
- De llamada (reutilizable): borde grueso, tiene pools y lanes propios.
- Ad-hoc: sin orden ni cantidad definida de ejecución de las actividades.
- De evento: se inicia con un evento.
- Transacción: if-else break.

##### Flujo de mensaje
Se usa una flecha punteada (inicio con círculo, final con triángulo) para representar la transmisión de información de un Pool a otro. No permite representar flujo de actividades, sólo envío de información.
Se pueden unir pools, swimlanes, subprocesos, actividades y eventos de mensaje.

*Entradas y salidas de SIPOC se relacionan con el flujo de mensajes.

##### Artefactos
Enriquecen el diagrama, muestran información adicional, aunque no son escenciales para el modelamiento.

- Data object: se representa como un documento, representan formularios, información. 

- Grupo: agrupación de actividades, actividad ocn borde semi-punteado. 

- Anotaciones: permite hacer comentarios.

- Asociación: líneas punteadas con flechas no rellenas para denotar flujos de artefactos (no todos tienenq ue salir y entrar, no todos son entradas y salidas.)


*Mientras menos elementos por diagrama mejor, lo hace más leíble, intentar no pasar de 50 elementos.

*Todo flujo debe tener un evento de fin (no puden haber "islas").

En los documentos se puede colocar una flecha blanca o negra dependiendo si entra o sale.

Hay un almacén de datos.

#### Modelamiento

1. Identificar roles:
    - Pools: entidades de negocio.
    - Lanes: ejecutores.
2. Listar actividades
    *Opcional: identificar subprocesos.
3. Identificar eventos.
4. Identificar necesidad de agregar gateways.
    - Caminos alternativos
    - Caminos paralelos
    - Caminos opcionales
5. Bosquejar modelo en papel.
6. Modelar proceso en BPMN.

