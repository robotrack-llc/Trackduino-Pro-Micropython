[![Read the wiki](https://img.shields.io/static/v1?label=Read%20the&message=Wiki&color=orange&style=for-the-badge)](../../wiki)

# Trackduino Pro Micropython API

This **API**'s goal is to provide implementation of Robotrack's Trackduino Pro interface on MicroPython 32-bit platform.

This **API** contains:
- Common Arduino-like functions;
- Pin definitions;
- Timer management class;
- Robotrack's executor drivers;
- Robotrack's sensor drivers.

## Notation list

| Notation | Meaning                       |
| :------: | :---------------------------- |
|    BT    | Bluetooth                     |
|   CdS    | Cadmium sulfide photoresistor |
|    IR    | Infrared                      |
|   LED    | Light-emitting diode          |
|    RC    | Remote control                |

## Robotrack's driver compatibility

| Sensor                                         | Implemented |
| :--------------------------------------------- | :---------: |
| Analog mic                                     |     ✔️      |
| Built-in buttons                               |     ✔️      |
| Button                                         |     ✔️      |
| CdS                                            |     ✔️      |
| Combined color sensor                          |     ✔️      |
| Digital mic                                    |     ✔️      |
| External motor encoder                         |     ✔️      |
| Flame sensor                                   |     ✔️      |
| IR sensor                                      |     ✔️      |
| Magnetic field sensor                          |     ✔️      |
| Temperature sensor                             |     ✔️      |
| Tilt sensor                                    |     ✔️      |
| Ultrasonic distance sensor                     |     ✔️      |
| Vibration sensor                               |     ✔️      |
| Accelerometer / Gyroscope                      |     ✔️      |
| BT RC                                          |     ✔️      |
| IR RC receiver                                 |      ❌      |
| **Neurotrack** connector                       |      ❌      |
| **Young Neurophysiologist-engineer** connector |      ❌      |

| Executor       | Implemented |
| :------------- | :---------: |
| DC motor       |     ✔️      |
| Servo (Big)    |     ✔️      |
| Servo (Small)  |     ✔️      |
| Buzzer         |     ✔️      |
| Built-in LED   |     ✔️      |
| LED            |     ✔️      |
| Display module |     ✔️      |
| **Audiotrack** |     ✔️      |
