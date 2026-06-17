Kagastian 5000

Robot caminante inspirado en un pinguino. No usa ruedas. El movimiento se
genera con un motorreductor y un mecanismo de patas tipo biela y manivela.

Componentes:
- Arduino UNO
- Un motorreductor
- Puente H L293D
- Sensor ultrasonico HC-SR04
- Buzzer
- Power bank para Arduino
- Fuente externa para el motor

Estado del proyecto:
- La version actual usa un solo motor.
- Se probaron dos motores, pero se regreso a uno por la falla de un motor y del L293D.
- No usa Bluetooth.
- No usa LEDs.

Pines:
- ENA del L293D: 5
- IN1 del L293D: 2
- IN2 del L293D: 3
- TRIG del HC-SR04: 8
- ECHO del HC-SR04: 9
- Buzzer: 12

Codigo Arduino:
- Abrir main/main.ino en Arduino IDE.
- Seleccionar Arduino UNO.
- Seleccionar el puerto COM.
- Cargar el programa.
- Usar el Monitor Serial a 9600 baudios.

Los archivos .h estan en la carpeta main junto a main.ino para que Arduino IDE
los muestre como pestanas.

Comandos:
- A: modo automatico
- C: caminata continua
- S: detener
- D: prueba corta
- +: frenar a mayor distancia
- -: frenar a menor distancia

Interfaz:
- Archivo Python: python_gui/pinguino_gui_usb.py
- La comunicacion se realiza por Serial USB.

Botones:
- Conectar: abre la comunicacion con el puerto COM.
- Automatico: camina y frena cuando el sensor detecta un obstaculo.
- Caminata continua: mantiene el motor funcionando para probar el avance.
- Detener robot: detiene el motor.
- Prueba corta: avanza, se detiene, retrocede y activa el buzzer.
- Frenar mas lejos: aumenta la distancia de deteccion.
- Frenar mas cerca: disminuye la distancia de deteccion.

Programacion orientada a objetos:
- MotorL293D controla el motor.
- UltrasonicSensor mide la distancia.
- BuzzerAlert controla el buzzer.
- PenguinRobot coordina el funcionamiento.

El proyecto utiliza interfaces para separar el motor, el sensor y la alerta.