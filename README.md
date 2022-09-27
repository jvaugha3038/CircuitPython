## Table of Contents
* [Table of Contents](#TableOfContents)
* [blink.py](#blink.py)
* [servo.py](#servo.py)
* [ultrasensor.py](#ultrasensor.py)
* [lcd.py](#lcd.py)
---
# `blink.py`
Controls a neopixel and makes it blink red, green, and blue. 
## Goal
The assignment was to make the neopixel on the Metro M4 change colors from red, to green, to blue.
## libraries required:
board, neopixel, time.sleep

All libraries required (except time.sleep) can be found in the bundle: https://circuitpython.org/libraries
## Code
![image](https://user-images.githubusercontent.com/112961338/191976543-13d5759d-2f82-4997-a063-4db2cf937ab6.png)
## Reflection
This was a fairly simple assignment overall. It was basically a test to make sure VS Code and the Metro M4's actually worked.
# `servo.py` 
Controls a servo with 2 buttons, one button moves the servo one way, and the other button moves it the other way. 
## Goal
To get a micro servo to sweep back and forth with 2 buttons.
## libraries required:
board, time.sleep, pwmio, servo, digitalio.DigitalInOut, digitalio.Direction
## Code
![image](https://user-images.githubusercontent.com/112961338/192539077-f8848581-a07c-4dea-b97a-23b43bb37a45.png)
## Wiring
![image](https://user-images.githubusercontent.com/112961338/192543191-aa17c350-e8f0-4e44-871f-a25ccecde198.png)
## Evidence

## Reflection
This project took a bit longer than it should've, and it turns out the problems were that the signal wire was on the wrong side of the button, and that one of my buttons just didn't work. Past those problems, the assignment was pretty simple.
# `ultrasensor.py` 
Controls a neopixel, which fades from red to blue to green based on the distance an ultrasonic sensor produces. 
## Goal
Smoothly shift the color of the Metro M4's neopixel based on the distance given by an ultrasonic sensor, according to this graphic:
![image](https://user-images.githubusercontent.com/112961338/192543808-eb23399e-13dd-4b47-9c55-851d5c1238ce.png)
## libraries required:
time.sleep, board, neopixel, adafruit_hcsr04, simpleio
## Code
![image](https://user-images.githubusercontent.com/112961338/192544025-d3b3d278-7e73-4da5-b064-deef88f071b4.png)
## Wiring
(the tinkercad ultrasonic sensor only has 3 pins so I did a table instead)
HC-SR04|Metro
---|---|
GND|GND
VCC|5V
TRIG|D5
ECHO|D6
## Reflection
Most of my time spent on this assignment was me trying to figure out a way to make the neopixel fade properly (it produced purple, yellow, and a handful of other colors that shouldn't have happened), and variables quickly solved that problem when I added them. Overall, a tricky assignment.
# `lcd.py`
Makes an LCD screen print a number, which can be increased and decreased with one button. a second button controls whether the first button increases or decreases the number.
## Goal
Use 2 inputs(buttons, switches, etc.) to control a number on an LCD. one button increases the number by 1, the other button switches whether the 1st button increases or decreases the number. Holding either button won't repeat the action.
## libraries required:
board, time.sleep, digitalio.DigitalInOut, digitalio.Direction, LCD(from lcd.lcd), I2CPCF8574Interface(from lcd.i2c_pcf8574_interface)
## Code
![image](https://user-images.githubusercontent.com/112961338/192549323-0a317b1f-465a-4520-8b76-30a9581cef41.png)
## Wiring
![image](https://user-images.githubusercontent.com/112961338/192551649-81cf4202-75e5-4c22-84b8-5747447f2505.png)
## Reflection
This assignment seemed very complicated at the start, but the wiring was very similar to the servo.py wiring, and we were given a lot of freedom within it (see "count-o-tron 900"). This was definitely the most fun assignment so far.
