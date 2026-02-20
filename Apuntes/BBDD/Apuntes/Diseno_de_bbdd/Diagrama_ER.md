# Relaciones múltiples

Cuando es una relación 1 a n, se representa en el diagrama con una flecha, la dirección en la que apunta la flecha es la del 1, de donde sale la flecha es el n.

*Las situaciones se pueden representar con varios diagramas, cada uno con sus propias ventajas y desventajas.

# Jerarquía de clases

Las subclases se representan pod medio de un triángulo verde invertido, las subclases no pueden tener llaves.

# Entidades débiles

Una entidad débil es una entidad cuya llave depende de otra entidad. Es identificada por sus atributos y la llave de otra endidad. El identificador de una entidad débil se conoce como una llave parcial.
La llave de una entidad débil sería una tupla con la llave parcial propia y todas las llaves de las entidades de las que depende (de más general a más específico).

# Agregación

Se puede encapsular relaciones y entidades en una entidad virtual, agrupando.

# LLaves

Una relación es un conjunto de tuplas, por lo que no hay filas repetidas.

- Super llave: es un conjunto de atributos de R tales que no hayan dos tuplas con los mismos valores. Cualquier conjunto de atributos que determina al resto.
- Llave candidata: una superllave que no se puede achicar. Cualquier conjunto de atributos que determina al resto y ninguno de sus subconjuntos es una super llave.
- Llave primaria: Una llave candidata que queremos destacar y subrayamos en el esquema.
- Llave sustituta: Llave genérica que simplifica las cosas (id).

# Modelo relacional

Para pasar de un diagrama entidad relación a un modelo relacional, hay que crear una relación (tabla) por cada entidad y relación del esquema, para modelar las relaciones se utilizan las llaves foráneas (las llaves de las entidades que relaciona, referenciando a la entidad a la que pertenece).

Las llaves foráneas evitan que se genere una relación con una llave que no existe dentro de su entidad (evita que salgan datos "inventados").

No es necesario representar cada una de las relaciones, hay algunas que puede ser redundante representarlas en tablas.

# Principios básicos del diseño

1. El modelo debe ser fiel al problema.
2. Evitar redundancia.
3. Elegir las entidades y relaciones correctamente.
4. No complicar más de lo necesario.
5. Buena elección de llave primaria.

*Generalmente es conveniente usar una llave sustituta (id).

# Restricciones de integridad

Son restricciones formales que se imponen a un esquema que todas sus instancias se deben satisfacer:
- Valores nulos.
- Unicidad.
- De llave.
- De referencia.
- Dominio.

*Suelen conocerse como IC (Integrity Constrain)