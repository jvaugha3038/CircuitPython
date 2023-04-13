## Table of Contents
* [Table of Contents](#TableOfContents)
* [blink.py](#blinkpy)
* [servo.py](#servopy)
* [ultrasensor.py](#ultrasensorpy)
* [lcd.py](#lcdpy)
* [temp.py](#temppy)
* [rotary.py](#rotarypy)
* [photo.py](#photopy)
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
## Evidence
![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/112961338/193049719-032fa94f-a18e-4824-8b91-dd4695897ab6.gif)
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
https://user-images.githubusercontent.com/112961338/193276559-804bfd3b-e2af-48be-a515-75a5b8d43e00.mp4
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
## Evidence
https://user-images.githubusercontent.com/112961338/193276790-ac05f340-8184-4312-8d2b-35f6b1026090.mp4
## Reflection
Most of my time spent on this assignment was me trying to figure out a way to make the neopixel fade properly (it produced purple, yellow, and a handful of other colors that shouldn't have happened), and variables quickly solved that problem when I added them. Overall, a tricky assignment.

# `lcd.py`
Makes an LCD screen print a number, which can be increased and decreased with one button. a second button controls whether the first button increases or decreases the number.
## Goal
Use 2 inputs(buttons, switches, etc.) to control a number on an LCD. one button increases the number by 1, the other button switches whether the 1st button increases or decreases the number. Holding either button won't repeat the action.
## Libraries required:
board, time.sleep, digitalio.DigitalInOut, digitalio.Direction, LCD(from lcd.lcd), I2CPCF8574Interface(from lcd.i2c_pcf8574_interface)
## Code
![image](https://user-images.githubusercontent.com/112961338/192549323-0a317b1f-465a-4520-8b76-30a9581cef41.png)
## Wiring
![image](https://user-images.githubusercontent.com/112961338/192551649-81cf4202-75e5-4c22-84b8-5747447f2505.png)
## Evidence
![ezgif com-gif-maker](https://user-images.githubusercontent.com/112961338/193049116-ff705893-cd41-4f89-84db-9e2196635437.gif)
## Reflection
This assignment seemed very complicated at the start, but the wiring was very similar to the servo.py wiring, and we were given a lot of freedom within it (see "count-o-tron 900"). This was definitely the most fun assignment so far.

# `temp.py`
Uses a temperature sensor to accurately display the temperature (in celcius and fahrenheit!) on an LCD screen.
## Goal
Use a temperature sensor to display the temperature on an LCD screen.
## Libraries required:
board, time.sleep, analogio, LCD(from lcd.lcd), I2CPCF8574Interface(from lcd.i2c_pcf8574_interface)
## Code
![image](https://user-images.githubusercontent.com/112961338/225021856-dfdacb5c-6f11-41c4-a8b9-3b5ffb72453e.png)
## Wiring
![20230314_094945](https://user-images.githubusercontent.com/112961338/225025515-fbd786ea-a3b4-419c-a4dd-37893fa5880b.jpg)
## Evidence
https://user-images.githubusercontent.com/112961338/225024414-15ca2db0-48de-450b-b9c4-d0ff106516a7.mp4
## Reflection
Here we enter the age of VSCode being garbage.
This assignment, like the LCD one, was very fun to mess around with. I decided that I could also display fahrenheit along with celcius to spice it up, so I did that. I had to figure out what order to have the lcd.clear and all of the print messages in, so it didnt flood the screen with nonsense or clear things before you could even read them.

# `rotary.py`
Uses a rotary encoder and an LCD to create a menu for selecting an LED.
## Goal
Use a rotary encoder to select and activate a set of LEDs, with an LCD screen to display the menu.
## Libraries required:
board, time.sleep, digtitalio, LCD(from lcd.lcd), I2CPCF8574Interface(from lcd.i2c_pcf8574_interface), rotaryio
## Code
![image](https://user-images.githubusercontent.com/112961338/226637992-fe7325c6-140a-4205-914a-b6587c4c2757.png)
![image](https://user-images.githubusercontent.com/112961338/226638007-4470b8af-35d6-4ef8-9dcb-859ed6a2450a.png)
## Wiring
![20230321_103059](https://user-images.githubusercontent.com/112961338/226639417-6d31bfce-8167-4dba-8fcb-740024777547.jpg)
## Evidence
https://user-images.githubusercontent.com/112961338/226640856-aa997050-44f3-4af0-a779-f53bf481f5f4.mp4
## Reflection
This one was very annoying, mainly due to unrelated VSCode problems. Trying to figure out what to actually do also took a bit of time, but after that it was mostly fine. Also, LCDs just don't like working.

# `photo.py`
Uses a photointerrupter, and displays how many times its been interrupted on an LCD screen.
## Goal
USe a photointerrupter and print how many times it has been interrupted.
## Libraries required:
board, time, digtitalio, LCD(from lcd.lcd), I2CPCF8574Interface(from lcd.i2c_pcf8574_interface), digitalio
## Code
![image](https://user-images.githubusercontent.com/112961338/227223485-ebefa9f1-096e-437c-ad97-e9d821c0d146.png)
## Wiring
![20230323_094048](https://user-images.githubusercontent.com/112961338/227223771-9b9dc38d-43a3-4c7a-bacd-25430a1e3b3e.jpg)
## Evidence
![ezgif com-crop](https://user-images.githubusercontent.com/112961338/227224235-1fbebaed-71a6-4c6a-9a87-8b26ece9bef9.gif)
## Reflection
This may have been the easiest project we've had so far. Ignoring VSCode problems, it took about 15 minutes to finish the code and get it to work. Also, I had to display it on an LCD because VSCode was being terrible, meaning I got to reuse my LCD code for probably the 4th time. This made the project take much less time, though.



