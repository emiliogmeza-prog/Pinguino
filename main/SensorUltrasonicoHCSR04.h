#ifndef SENSORULTRASONICOHCSR04_H
#define SENSORULTRASONICOHCSR04_H

#include <Arduino.h>
#include "InterfazSensorDistancia.h"

// Adaptador del sensor HC-SR04 a la interfaz IDistanceSensor.
class UltrasonicSensor : public IDistanceSensor {
  private:
    byte trigPin;
    byte echoPin;

  public:
    UltrasonicSensor(byte trig, byte echo) {
      trigPin = trig;
      echoPin = echo;
    }

    void begin() override {
      pinMode(trigPin, OUTPUT);
      pinMode(echoPin, INPUT);
      digitalWrite(trigPin, LOW);
    }

    int getDistanceCm() override {
      // Pulso de 10 microsegundos requerido para iniciar la medicion.
      digitalWrite(trigPin, LOW);
      delayMicroseconds(2);

      digitalWrite(trigPin, HIGH);
      delayMicroseconds(10);
      digitalWrite(trigPin, LOW);

      unsigned long duration = pulseIn(echoPin, HIGH, 30000UL);
      if (duration == 0) {
        // Si no existe eco dentro del tiempo limite, se considera despejado.
        return 100;
      }

      // La onda recorre ida y vuelta; por eso la distancia se divide entre dos.
      return (int)(duration * 0.0343 / 2.0);
    }
};

#endif
