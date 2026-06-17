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
main.ino
include/
  clases e interfaces del proyecto

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
  DOCUMENTO_PROGRAMACION.md
  MANUAL_USUARIO.md
  MANUAL_TECNICO.md

imgs/
  Diagrama de arquitectura.png
  Diagrama del circuito.png
  Aplicacion.png
  fotos del prototipo y componentes

video/
  proyecto.mp4
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

Tambien se incluye `main.ino` junto con la carpeta `include/` para cumplir con
la estructura pedida en el PDF de la materia.

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

### Botones de la interfaz

| Boton | Comando | Que hace |
|---|---|---|
| Conectar | - | Abre la comunicacion con el puerto COM del Arduino. |
| Automatico: frena con sensor | `A` | El robot camina y usa el sensor ultrasonico. Si detecta un obstaculo cerca, se detiene, pita y retrocede. |
| Caminata continua | `C` | El robot camina de forma continua para probar el mecanismo y medir avance. |
| Detener robot | `S` | Apaga el motor y deja el robot detenido. Sirve para cortar una prueba desde la interfaz. |
| Demo corta | `D` | Hace una prueba corta: avanza, se detiene, retrocede un poco y pita. |
| + Frenar mas lejos | `+` | Aumenta la distancia de frenado del sensor. El robot se detiene desde mas lejos. |
| - Frenar mas cerca | `-` | Disminuye la distancia de frenado del sensor. El robot se acerca mas antes de detenerse. |

La distancia de frenado es la distancia a la que el sensor hace que el robot se
detenga por seguridad. Por ejemplo, si esta en 10 cm, cuando el sensor mida 10
cm o menos el robot frena.

## POO y SOLID

El codigo esta separado en clases:

- `MotorL293DControl.h`: contiene la clase `MotorL293D`, que controla el motor.
- `SensorUltrasonicoHCSR04.h`: contiene la clase `UltrasonicSensor`, que lee el HC-SR04.
- `AlertaBuzzer.h`: contiene la clase `BuzzerAlert`, que controla el buzzer.
- `RobotPinguinoCaminante.h`: contiene la clase `PenguinRobot`, que coordina los modos.

Tambien se usan interfaces para motor, sensor y alerta. Asi la logica principal
no depende directamente de un componente especifico.
