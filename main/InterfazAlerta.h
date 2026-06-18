#ifndef INTERFAZALERTA_H
#define INTERFAZALERTA_H

// Contrato pequeno para las alertas sonoras usadas por el robot.
class IAlert {
  public:
    virtual ~IAlert() {}

    virtual void begin() = 0;
    virtual void startSound() = 0;
    virtual void obstacleAlert() = 0;
    virtual void modeSound() = 0;
};

#endif
