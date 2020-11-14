# crypto-therm
Have resistive electric heating at home? Why not heat your home by cryptomining to recouperate some of your electric bill? This is a thermostat that controls your cryptorig.

#### BOM:
- Raspberry Pi (model doesn't matter, must have network connectivity)
  - Note: you could (and really should) use an esp32 or esp8266. I'm using a RPi because I feel guilty about having it sit around, and its a little easier to develop for since it has full Linux + anything that comes with that ecosystem.
- 0-3 LEDs (Optional)
- LCD (Optional)
- 2 Buttons (Optional)
- Breadboard
- Wires (including ones with dupont connectors to connect to RPi pin headers)
- 1k resistor for contrast on LCD
- Resistor Apporporaite for chosen LED to be powered by 3.3v logic

#### Wiring
##### LCD

Diagram: https://www.circuitbasics.com/wp-content/uploads/2015/04/Raspberry-Pi-LCD-4-bit-mode.png


| LCD Pin | Raspberry Pi Pin (pin numbers, not GPIO numbers) |
|-----|-----------------------------------|
| VSS | GND                               |
| VDD | 5v                                |
| V0  | Connect To Ground Via 1k Resistor |
| RS  | 37                                |
| RW  | GND                               |
| E   | 35                                |
| D0  | NC                                |
| D1  | NC                                |
| D2  | NC                                |
| D3  | NC                                |
| D4  | 33                                |
| D5  | 31                                |
| D6  | 29                                |
| D7  | 23                                |
| A   | 5v                                |
| K   | GND                               |


