### Resumen
Proxy sirve para controlar acceso. Permite ejecutar algo antes o después de dejar pasar una request.

La clase Subject declara la interfaz que será utilizada tanto por el servicio como por el proxy. Permite que el cliente interactúe tanto con el servicio como con el proxy indistintamente.

La clase Service (o RealSubject) que hereda la estructura de Subject implementa la lógica del código.

La clase Proxy tiene una relación de agregación con la clase Service, una vez termina su ejecución pasa la request al servicio, y puede implementar código posterior a la ejecución de este.

### Observaciones
* Hay varios tipos de proxy, pero el funcionamiento básico de todos es el mismo.