# Manual de usuario

## Cargar codigo

1. Abrir Arduino IDE.
2. Abrir `main/main.ino`.
3. Seleccionar placa Arduino UNO.
4. Seleccionar el puerto COM.
5. Cargar el programa.
6. Abrir Monitor Serial a 9600 baudios si se desea probar por texto.

## Usar interfaz Python

1. Conectar Arduino por USB.
2. Abrir `python_gui/pinguino_gui_usb.py`.
3. Escribir el puerto COM, por ejemplo `COM5`.
4. Presionar `Conectar`.
5. Usar los botones de control.

## Botones

- Automatico: frena con sensor.
- Caminata continua: prueba de avance del mecanismo.
- Detener robot: apaga el motor y deja el robot quieto.
- Prueba corta: avanza, retrocede y pita.
- + Frenar mas lejos: aumenta la distancia a la que frena.
- - Frenar mas cerca: disminuye la distancia a la que frena.

## Nota

Los botones de distancia no cambian la velocidad. Cambian la distancia a la que
el sensor ultrasonico hace que el robot frene.
