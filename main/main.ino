#include "MotorL293DControl.h"
#include "SensorUltrasonicoHCSR04.h"
#include "AlertaBuzzer.h"
#include "RobotPinguinoCaminante.h"

// Pines usados por el puente H L293D para controlar el motorreductor.
const byte PIN_ENA = 5;
const byte PIN_IN1 = 2;
const byte PIN_IN2 = 3;

// Pines del sensor ultrasonico HC-SR04.
const byte PIN_TRIG = 8;
const byte PIN_ECHO = 9;

// Salida de la alerta sonora.
const byte PIN_BUZZER = 12;

// Objetos concretos del hardware e inyeccion de dependencias al robot.
MotorL293D motor(PIN_ENA, PIN_IN1, PIN_IN2);
UltrasonicSensor sensor(PIN_TRIG, PIN_ECHO);
BuzzerAlert buzzer(PIN_BUZZER);
PenguinRobot robot(&motor, &sensor, &buzzer);

void setup() {
  // El protocolo con la computadora trabaja a 9600 baudios.
  Serial.begin(9600);
  robot.begin();

  Serial.println("Kagastian 5000 iniciado");
  Serial.println("A automatico, C caminar, S detener, D prueba, + frenar lejos, - frenar cerca");
}

void loop() {
  // Actualiza continuamente comandos, sensor y modo de movimiento.
  robot.update();
}
