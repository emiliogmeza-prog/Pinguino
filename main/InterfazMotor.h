#ifndef INTERFAZMOTOR_H
#define INTERFAZMOTOR_H

// Abstraccion minima para cualquier sistema de movimiento compatible.
class IMotor {
  public:
    virtual ~IMotor() {}

    // Inicializa pines y deja el actuador en un estado seguro.
    virtual void begin() = 0;
    virtual void setSpeed(int speedValue) = 0;
    virtual void forward() = 0;
    virtual void backward() = 0;
    virtual void stop() = 0;
};

#endif
