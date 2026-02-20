# Minería de procesos

Los sistemas de información almacenan información útil para mejorar procesos de negocio. 

Los logs de eventos son un reflejo de la realidad, aportan datos reales de cómo se ejecutan los procesos, a diferencia de los modelos teóricos clásicos. Algunos sistemas que crean logs son SAP, Oracle, Salesforce, Excel, etc.

Los logs de eventos tienen los siguientes componentes:
- Identificador del caso: identifica una instancia del proceso (por ejemplo, número de orden).
- Actividad: nombre de la actividad ejecutada (por ejemplo, "aprobar solicitud").
- Evento: tipo de evento (por ejemplo, inicio o fin de una actividad).
- Timestamp: fecha y hora del evento.
- Ejecutor: persona o sistema que ejecuta la actividad.

\* El registro de evento permite conocer mejor el proceso.

Hay distintas perspectivas:
- Control de flujo: orden de ejecución de las actividades, permiten identificar dinsintos posibles de ejecución.
- Organizacional: recursos y las relaciones que existen entre ellos, permiten identificar roles e interacciones.
- Caso: datos que caracterizan a cada instancia del proceso, permiten analizar similitudes y diferencias entre los casos ejecutados.
- Temporal: cuándo ocurren y con qué frecuencia, permiten identificar cuellos de botella, medir niveles de servicio, monitorear usos de recursos, y predecir tiempo remanente de un caso en ejecución.

### Process mining
Busca extraer conocimiento útil e inesperado de los procesos, mediante el análisis de sus logs de eventos. Permiten descubrir, verificar conformidad y mejorar.

Algunos conceptos clave:
- Evento: acción almacenada en un log, puede referirse al incio, conclusión o cancelación de una actividad para un caso particular del proceso.
- Log de eventos: registro de eventos observador para un cierto proceso.
- Caso: instancia de un proceso.
- Traza: registro de ejecución de una instancia de un proceso como una secuencia finita de eventos ordenados cronológicamente (lista).
- Variante: secuencia específica de actividades de un proceso (set).

\* Un proceso con actividades A, B, C puede tener trazas [ABC, ABC, ABABC], pero las variantes son (ABC, ABABC).


Hay 3 tipos de process mining:
- Descubrimiento (automático) de procesos: ¿cuál es el proceso?
- Verificación de conformidad (conformance checking): ¿estamos haciendo lo que se definió?
- Mejoramiento (enhancement): ¿cómo podemos mejorar?

\* Es escencial tener acceso a los logs de ventos, o tener la posibilidad de crearlos a partir de datos almacenados en los SI. También se debe tener acceso a reuniones con los ejecutores y dueños del proceso para un diagnóstico acabado de las necesidades y oportunidades del negocio, así como el significado y relevancia de los datos.

\* Una herramienta sencilla para process mining es Disco.

\* Para pymes puede ser muy caro usar una herramienta tradicional, en esos casos puede ser mejor usar R o Python.