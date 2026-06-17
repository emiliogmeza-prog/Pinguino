# Manual tecnico

## Pines

- ENA L293D: pin 5.
- IN1 L293D: pin 2.
- IN2 L293D: pin 3.
- TRIG HC-SR04: pin 8.
- ECHO HC-SR04: pin 9.
- Buzzer: pin 12.

## Alimentacion

- Arduino por USB.
- Motor con fuente externa por el L293D.
- Tierra comun entre Arduino, L293D y fuente del motor.

## Archivos principales

- `main/main.ino`: sketch principal para Arduino IDE.
- `main/*.h`: clases e interfaces visibles como pestanas.
- `python_gui/pinguino_gui_usb.py`: interfaz por Serial USB.

## Comunicacion

La comunicacion usa Serial USB a 9600 baudios. Python envia un caracter y
Arduino cambia el modo del robot.

## Comandos

- `A`: automatico.
- `C`: caminar continuo.
- `S`: detener.
- `D`: prueba corta.
- `+`: frenar mas lejos.
- `-`: frenar mas cerca.
