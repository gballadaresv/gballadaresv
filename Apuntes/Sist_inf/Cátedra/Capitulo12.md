# Redes y seguridad

### Seguridad informática y de la información

La seguridad informática se ocupa de las vulnerabilidades de software, velando por la continuidad operacional (disponibilidad).

_Una cosa es recuperar el computador que robaron, y otra es recuperar el trabajo que estaba en el computador._

*Un virus no quiere destruir la máquina, quiere tomar control de ella.

*Cuando hay un ataque, no sale una calavera en la pantalla, se detecta mediante análisis de datos anormales.

*Es relevante saber cómo están atacando, no sirve reforzar la puerta si entran por la ventana.

###### Características de un sistema seguro

- Confidencialidad: Sólo la puede ver el que la tiene que ver.
- Integridad: Tiene que estar completo, y cada cosa está en su lugar con sus restricciones correspondientes.
- Disponibilidad: La información y los sistemas deben estar disponibles para los usuarios autorizados cuando la organización lo estime conveniente.

###### ISO 28001/2
Las normas ISO son estándares internacionales que establece qué cosas hay que hacer. En este caso la norma establece cómo trabajar con la información, con controles y respaldos periódicos:

Evaluación de riesgos de la organización: Hay que considerar la probabilidad y el impacto, son relevantes los de alta probabilidad y bajo impacto y las de baja probabilidad y alto impacto, y las de alta probabilidad y alto immpacto son prioridad. *Mitigar los riesgos es caro. El costo de prevenir se justifica con el costo del impacto?

*La mejor forma de cazar un tiranosaurio, es cuando aún está en el huevo.*

*Hay que asegurar la continuidad operativa. Es conveniente tener un proceso B (plan B).

##### RAID
Risk, Assumptions, Issues, Dependencies.

- Assumptions: Lo que se supone con alta probabilidad que será verdadero durante el proyecto. Dejar explícitos y documentados los supuestos y comunicarlo a los clientes/usuarios. NADA es sentido común ni evidente.

- Dependencias: Tareas o eventos que requieren de otras tareas o eventos para comenzar.

- Riesgo: Combina la probabilidad de aparición con el impacto sobre el proyecto (matriz).

##### Ataques comunes

- Malware: Bloquear acceso a archivos (ransomware), spyware y virus.

- Pishing: Enviar información fraudulenta al usuario y que éste entregue información sensible.

- Denial of service (DoS): se spamean peticiones al servidor para que se saturen tratando de responder y lograr una interrupción de servicios.

- SQL-injetion: Se inserta código malicioso entre las comunicaciones de un cliente con un servidor.

- zero day exploit: cuando se detecta una vulnerabilidad y el atacante aprovecha el tiempo en el que aún no se instala el parche y dañar sistemas o robar información.

##### Modelo NIST

1. Identificar: conocer su sistema.
2. Proteger: evaluación de riesgos y estrategia de gestión de riesgo.
3. Detectar: monitoreo de métricas y detección de anomalidades.
4. Responder: ¿qué hacemos? comunicación.
5. Recuperar: planes de recuperación (plan de contingencia).
