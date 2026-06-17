#ifndef INTERFAZMOTOR_H
#define INTERFAZMOTOR_H

class IMotor {
  public:
    virtual ~IMotor() {}

    virtual void begin() = 0;
    virtual void setSpeed(int speedValue) = 0;
    virtual void forward() = 0;
    virtual void backward() = 0;
    virtual void stop() = 0;
};

#endif
