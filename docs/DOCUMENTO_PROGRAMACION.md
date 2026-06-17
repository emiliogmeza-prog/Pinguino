# Proyecto Segundo Parcial - Programacion Avanzada

## Portada

Institucion: La Salle Bajio  
Materia: Programacion Avanzada  
Proyecto: Robot caminante inspirado en un pinguino  
Nombre del robot: Kagastian 5000  
Docente: Luis Adan Almedia Alcantara  
Fecha de entrega: 17 de junio de 2026

Integrantes:

- 6100090 - Diego De la O Arellano
- 6100093 - Hazel Ramirez Vazquez
- 6100103 - Diego Sebastian Espinoza Perez
- 6100116 - Emilio Giovanni Meza Mendez
- 6100130 - David Alexander Torres Jalomo

## Resumen

El proyecto consiste en un robot caminante inspirado en un pinguino. El objetivo
principal es que el robot se desplace sin ruedas, usando patas movidas por un
motorreductor y un mecanismo tipo biela/manivela.

El sistema utiliza Arduino UNO, puente H L293D, sensor ultrasonico HC-SR04,
buzzer y una interfaz opcional en Python con Tkinter. La comunicacion se realiza
por Serial USB. El robot puede caminar en modo automatico, caminar de forma
continua para pruebas, ejecutar una demostracion y ajustar la distancia a la que
frena con el sensor.

## Introduccion

El proyecto se desarrollo para aplicar programacion orientada a objetos en un
sistema fisico. Se eligio un robot tipo pinguino porque su movimiento permite
representar una locomocion por patas y un balanceo lateral sencillo de observar.

El alcance del sistema incluye control de motor, lectura de distancia,
alerta sonora y comunicacion con una interfaz grafica. No se implemento
Bluetooth ni LEDs en la version actual. Durante el desarrollo se probaron dos
motores, pero se regreso a un diseno de un motor por fallas de un motor y del
puente H L293D.

## Descripcion del sistema

### Hardware

- Arduino UNO.
- Motorreductor funcional.
- Puente H L293D.
- Sensor ultrasonico HC-SR04.
- Buzzer.
- Fuente USB para Arduino.
- Fuente externa para el motor.
- Mecanismo de patas tipo biela/manivela.

### Software

- Arduino IDE para cargar el firmware.
- Arduino C/C++ para el codigo del microcontrolador.
- Python 3 con Tkinter para la interfaz grafica.
- PySerial para comunicacion Serial USB.

## Diagrama general

Los diagramas estan en la carpeta `imgs`:

- `Diagrama de arquitectura.png`
- `Diagrama del circuito.png`
- `Aplicacion.png`

## Arquitectura del programa

El codigo se separo en clases para mantener responsabilidades claras:

- `InterfazMotor.h`: contiene la interfaz `IMotor`.
- `InterfazSensorDistancia.h`: contiene la interfaz `IDistanceSensor`.
- `InterfazAlerta.h`: contiene la interfaz `IAlert`.
- `MotorL293DControl.h`: contiene la clase `MotorL293D`.
- `SensorUltrasonicoHCSR04.h`: contiene la clase `UltrasonicSensor`.
- `AlertaBuzzer.h`: contiene la clase `BuzzerAlert`.
- `RobotPinguinoCaminante.h`: contiene la clase `PenguinRobot`.

Tambien se separo por capas:

- Capa de presentacion: interfaz Python y Monitor Serial.
- Capa de comunicacion: Serial USB a 9600 baudios.
- Capa de logica: clase `PenguinRobot`.
- Capa de hardware: motor, sensor y buzzer.

## Principios SOLID

SRP: Cada clase tiene una responsabilidad. El motor controla movimiento, el
sensor mide distancia, el buzzer genera sonidos y `PenguinRobot` coordina.

OCP: Se pueden agregar nuevos motores, sensores o alertas creando nuevas clases
que respeten las interfaces.

LSP: `PenguinRobot` trabaja con interfaces. Una clase nueva que implemente
`IMotor`, `IDistanceSensor` o `IAlert` puede sustituir a las actuales.

ISP: Las interfaces son pequenas. No existe una interfaz unica enorme para todo
el robot.

DIP: La logica principal depende de abstracciones, no directamente de las clases
concretas del motor, sensor o buzzer.

## Comunicacion computador - microcontrolador

La comunicacion se realiza por Serial USB a 9600 baudios. La computadora envia
caracteres al Arduino:

- `A`: modo automatico.
- `C`: caminata continua.
- `S`: detener.
- `D`: demo.
- `+`: aumentar distancia de frenado del sensor.
- `-`: disminuir distancia de frenado del sensor.

La interfaz Python envia estos comandos al Arduino mediante PySerial.

## Interfaz grafica

La interfaz esta en `python_gui/pinguino_gui_usb.py`.

Elementos:

- Campo de puerto COM.
- Boton Conectar.
- Indicador de estado.
- Boton Automatico: camina y frena con sensor.
- Boton Caminar continuo: prueba de avance.
- Boton Detener robot ahora: apaga el motor y deja el robot en reposo.
- Boton Demo: avanza, retrocede y pita.
- Boton Frenar mas lejos con sensor.
- Boton Frenar mas cerca con sensor.
- Registro de eventos.

## Resultados

El prototipo logro mover el mecanismo de patas y realizar pruebas de avance.
Tambien se comprobo la comunicacion Serial USB entre Python y Arduino. El sensor
ultrasonico permite definir una distancia de frenado: si el robot detecta un
objeto a esa distancia o menos, se detiene, pita y retrocede un poco.

Problemas encontrados:

- Diferencia de velocidad entre motores.
- Falla de un motor.
- Fallas asociadas al L293D.
- Alimentacion insuficiente con pila rectangular de 9 V.

Soluciones:

- Se regreso a un diseno de un motor funcional.
- Se reviso la alimentacion.
- Se separo el codigo en clases.
- Se uso Serial USB en lugar de Bluetooth.

## Conclusiones

El proyecto permitio aplicar programacion orientada a objetos en un sistema real
con sensores y actuadores. La separacion por clases facilito adaptar el codigo
cuando el hardware cambio de dos motores a un motor. Tambien se comprobo que en
robotica el funcionamiento depende tanto del codigo como de la mecanica, la
alimentacion y las conexiones.

## Referencias

[1] Arduino, "Arduino UNO Rev3 Documentation," Arduino Docs.  
[2] STMicroelectronics, "L293D Push-Pull Four Channel Driver Datasheet."  
[3] Python Software Foundation, "tkinter - Python interface to Tcl/Tk."  
[4] PySerial, "Python Serial Port Extension Documentation."  
[5] GitHub, "Repositorio del proyecto Pinguino," https://github.com/emiliogmeza-prog/Pinguino

## Anexos

- Repositorio: https://github.com/emiliogmeza-prog/Pinguino
- Video demostrativo: `video/proyecto.mp4`
- Codigo Arduino: `main.ino`, `include/` y `arduino/pinguino_robot_final/`
- Interfaz Python: `python_gui/pinguino_gui_usb.py`
- Diagramas: `imgs/`
