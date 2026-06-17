# Conexiones

## L293D

- ENA al pin 5 de Arduino.
- IN1 al pin 2 de Arduino.
- IN2 al pin 3 de Arduino.
- Pin 16 del L293D a 5V de Arduino.
- Pin 8 del L293D a la fuente externa del motor.
- GND del Arduino, GND del L293D y negativo de la fuente del motor unidos.

## HC-SR04

- TRIG al pin 8 de Arduino.
- ECHO al pin 9 de Arduino.
- VCC a 5V.
- GND a tierra comun.

## Buzzer

- Senal al pin 12 de Arduino.
- GND a tierra comun.

## Alimentacion

El Arduino se alimenta por USB. El motor se alimenta con una fuente externa por
el L293D. Es importante compartir tierra entre Arduino, L293D y la fuente del
motor.
