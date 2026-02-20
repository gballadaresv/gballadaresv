# Mapas de procesos

Existen distintos niveles de mapas de procesos, mientras mayor el nivel, mayor el detalle y especificidad de los procesos representados.

### Nivel 3+: procesos individuales ámbito implementación
- Cada proceso desde un punto de vista operacional.
- Modelos enriquecidos con información sobre la ejecución (tipos de tareas, información de ejecución, etc.)
- Principales usuarios: quienes implementas SI y ejecutores

### Nivel 2: Procesos individuales ámbito conceptual
- Cada proceso desde una perspectiva de negocio (organización lógica de actividades, puntos de decisión y responsabilidades).
- Principales usuarios: dueños de procesos y gerentes.
- \* Lenguajes: BPMN, EPC o similar.

### Nivel 1: Mapas de procesos
- Conjunto de proceso de la organización y sus relaciones.
- Principales usuarios: arquitectos de procesos y ejecutivos.
\* Lenguajes: cadena de valor (value chain), ArchiMate, o similar.

_\* La cantidad de procesos de una organización promedio no puede ser contada con los dedos._

##### Ciclo de alineamiento empresarial
El principal valor de una Arquitectura de Procesos es ser una herramienta de gestión que apoya la toma de decisiones estratégicas sobre la operación.

- Comprensión: facilita la navegación entre procesos, permite la priorización, ofrece vista estructurada y aumenta la familiarización con los procesos.
- Control: aumenta la transparencia de los procesos, genera bases para sistemas de control, asigna roles y responsabilidades.
- Desempeño: aumenta la estandarización de los procesos (modelo de madurez).

##### Relaciones entre procesos de negocios
- Composición: un proceso (subproceso) es parte de otro proceso (de alto nivel).
- Especialización: un proceso especializado es una variación de otro proceso.
- Gatillo: un proceso (origen) causa el inicio de otro proceso (objetivo).
- Flujo de recursos: un proceso (origen) provee recursos para la ejecución de otro proceso (objetivo).

##### Agrupaciones de procesos
- Primarios: los más centrales para el funcionamiento de una organización (core buisness). Diseño y desarollo, manufactura, marketing y ventas, postventa.
- De soporte: habilitan la ejecución de los procesos primarios. Gestión TI, gestión de personal, contabilidad, gestión financiera, servicios legales.
- De gestión: proveen dirección, reglas, y prácticas para los procesos primarios. Planificacición estratégica, gestión de calidad, gestión de riesgos, presupuesto.

##### Notación ArchiMate
- Proceso: se representa como un rectángulo con bordes redondeados y una flecha blanca en la esquina superior derecha.
- Composición: el subproceso es un proceso que se encuentra dentro de otro proceso de alto nivel (literalmente).
- Especialización: similar a herencia en UML, se representa con un triángulo que apunta al proceso general.
- Gatillo: una flecha sólida que apunta del proceso origen al proceso objetivo.
- Flujo de recursos: una flecha punteada que apunta del proceso origen al proceso
- Grupos: se representan con un rectángulo punteado que engloba a los procesos que pertenecen al grupo.

##### Métodos para generar mapas de procesos
- Estructura de objetivos: usa como base una estructura de objetivos (metas). Desde los objetivos se identifican los procesos necesarios para alcanzarlos.
- Estructura de acciones: usa como base una estructura de acciones (patrones cíclicos). Desde las acciones se identifican los procesos que las ejecutan.
- Modelo de objetos: usa como base un modelo de objetos (entidades). Parte de una base similar a OOP para identificar procesos que manipulan los objetos.
- Modelos de referencia: se basa en que las empresas compran insumos, producen, venden, y despachan. El modelo más usado es PCF (Process Classification Framework), hay distintas versiones separadas por rubro.
- Descomposición de funciones: usa como base la descomposición jerárquica de funciones (capacidades)

1. Clarificar terminología:
   - Definir términos clave.
   - Usar un glosario organizacional o modelos de referencia.
2. Identificar procesos primarios:
   - Los procesos se vinculan con clientes y proveedores.
   - Productos y servicios pueden usarse como puntos de partida.
   - Ayuda pensar en tipos de producto/servicio, canales, tipos de clientes.
3. Para cada proceso identificar sus subprocesos y flujos
   - Identificar salidas intermedias.
   - Ayuda para definir límites: ciclo de vida de productos, relación con clientes, cadena de suministros, etapas de transiciones.
4. Para cada proceso identificar los procesos de soporte y gestión asociados:
   - Qué se necesita para ejecutar los procesos.
   - Los procesos de gestión suelen ser genéricos.
5. Descomponer y especializar procesos: debe hacerse en relación al nivel de detalle requerido para que cada proceso pueda ser gestionado por un único dueño de proceso.
6. Generar especificaciones para cada proceso (ej. matriz de descubrimiento).
7. Revisar consistencia y completitud: se pueden usar modelos de referencia.

