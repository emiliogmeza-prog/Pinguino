#ifndef SENSORULTRASONICOHCSR04_H
#define SENSORULTRASONICOHCSR04_H

#include <Arduino.h>
#include "InterfazSensorDistancia.h"

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
      digitalWrite(trigPin, LOW);
      delayMicroseconds(2);

      digitalWrite(trigPin, HIGH);
      delayMicroseconds(10);
      digitalWrite(trigPin, LOW);

      unsigned long duration = pulseIn(echoPin, HIGH, 30000UL);
      if (duration == 0) {
        return 100;
      }

      return (int)(duration * 0.0343 / 2.0);
    }
};

#endif
