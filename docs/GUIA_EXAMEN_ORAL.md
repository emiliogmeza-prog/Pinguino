# Guía para presentación y examen oral

Esta guía resume los temas que cada integrante debe poder explicar. No sustituye
la revisión directa del código.

## Explicación de 60 segundos

Kagastian 5000 es un robot caminante inspirado en un pingüino. Arduino controla
un motor mediante el L293D, mide obstáculos con el HC-SR04 y utiliza un buzzer
para alertas. La computadora se comunica por Serial USB a 9600 baudios mediante
una interfaz Tkinter. El software está separado en interfaces, implementaciones
de hardware, lógica del robot y presentación.

## Flujo completo de un comando

1. El usuario presiona un botón en Tkinter.
2. `enviar()` manda un carácter por PySerial.
3. Arduino recibe el carácter mediante `Serial.read()`.
4. `PenguinRobot` cambia su modo interno.
5. La lógica llama a la abstracción `IMotor`.
6. `MotorL293D` convierte la orden en señales para ENA, IN1 e IN2.
7. Arduino devuelve mensajes y distancia.
8. `leer_serial()` actualiza la interfaz sin bloquearla.

## Archivos que deben poder explicar

- `main.ino`: crea objetos, configura Serial y llama `robot.update()`.
- `RobotPinguinoCaminante.h`: modos, comandos y decisiones.
- `MotorL293DControl.h`: dirección, PWM y detención del motor.
- `SensorUltrasonicoHCSR04.h`: pulso ultrasónico y cálculo de distancia.
- `AlertaBuzzer.h`: patrones sonoros.
- `InterfazMotor.h`: operaciones mínimas del motor.
- `InterfazSensorDistancia.h`: contrato de medición.
- `InterfazAlerta.h`: contrato de alertas.
- `pinguino_gui_usb.py`: presentación y comunicación desde la computadora.

## Principios SOLID

- **SRP:** cada clase controla una sola parte: motor, sensor, alerta o coordinación.
- **OCP:** puede agregarse otra implementación de motor o sensor sin cambiar la
  lógica principal.
- **LSP:** cualquier implementación válida de las interfaces puede reemplazar a
  la actual.
- **ISP:** se utilizan interfaces pequeñas en vez de una interfaz enorme.
- **DIP:** `PenguinRobot` depende de `IMotor`, `IDistanceSensor` e `IAlert`, no de
  componentes concretos.

## Arquitectura por capas

- Presentación: Tkinter.
- Comunicación: PySerial y Serial de Arduino.
- Lógica: `PenguinRobot`.
- Hardware: motor, sensor, buzzer y sus implementaciones.

## Protocolo que deben memorizar

- `A`: automático.
- `C`: caminata continua.
- `S`: detener.
- `D`: prueba corta.
- `+`: aumentar distancia mínima.
- `-`: disminuir distancia mínima.
- Respuesta de sensor: `Distancia: N cm`.

## Preguntas probables

### ¿Por qué usan interfaces?

Para reducir el acoplamiento. La lógica del robot puede trabajar con otro motor,
sensor o alerta si la nueva clase respeta el contrato.

### ¿Por qué la GUI no se congela?

Porque no utiliza un ciclo infinito para leer Serial. `ventana.after(100,
leer_serial)` programa lecturas cortas dentro del ciclo de eventos de Tkinter.

### ¿Por qué el motor tiene fuente externa?

El motor necesita más corriente de la que debe entregar el Arduino. Las tierras
se conectan en común para que las señales de control tengan la misma referencia.

### ¿Cómo calcula distancia el HC-SR04?

Mide el tiempo que tarda el eco en regresar. Se multiplica por la velocidad del
sonido y se divide entre dos porque la onda recorre ida y vuelta.

### ¿Qué pasa cuando detecta un obstáculo?

El robot se detiene, activa el buzzer, retrocede durante un tiempo corto y vuelve
a detenerse.

### ¿Qué limitaciones tiene?

Utiliza comunicación por cable, un motor funcional y retardos con `delay()`.
Además, la locomoción depende de la alineación y de la resistencia mecánica.

## Reparto recomendado para presentar

Cada integrante debe estudiar todo, aunque pueda iniciar con un tema:

- Integrante 1: objetivo, mecanismo y hardware.
- Integrante 2: interfaz y protocolo serial.
- Integrante 3: clases de hardware e interfaces.
- Integrante 4: `PenguinRobot`, capas y SOLID.
- Integrante 5: pruebas, problemas, resultados y mejoras.

## Lista antes de presentar

- Probar todos los comandos.
- Cerrar el Monitor Serial antes de conectar Tkinter.
- Confirmar el puerto COM.
- Tener una fuente externa estable.
- Preparar el video como respaldo.
- Abrir el código y localizar rápidamente cada clase.
