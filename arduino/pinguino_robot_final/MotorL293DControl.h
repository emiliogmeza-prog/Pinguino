#ifndef MOTORL293DCONTROL_H
#define MOTORL293DCONTROL_H

#include <Arduino.h>
#include "InterfazMotor.h"

class MotorL293D : public IMotor {
  private:
    byte enablePin;
    byte in1Pin;
    byte in2Pin;
    int speedMotor;

  public:
    MotorL293D(byte en, byte in1, byte in2) {
      enablePin = en;
      in1Pin = in1;
      in2Pin = in2;
      speedMotor = 180;
    }

    void begin() override {
      pinMode(enablePin, OUTPUT);
      pinMode(in1Pin, OUTPUT);
      pinMode(in2Pin, OUTPUT);
      stop();
    }

    void setSpeed(int speedValue) override {
      speedMotor = constrain(speedValue, 0, 255);
    }

    void forward() override {
      digitalWrite(in1Pin, HIGH);
      digitalWrite(in2Pin, LOW);
      analogWrite(enablePin, speedMotor);
    }

    void backward() override {
      digitalWrite(in1Pin, LOW);
      digitalWrite(in2Pin, HIGH);
      analogWrite(enablePin, speedMotor);
    }

    void stop() override {
      analogWrite(enablePin, 0);
      digitalWrite(in1Pin, LOW);
      digitalWrite(in2Pin, LOW);
    }
};

#endif
