# Raspberry Pi Projects
## Independent Raspberry Pi Projects

These projects originated from a course offered by 42Electronics.

While much of the setup is identical, I have made significant independent changes adding to their complexity and user experience.

2 sample projects are provided in this Repository:

### ForLoop_4LED: 
- Code featuring a series of for-loops which iterate through output pins and flash an LED sequence
- Code, Video and Schematic (Fritzing) provided

### RFID:
- Code making use of an RFID reader to distiguish approved IDs
- System denies the "tag" and sends a PWM signal to a piezo buzzer for user feedback
- System approves the "card" and illuminates a blue LED for verification
- Code and Video provided

## Level Shifter:
- This project uses and Integrated Circuit(IC) to receive a 5V input and produce a 3.3V output
- This is necessary to not overload the Raspberry Pi circuit
- Infrared LED sensors monitor distance and have line tracking abilities
- The first sensor is a blind proximity sensor. When objects are close it gives an output and the RPi switches the LED to red
- The second sensor is a line tracer. Once it identifies the black line, the LED will remain blue until it diverts
- These types of sensors give sensory feedback to circuits about the real world.
- See the video which is on the "video" branch of this repository.
