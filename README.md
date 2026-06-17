# Kagastian 5000

Robot caminante inspirado en un pinguino. No usa ruedas; el avance se genera
con patas movidas por un motorreductor y un mecanismo tipo biela/manivela.

El proyecto usa Arduino UNO, un puente H L293D, sensor ultrasonico HC-SR04 y un
buzzer. La comunicacion con la computadora es por Serial USB.

## Estado del prototipo

- Version actual con 1 motorreductor funcional.
- Se probaron 2 motores, pero se regreso a un motor por falla de un motor y del
  L293D.
- No usa Bluetooth.
- No usa LEDs.
- No es un carro con ruedas.

## Carpetas

```text
arduino/
  pinguino_robot_final/
    pinguino_robot_final.ino
    InterfazMotor.h
    InterfazSensorDistancia.h
    InterfazAlerta.h
    MotorL293DControl.h
    SensorUltrasonicoHCSR04.h
    AlertaBuzzer.h
    RobotPinguinoCaminante.h

python_gui/
  pinguino_gui_usb.py

docs/
  CONEXIONES.md
  ESTRUCTURA.md

imgs/
  imagenes del prototipo y componentes

video/
  pruebas del mecanismo
```

## Pines usados

| Componente | Pin Arduino |
|---|---:|
| ENA L293D | 5 |
| IN1 L293D | 2 |
| IN2 L293D | 3 |
| TRIG HC-SR04 | 8 |
| ECHO HC-SR04 | 9 |
| Buzzer | 12 |

## Cargar en Arduino IDE

1. Abrir `arduino/pinguino_robot_final/pinguino_robot_final.ino`.
2. Seleccionar placa Arduino UNO.
3. Seleccionar el puerto COM.
4. Cargar el programa.
5. Abrir Monitor Serial a 9600 baudios.

## Comandos Serial

| Comando | Funcion |
|---|---|
| `A` | Modo automatico |
| `C` | Caminata continua |
| `S` | Detener |
| `D` | Demo |
| `+` | Aumentar distancia minima |
| `-` | Disminuir distancia minima |

## Interfaz Python

La interfaz es opcional y manda comandos por Serial USB.

```bash
pip install -r requirements.txt
python python_gui/pinguino_gui_usb.py
```

## POO y SOLID

El codigo esta separado en clases:

- `MotorL293D`: controla el motor con L293D.
- `UltrasonicSensor`: lee el HC-SR04.
- `BuzzerAlert`: controla el buzzer.
- `PenguinRobot`: coordina modos de movimiento.

Tambien se usan interfaces para motor, sensor y alerta. Asi la logica principal
no depende directamente de un componente especifico.
