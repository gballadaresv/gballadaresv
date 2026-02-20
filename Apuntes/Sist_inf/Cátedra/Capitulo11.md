### Gestión de datos e inteligencia de negocios

#### Sistemas de manejo de bases de datos

Los Database management systems (DBMS) son software que permiten la centralización de datos en una organización para poder almacenarlos y gestionarlos de forma eficiente y proveer acceso mediante programas de aplicación.

*ETL: Extract, transform, load.

Funcionalidades de una DBMS:
- Definir: especifica tipo, estructura y resticciones para almacenar datos.
- Construir: procesa el almacenamiento de datos.
- Manipular: consutlas para CRUD (Create Read Update Delete)
- Compartir: Permite acceso a múltiples usuarios y programas.

*Las bases de datos no SQL tienen la capcidad de almacenar datos no estructurados y escalar con mayor facilidad. Pueden ser imágenes, películas, etc.

###### Acid vs. Base

Acid: Atomicity, consistent, isolated, durability:

Base: Basically Aviliable, Soft state, Eventual Consistency.

*Base es para datos no SQL, no estructurados.

#### Buisness Intelligence

##### Big data

- Velocidad.
- Variedad (muchas formas, estructurado y no estructurado).
- Volumen.

- Variabilidad (la forma de generación).
- Veracidad.
- Valor.

*Una línea base sirve para hacer comparaciones

Una parte de una  buena gestión de datos es poder indentificar oportunidades de mejora.

Buisness Intelligence (BI) hace referencia al conjunto de estrategias, aplicaciones, arquitecturas y técnicas enfocados a la administración y creación del conocimiento.

Componentes:
- Hadoop.
- Data warehouse (Lugar donde almacenameno las fuentes de información)
- Data mart.
- In-memory computing.
- Analytical platforms.

##### Hadoop
Permite procesar grandes cantidades de datos de manera distribuida y paralela.

Servicios clave:
- MapReduce: separa la información en categorías para trabajarlas.
- Hadoop Distributed File System (HDFS): almacena datos.
- HBase: base de datos no SQL.

##### Data warehouse

Almacena datos históricos y actuales d elos sitemas de operación claves.

Consolida y estandariza información  a lo largo de la empresa, los datos no pueden ser modificados.

Sirve para "guardar una copia del original" por si ocurre algo indeseado durante el manejo de los datos.

Es importante que sea escalable debido a la gran cantidad de datos que llega.

##### Data mart

Es un subconjunto del Data Warehouse, una parte enfocada en los datos específicos según tipo de cliente o zona.

#### Infraestructura Buisness intelligence

Los datos se obtienen de los sistemas de operaciones o ERP, esa data se somete a un proceso ETL para almacenarse a la warehouse, que se descompone en los data marts, y con eso las personas pueden ahcer análisis y reportes.

##### In-memory computing

Se usa la RAM para almacenar datos y reducir retroasos en el sacado de los datos (las BD se almacenan en disco). Puede reducir días o semanas de procesamiento de datos a sólo segundos. Requieren de hardware optimizado. Es conveniente cuando se requiere trabajar con datos a tiempo real.

##### Analytics platform

Plataformas de alta velocidad optimizadas para analizar grandes cantidades de datos.

#### Buisness Analytics

Se busca encontrar nuevas relaciones, patrones y tendencias. Existen varias herramientas para consolidar, analizar y accede a grandes cantidades de datos para tomar mejores decisiones.

##### Multidimensional data analysis (OLAP)

Online Analytical Processing.
Apoya al análisis multidimensional de datos (varias características de una entidad). Permite responder consultas online de manera rápida.

##### Data mining

_Quiero encontrar algo de valor entre tanta roca_.
Permite encontrar patrones y relaciones en la BD. Utiliza técnicas de Machine Learning.
Ej:
- Asociaciones (Ocurrencias vinculadas a sólo un evento).
- Secuencias (Eventos vinculados en el tiempo).
- Clasificaciones (Patrones que describen grupos).
- Predicciones.

##### Text mining

Extrae elementos claves de un conjunto de datos no estructurados. (Emails, Transcripciones de call centers, descripción de patentes y búsquedas, reportes de servicios). Se utilizan técnicas de ML como Natural Language Processing o incluso software de análisis de sentimientos.

##### Web mining

Descubre y analiza patrones útiles de información en la web. Implica entender el comportamiento de los clientes y evaluar la efectividad de una página.

x