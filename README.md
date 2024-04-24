# Smart Ceramic (Smart Bathroom & Smart Environment)

## Integrantes
- Herrera Ramiro - 1222100418
- Hernández Negrete Alejandro - 1222100417
- Vega Cervantes Salvador - 1222100485

## Carta de liberación del proyecto
- Se presenta y anexa formato de carta, así como la respectiva evidencia mediante una foto
- 
![Liberacion](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Carta%20Liberacion/CartaLiberacion.jpeg) 

Puedes descargar la carta de liberación del proyecto [aquí](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Carta%20Liberacion/Formato%20Hoja%20Membretada.pdf).
Puedes visualizar el video de agradecimiento en el siguiente enlace: [Mira en Drive](https://drive.google.com/drive/folders/1LTE3EKmxZ0Ou9a7oJMnLAZchoGJ-tKnn?usp=sharing)
## Lista del Hardware utilizado
| Id | Componente | Descripción | Imagen | Cantidad | Costo total |
|----|------------|-------------|--------|----------|-------------|
| 1  | ESP32      | Microcontrolador que ayudará a cargar el código, hará funcionar los sensores y controladores | ![ESP32](https://cdn-reichelt.de/bilder/web/xxl_ws/A300/SBC-NODEMCU-ESP32-01.png) | 1 | $140.00 |
| 2  | Raspberry PI | Tiene la capacidad para interactuar con sensores y dispositivos externos, así como para conectarse a redes y enviar datos a la nube | ![RaspBerry Pi 4](https://agelectro904833371.files.wordpress.com/2019/10/board_02.png?w=1024) | 1 | $1,891.00 |
| 3  | DTH11      | Permite medir la temperatura y la humedad relativa del ambiente. | ![DHT11](https://www.mysensors.org/uploads/57c3ec0c4d04abe84cd93e0f/image/dht11.png) | 1 | $52.00 |
| 4  | Buzzer      | Dispositivo que emite sonido para notificaciones auditivas | [![Buzzer](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Imagenes%20de%20los%20componentes/Buzzer.jpg)](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Imagenes%20de%20los%20componentes/Buzzer.jpg) | 1 | $40.00 |
| 5  | Flame      | Sensor de fuego para detectar posibles incendios | [![Flame](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Imagenes%20de%20los%20componentes/Flame%20sensor.jpg)](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Imagenes%20de%20los%20componentes/Flame%20sensor.jpg) | 1 | $30.00 |
| 6  | Photoresistor  | Sensor de luz para detectar la intensidad lumínica del ambiente | [![Photoresistor](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Imagenes%20de%20los%20componentes/Photoresistor.jpg)](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Imagenes%20de%20los%20componentes/Photoresistor.jpg) | 1 | $50.00 |
| 7  | Pir      | Sensor de movimiento para detectar la presencia de personas u objetos en movimiento | [![Pir](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Imagenes%20de%20los%20componentes/PIR.jpg)](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Imagenes%20de%20los%20componentes/PIR.jpg) | 1 | $40.00 |
| 8  | RGB      | Dispositivo que emite luces de colores programables | [![RGB](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Imagenes%20de%20los%20componentes/RGB%20Led.jpg)](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Imagenes%20de%20los%20componentes/RGB%20Led.jpg) | 1 | $17.00 |
| 9  | Led  | Foco que emite luz para iluminación general | [![Led](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Imagenes%20de%20los%20componentes/LED.jpg)](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Imagenes%20de%20los%20componentes/LED.jpg) | 1 | $2.00 |
| 10 | Oled      | Pantalla OLED para mostrar información | [![Oled](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Imagenes%20de%20los%20componentes/Display%20OLED.jpg)](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Imagenes%20de%20los%20componentes/Display%20OLED.jpg) | 2 | $60.00 |
| 11 | Relay      | Módulo de relé para controlar dispositivos eléctricos | [![Relay](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Imagenes%20de%20los%20componentes/Rele.jpg)](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Imagenes%20de%20los%20componentes/Rele.jpg) | 1 | $59.00 |



## Lista de Software utilizado
| Id | Software | Version | Tipo |
|----|----------|---------|------|
|  1  |    Thonny      |    4.1.2     |   IDE para manejo con Micropython   |
| 2   |      Node red    |    3.1.5     |   Software libre que permite crear Dashboard   |
| 3   |   Postgres   |     16.1        |   Software libre que permite la gestión de base de datos   |


## Visión del producto
"Smart Ceramic" es una innovadora solución diseñada para transformar el entorno del baño y mejorar la experiencia del usuario a través de tecnologías inteligentes integradas en cerámicas de última generación. Con un enfoque en la funcionalidad, el diseño y la sostenibilidad, nuestro producto busca ofrecer un espacio de baño más seguro, eficiente y confortable para los usuarios. Esto se planea implementar gracias a la ayuda de un sensor PIR, sensor de humedad y temperatura DHT11, Sensor de Flama, Buzzer y Relés para el control de la energía, además de manejar el envio de un mensaje mediante la API de WhatsApp para Node-Red.

El concepto de "Smart Ceramic" abarca dos aspectos principales: Smart Bathroom y Smart Environment.

- Smart Bathroom:

El Smart Bathroom incorpora una serie de características y dispositivos inteligentes que optimizan las actividades diarias en el baño. Desde sistemas de iluminación LED regulables hasta la incorporación de una pantalla OLED y sistema de energpia mediante luz, para visualizar el estado del baño, nuestro objetivo es crear un ambiente de baño personalizado y de alta tecnología que se adapte a las necesidades y preferencias de cada usuario.

Además, el Smart Bathroom incluye elementos de seguridad avanzados, como sensores de movimiento para ofrecer una experiencia de usuario intuitiva y accesible.

- Smart Environment

El Smart Environment se enfoca en la mejora del entorno general de la cerámica mediante tecnologías innovadoras que promueven la eficiencia energética y la sostenibilidad. Esto incluye controladores de temperatura ambiente y humedad, así como dispositivos de monitoreo de luz y fuego.

Nuestro objetivo es crear un entorno al bienestar de los usuarios y al cuidado de los materiales y producción. Al integrar tecnologías inteligentes en los materiales cerámicos, "Smart Ceramic" no solo mejora la funcionalidad del baño, sino que también promueve un estilo de vida más consciente y responsable.

En resumen, "Smart Ceramic" representa una nueva era en el diseño y la tecnología de baños, ofreciendo soluciones innovadoras que transforman el espacio de baño en un ambiente inteligente, seguro y sostenible, además de monitorear los estados de los componentes mediante un dispositivo celular o dashboard de Node-red.

## Conexiones
- Imagenes de Wokwi, Fritzing, o de otro software que permiten mostrar las conexiones del circuito.
- ESP 32

- Modelado de SmartBathroom

![SmartBathroom](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Fritzing/ModeladoBa%C3%B1o.jpeg)

- Modelado de SmartEnvironment

![SmartEnvironment](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Fritzing/ModeladoAmbiente.jpeg)

- Modelado de SmartLight

![SmartLight](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Fritzing/ModeladoControLuz.jpeg)


## Funcionalidades

| Id | Historia de usuario | Prioridad | Estimación | Como probarlo | Responsable |
|----|---------------------|-----------|------------|---------------|-------------|
| 1  | Es molesto encender el baño con las manos llenas de mezcla de la cerámica, se daña | Alta      | 5 días     | Intentar encender el baño con las manos ocupadas | Ramiro Herrera |
| 2  | Es necesario tener una manera de saber qué temperatura o humedad hay para chequear las cerámicas. | Media     | 3 días     | Verificar la visualización de la temperatura y humedad en la pantalla del dispositivo | Alejandro Hernández Negrete |
| 3  | Sería interesante que el baño encienda automáticamente un foco al detectar la presencia de una persona. | Alta      | 7 días     | Ingresar al baño y verificar si el foco se enciende automáticamente al detectar movimiento | Salvador Vega Cervantes |
| 4  | Se debe poder controlar las luces del baño de manera remota a través de una aplicación móvil. | Alta      | 6 días     | Utilizar la aplicación móvil para encender y apagar las luces del baño desde una ubicación remota | Ramiro Herrera |
| 5  | Sería beneficioso visualizar los datos de temperatura y humedad en gráficas o representaciones visuales en una interfaz de usuario. | Alta      | 8 días     | Observar gráficas o representaciones visuales en la interfaz de usuario creada en Node-RED que muestren los procesos y valores de temperatura y humedad en tiempo real | Alejandro Hernández Negrete |

## Prototipo 
- Coloca la imagen de tu proyecto al iniciar el desarrollo
![Antes](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Evidencias%20Fotograficas/Antes.jpeg)
![Antes](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Evidencias%20Fotograficas/ZonaLuz.jpeg)

# Evidencias de funcionamiento
- Captura de pantalla de flujos de Node RED
![SmartBathroom](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Flujos%20NodeRed/SmartBathroom.png)
![SmartEnvironment](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Flujos%20NodeRed/SmartEnvironment.png)
![SmartLight](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Flujos%20NodeRed/LightControl.png)
![APIWHATS](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Flujos%20NodeRed/APIWhatsApp.png)

## Captura de las pantallas del proyecto DASHBOARD y Pantalla de la ESP32

![1](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Flujos%20NodeRed/DashBoard1.png)
![2](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Flujos%20NodeRed/DashBoard2.png)
![3](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Flujos%20NodeRed/LightControl.png)
![4](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Flujos%20NodeRed/DashBoard3.png)
![5](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Flujos%20NodeRed/DashboardTelefono1.jpg)
![6](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Flujos%20NodeRed/DashboardTelefono2.jpg)

## Video demostrativo de las funcionalidades del proyecto

Enlace a los videos respecto a las funcionalidades del proyecto

[Mira en Drive](https://drive.google.com/drive/folders/1LTE3EKmxZ0Ou9a7oJMnLAZchoGJ-tKnn?usp=sharing)


## Código fuente

Descarga los archivos utilizados 
[SMART BATHROOM](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/CodigosPY/SmartBathroom.py).
[SMART ENVIRONMENT](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/CodigosPY/SmartEnvironment.py).
[LIGHT CONTROL](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/CodigosPY/SmartLight.py).
[LIBRERÍA PARA OLED](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/CodigosPY/LibreriaOLED.py).

## Creación de base de datos POSTGRES

CREATE DATABASE ceramica;

Tabla sensor_type

CREATE TABLE sensor_type (id SERIAL PRIMARY KEY, name VARCHAR(100) NOT NULL, record_at TIMESTAMP DEFAULT now());

Tabla users

CREATE TABLE users(id SERIAL PRIMARY KEY, username VARCHAR(40), password VARCHAR(40), record_at TIMESTAMP DEFAULT now());

Tabla sensor

CREATE TABLE sensor(id SERIAL PRIMARY KEY, type INTEGER, name VARCHAR(50), record_at TIMESTAMP DEFAULT now(), FOREIGN KEY(type) REFERENCES sensor_type(id));

Tabla sensor_details

CREATE TABLE sensor_details(id SERIAL PRIMARY KEY, sensor_id INTEGER, user_id INTEGER, value FLOAT, record_at TIMESTAMP DEFAULT now(), FOREIGN KEY(sensor_id) REFERENCES sensor(id), FOREIGN KEY(user_id) REFERENCES users(id));

## Finalización del proyecto

Se anexan las imagenes pertinentes al resultado del proyecto, revisar la sección de evidencia para descargarlo.
| SMART BATHROOM 1  | SMART BATHROOM 2|
|----------------|--|
|![1](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Evidencias%20Fotograficas/Ba%C3%B1o1.jpeg)|![2](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Evidencias%20Fotograficas/Ba%C3%B1o2.jpeg)|

| SMART ENVIRONMENT 1  | SMART ENVIRONMENT 2|
|----------------|--|
|![1](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Evidencias%20Fotograficas/Ambiente1.jpeg)|![2](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Evidencias%20Fotograficas/Ambiente2.jpeg).|

| SMART LIGHT 1  | SMART LIGHT 2|
|----------------|--|
|![1](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Evidencias%20Fotograficas/Luz1.jpeg)|![2](https://github.com/RamiroHerreraX/projectJardinIntelgente/blob/main/Evidencias%20Fotograficas/Luz2.jpeg)|
