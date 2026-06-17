#ifndef ROBOTPINGUINOCAMINANTE_H
#define ROBOTPINGUINOCAMINANTE_H

#include <Arduino.h>
#include "InterfazMotor.h"
#include "InterfazSensorDistancia.h"
#include "InterfazAlerta.h"

class PenguinRobot {
  private:
    enum RobotMode {
      STOPPED,
      AUTOMATIC,
      CONTINUOUS_WALK,
      DEMO
    };

    IMotor* motor;
    IDistanceSensor* sensor;
    IAlert* alert;

    RobotMode mode;
    int minDistanceCm;
    int walkSpeed;
    unsigned long lastDistancePrintMs;

    static const int DEFAULT_MIN_DISTANCE_CM = 10;
    static const int MIN_ALLOWED_DISTANCE_CM = 5;
    static const int MAX_ALLOWED_DISTANCE_CM = 50;
    static const int DEFAULT_WALK_SPEED = 180;
    static const int BACKWARD_SPEED = 170;

  public:
    PenguinRobot(IMotor* motorRef, IDistanceSensor* sensorRef, IAlert* alertRef) {
      motor = motorRef;
      sensor = sensorRef;
      alert = alertRef;

      mode = AUTOMATIC;
      minDistanceCm = DEFAULT_MIN_DISTANCE_CM;
      walkSpeed = DEFAULT_WALK_SPEED;
      lastDistancePrintMs = 0;
    }

    void begin() {
      motor->begin();
      sensor->begin();
      alert->begin();

      motor->setSpeed(walkSpeed);
      motor->stop();
      alert->startSound();
    }

    void update() {
      readSerialCommand();

      switch (mode) {
        case STOPPED:
          stopRobot();
          break;
        case AUTOMATIC:
          automaticMode();
          break;
        case CONTINUOUS_WALK:
          continuousWalk();
          break;
        case DEMO:
          demoMode();
          break;
      }
    }

  private:
    void automaticMode() {
      int distance = sensor->getDistanceCm();
      printDistance(distance);

      if (distance <= minDistanceCm) {
        avoidObstacle();
      } else {
        walk();
      }
    }

    void walk() {
      motor->setSpeed(walkSpeed);
      motor->forward();
    }

    void continuousWalk() {
      walk();
    }

    void stopRobot() {
      motor->stop();
    }

    void avoidObstacle() {
      Serial.println("Obstaculo detectado: detener, alertar y retroceder.");

      motor->stop();
      alert->obstacleAlert();
      delay(300);

      motor->setSpeed(BACKWARD_SPEED);
      motor->backward();
      delay(500);

      motor->stop();
      delay(300);
    }

    void demoMode() {
      Serial.println("Modo demo: avance, pausa, retroceso y alerta.");

      motor->setSpeed(150);
      motor->forward();
      delay(1000);

      motor->stop();
      delay(300);

      motor->setSpeed(150);
      motor->backward();
      delay(600);

      motor->stop();
      alert->modeSound();

      mode = STOPPED;
      Serial.println("Demo terminado. Modo: detenido");
    }

    void readSerialCommand() {
      while (Serial.available() > 0) {
        char command = Serial.read();

        if (command == '\n' || command == '\r' || command == ' ') {
          continue;
        }

        if (command == 'S' || command == 's') {
          mode = STOPPED;
          motor->stop();
          Serial.println("Modo: detenido");
          alert->modeSound();
        } else if (command == 'A' || command == 'a') {
          mode = AUTOMATIC;
          Serial.println("Modo: automatico");
          alert->modeSound();
        } else if (command == 'C' || command == 'c') {
          mode = CONTINUOUS_WALK;
          Serial.println("Modo: caminata continua");
          alert->modeSound();
        } else if (command == 'D' || command == 'd') {
          mode = DEMO;
          Serial.println("Modo: demo");
          alert->modeSound();
        } else if (command == '+') {
          changeMinimumDistance(1);
        } else if (command == '-') {
          changeMinimumDistance(-1);
        } else {
          Serial.print("Comando no reconocido: ");
          Serial.println(command);
        }
      }
    }

    void changeMinimumDistance(int delta) {
      minDistanceCm = constrain(
        minDistanceCm + delta,
        MIN_ALLOWED_DISTANCE_CM,
        MAX_ALLOWED_DISTANCE_CM
      );

      Serial.print("Distancia minima de deteccion: ");
      Serial.print(minDistanceCm);
      Serial.println(" cm");
    }

    void printDistance(int distance) {
      unsigned long now = millis();
      if (now - lastDistancePrintMs < 500) {
        return;
      }

      lastDistancePrintMs = now;
      Serial.print("Distancia: ");
      Serial.print(distance);
      Serial.println(" cm");
    }
};

#endif
