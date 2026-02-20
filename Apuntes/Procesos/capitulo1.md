# Modelos de procesos de negocio

Un proceso es un conjunto ordenado de pasos que tienen como propósito alcanzar un cierto objetivo.

Un proceso de negocio es un proceso que usa los recursos de la organización para alcanzar un objetivo de la misma.

##### Modelo
Representación abstracta de la realidad. Sirven para simplificar la realidad para poder analizarla.

Todo modelo deja fuera ciertos aspectos de la realidad en favor de aquellos que son relevantes.

*Pretende comunicar, diseñar y ejecutar.

##### Proceso 
Conjunto de acciones que tiene como resultado un cambio en la naturaleza.

##### Negocio
Una organización creada y operada con la intención de generar valor.

*Negación del ocio.

Realiza actividades alineadas con el propósito de creación de valor.


##### Gestión por procesos
Se centra en los objetivos del proceso, donde hay un único responsable. Existe una gestión transversal para lograr los objetivos del proceso, a diferencia de la gestión por funciones, que se centra en los objetivos para cada función (área).

Queremos que todas las áreas trabajen en conjunto en favor de los objetivos, para eso hay que buscar apoyo en la gerencia de las distintas áreas.

### Proceso de negocio
Una instancia de un proceso es una ejecución particular de éste en un momento determinado.
También se denomina _caso_, ya que tiene información única que diferencia una instancia de las demás.
Generalmente se asocia a un cliente único, puede tener información asociada a la entidad que recorre el proceso, y puede tener un id artificial.

*Un proceso debe agregar valor.

#### Roles para el descubrimiento de procesos

- Analista de proceso: Sabe analizar procesod e negocio, por lo general no está familisarizado del proceso a analizar.

- Experto de dominio: Conoce el proceso de negocio, suele ser un ejecutor, pero también puede ser fueño del proceso. También pueden ser proveedores y clientes del proceso.

*Se habla de descubrimiento de procesos, no de definición.


Para escoger un nombre para el proceso:
- Comunica el sentido del proceso.
- Define alcance que entregue valor al cliente.
- Que sea independiente de los recursos utilizados (qué, no cómo).


#### Elementos de un proceso de negocio

- Actividades: cómo
- Participantes: quiénes
    - Ejecutores: quién
    - Proveedores: desde quién
    - Clientes: para quién
- Entidades: qué

##### Actividades
Son los pasos que permiten llevar a cabo la creación de valor del proceso. Requieren de un esfuerzo para ser completados.

(verbo en infinitivo + sustantivo)

##### Participantes
Rol que algo o alguien desempeña en el proceso. Puede ser interno o externo a la organización.
Un mismo participante puede desempeñar varios roles en el proceso.

- Ejecutores: Son los recursos de la organización que realizan las actividades del proceso. Pueden ser personas o sistemas. Tienen capacidad limitada, su trabajo tiene un costo y se clasifican con un enfoque funcional (habilidades, competencias o calificaciones).

    *Interensan los roles, no los cargos o personas particulares.

##### Entidades
Elementos que son utilizados o generados durante la ejecución del proceso. Pueden ir transformándose a medida que avanzan por el proceso. Se refieren al contenido, no al medio. Pueden ser objetos, abstractos o personas.

*Hay que hacer la distinción entre la infraestructura y las entidades del proceso.

- Entradas: Se crean fuera del alcance del proceso, y se utilizan dentro del mismo.
- Salidas: Se crean dentro del proceso, y se utilizan fuera.
- Internas: Se crean y usan dentro del proceso.

##### Cliente
Quien recibe las salidas generadas como resultado del proceso.

- Externos: Suele pagar por el producto o servicio final.
- Interno: Procesos posteriores al proceso.

*Generalmente se consideran ambos tipos de clientes.
*Quien recibe un elemento de una actividad para ejecutar otra dentro del proceso no es cliente.

##### Proveedores
Quien entrega las entradas necesarias para la ejecución del proceso.

- Externos: Empresas externas que entregan insumos o servicios.
- Internos: Procesos anteriores al proceso.

*Quien genera un elemento de una actividad para la ejecución de otra dentro del proceso no es proveedor.

### Herramientas para el descubrimiento de procesos

##### Matriz de descubrimiento

- Nombre del proceso: verbo en infinitivo, descriptivo y entendible.
- Parte cuando: Cuando se gatilla o parte?
- Termina cuando: Después de qué se puede dar por terminado? (No necesariamente cuando se le entrga valor al cliente, puede haber una activida de cierre)
- Áreas involucradas: Qué áreas o ejecutores se ven incolucrados?
- Volumen y periodicidad: Cuánteas veces se ejecuta? Cada cuánto tiempo?

##### SIPOC

Proviene de una etapa "definir" de la metodología Six Sigma.
Ayuda a entender qué es lo que llega al proceso, y lo que sale del mismo.

- Suppliers: proveen las entradas.
- Inputs: creadas fuera del proceso.
- Process.
- Output: creado dentro del proceso.
- Customers: reciben las salidas.

1. Identificar entre 4 y 6 etapas de alto nivel.
2. Identificar las salidas resultantes del proceso.
3. Identificar los clientes (internos y externos).
4. Identificar entradas necesarias para que el proceso funcione.
5. Identificar los proveedores (internos y externos).

##### RECI

Es una matriz de asignación de responsabilidades.

- Responsable: quien toma las desiciones de la etapa, autoridad máxima sobre la actividad, procura que la actividad se desarrolle correctamente (no necesariamente quien la realiza).
- Ejecutor: encargado de ejecutar la actividad, reporta a un responsable.
- Consultado: tiene información y conocimientos que sirven de entradas para la actividad.
- Informado: es informado de los resultados de la actividad.

Las filas son las actividades, y las columnas los roles.

Primeramente se debiesen ocupar las mismas etapas de SIPOC, luego se pueden subdividir las etapas.

1. Identificar las etapas
2. Identificar las actividades que componen las etapas
3. Asignar códigos RECI
4. Identificar brechas y amigüedades
5. Redistribuir las asignaciones si fuese necesario
*Se debe iterar hasta que el resultado sea satisfactorio.

Reglas:
* Siempre debe haber un único Responsable (R).
* Toda actividad debe tener al menos un Ejecutor (E). (Si una actividad tienen más de un ejecutor se puede plantear dividir la actividad)
* Los demás códigos (C, I) pueden no estar en una actividad.
* Puede existir alguien que sea Ejecutor y Responsable de la misma actividad (E/R).
* Un sistema de información puede ser Ejecutor (E), pero no Responsable (R).

##### BlueworksLive

Plataforma de modelación colaborativa para etapas iniciales. Permite hacer reportes a PowerPoint de forma sencilla.

https://www.ibm.com/products/blueworkslive


