#ifndef ALERTABUZZER_H
#define ALERTABUZZER_H

#include <Arduino.h>
#include "InterfazAlerta.h"

// Implementacion de alertas audibles mediante las funciones tone y noTone.
class BuzzerAlert : public IAlert {
  private:
    byte buzzerPin;

  public:
    BuzzerAlert(byte pin) {
      buzzerPin = pin;
    }

    void begin() override {
      pinMode(buzzerPin, OUTPUT);
      noTone(buzzerPin);
    }

    void startSound() override {
      tone(buzzerPin, 1000);
      delay(150);
      noTone(buzzerPin);

      delay(100);

      tone(buzzerPin, 1300);
      delay(150);
      noTone(buzzerPin);
    }

    void obstacleAlert() override {
      tone(buzzerPin, 700);
      delay(200);
      noTone(buzzerPin);
    }

    void modeSound() override {
      tone(buzzerPin, 1200);
      delay(100);
      noTone(buzzerPin);
    }
};

#endif
