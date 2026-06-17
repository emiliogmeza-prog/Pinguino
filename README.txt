Kagastian 5000
==============

Robot caminante inspirado en un pinguino. No usa ruedas; camina con patas
movidas por un motorreductor.

Para cargar el codigo:
1. Abrir arduino/pinguino_robot_final/pinguino_robot_final.ino
2. Seleccionar Arduino UNO
3. Seleccionar puerto COM
4. Cargar el programa
5. Abrir Monitor Serial a 9600 baudios

Tambien se incluye main.ino e include/ con la estructura solicitada en el PDF.

Comandos:
A automatico
C caminata continua
S detener
D prueba corta
+ subir distancia minima
- bajar distancia minima

La interfaz Python esta en python_gui/pinguino_gui_usb.py.
Requiere pyserial.
Tambien esta el ejecutable en python_gui/dist/PinguinoRobotUSB.exe.

Botones de la interfaz:
- Conectar: abre la comunicacion con el puerto COM.
- Automatico: frena con sensor si detecta un obstaculo.
- Caminata continua: prueba de avance del mecanismo.
- Detener robot: apaga el motor y deja el robot quieto.
- Prueba corta: avanza, retrocede y pita.
- + Frenar mas lejos: aumenta la distancia a la que frena.
- - Frenar mas cerca: disminuye la distancia a la que frena.
