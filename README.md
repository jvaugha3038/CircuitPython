
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
HC-SR04|Metro
---|---|
GND|GND
VCC|5V
TRIG|D5
ECHO|D6
# `lcd.py`
Makes an LCD screen print a number, which can be increased and decreased with one button. a second button controls whether the first button increases or decreases the number.


