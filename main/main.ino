#include "MotorL293DControl.h"
#include "SensorUltrasonicoHCSR04.h"
#include "AlertaBuzzer.h"
#include "RobotPinguinoCaminante.h"

const byte PIN_ENA = 5;
const byte PIN_IN1 = 2;
const byte PIN_IN2 = 3;

const byte PIN_TRIG = 8;
const byte PIN_ECHO = 9;

const byte PIN_BUZZER = 12;

MotorL293D motor(PIN_ENA, PIN_IN1, PIN_IN2);
UltrasonicSensor sensor(PIN_TRIG, PIN_ECHO);
BuzzerAlert buzzer(PIN_BUZZER);
PenguinRobot robot(&motor, &sensor, &buzzer);

void setup() {
  Serial.begin(9600);
  robot.begin();

  Serial.println("Kagastian 5000 iniciado");
  Serial.println("A automatico, C caminar, S detener, D prueba, + frenar lejos, - frenar cerca");
}

void loop() {
  robot.update();
}
