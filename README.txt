Kagastian 5000

Robot caminante inspirado en un pinguino. No usa ruedas. Camina mediante un
motorreductor y un mecanismo de patas.

La version actual usa un solo motor.

Para cargar el codigo:
1. Abrir main/main.ino en Arduino IDE.
2. Seleccionar Arduino UNO.
3. Seleccionar el puerto COM.
4. Cargar el programa.
5. Abrir el Monitor Serial a 9600 baudios.

Los archivos .h estan junto a main.ino en la carpeta main.

Comandos:
- A: automatico
- C: caminata continua
- S: detener
- D: prueba corta
- +: frenar mas lejos
- -: frenar mas cerca

Interfaz:
- python_gui/pinguino_gui_usb.py

La interfaz se conecta por Serial USB. No usa Bluetooth.