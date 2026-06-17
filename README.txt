Kagastian 5000
==============

Robot caminante inspirado en un pinguino. No usa ruedas; avanza con un
mecanismo de patas tipo biela/manivela movido por un motorreductor.

Lenguajes:
- Arduino C/C++ para el robot.
- Python con Tkinter para la interfaz opcional por Serial USB.

Componentes:
- Arduino UNO.
- 1 motorreductor funcional.
- L293D.
- Sensor ultrasonico HC-SR04.
- Buzzer.
- Power bank para Arduino por USB.
- Fuente externa para el motor.

Durante las pruebas se intento usar dos motores, pero se regreso al diseno de
un motor por falla de un motor y problemas con el L293D.

Pines:
- ENA L293D: 5
- IN1 L293D: 2
- IN2 L293D: 3
- TRIG HC-SR04: 8
- ECHO HC-SR04: 9
- Buzzer: 12

Alimentacion:
- Arduino por USB.
- Motor con fuente externa conectada al L293D.
- GND de Arduino, L293D y fuente del motor unidos.

Cargar en Arduino IDE:
1. Abrir `arduino/pinguino_robot_final/pinguino_robot_final.ino`.
2. Seleccionar placa Arduino UNO.
3. Seleccionar el puerto COM.
4. Cargar el programa.
5. Abrir Monitor Serial a 9600 baudios.

Comandos:
- A: modo automatico.
- C: caminata continua.
- S: detener.
- D: demo.
- +: subir distancia minima.
- -: bajar distancia minima.

Interfaz Python:
- Archivo: `python_gui/pinguino_gui_usb.py`
- Requiere `pyserial` si se ejecuta desde Python.

Botones de la interfaz:
- Conectar: abre la comunicacion con el puerto COM.
- Automatico: camina y frena con sensor si detecta un obstaculo.
- Caminar continuo: prueba de avance del mecanismo.
- Detener robot ahora: apaga el motor y deja el robot quieto.
- Demo: avanza, retrocede y pita.
- Frenar mas lejos con sensor: aumenta la distancia a la que frena.
- Frenar mas cerca con sensor: disminuye la distancia a la que frena.

POO:
El programa separa motor, sensor, buzzer y logica principal en clases distintas.
El archivo `.ino` solo crea los objetos y llama al robot.

SOLID:
Se usan interfaces para motor, sensor y alerta. Asi la clase principal no queda
amarrada a un componente especifico y el codigo se puede modificar con menos
cambios.

Mejoras futuras:
- Control Bluetooth.
- LEDs de estado.
- Interfaz con lectura de distancia en tiempo real.
- Mejor fuente para el motor.
- Mejoras mecanicas para caminar mas recto.
