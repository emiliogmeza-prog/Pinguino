#ifndef INTERFAZSENSORDISTANCIA_H
#define INTERFAZSENSORDISTANCIA_H

class IDistanceSensor {
  public:
    virtual ~IDistanceSensor() {}

    virtual void begin() = 0;
    virtual int getDistanceCm() = 0;
};

#endif
