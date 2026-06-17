# Estructura del codigo

El programa se dejo en una sola carpeta llamada `main`. Dentro estan
`main.ino` y los archivos `.h` para que Arduino IDE los muestre como pestanas.

## Archivos

- `main.ino`: crea los objetos y llama a `robot.update()`.
- `InterfazMotor.h`: interfaz para motores.
- `InterfazSensorDistancia.h`: interfaz para sensores de distancia.
- `InterfazAlerta.h`: interfaz para alertas.
- `MotorL293DControl.h`: control del motor con L293D.
- `SensorUltrasonicoHCSR04.h`: medicion de distancia con HC-SR04.
- `AlertaBuzzer.h`: sonidos del buzzer.
- `RobotPinguinoCaminante.h`: logica de modos del robot.

## Modos

- Automatico: camina y revisa el sensor.
- Caminata continua: prueba de avance.
- Detenido: apaga el motor.
- Prueba: avance, pausa, retroceso y sonido.

## Nota de hardware

Se intento usar dos motores, pero la version preparada para entrega usa un solo
motorreductor funcional. Esto se hizo por fallas en un motor y en el L293D.

La carpeta que se usa para cargar el robot es `main/`.
