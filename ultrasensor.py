#jayden vaughan
#ultrasonic sensor assignment
#controls a neopixel, which fades from red to blue to green based on the distance an ultrasonic sensor produces.
#credit to afton vanhooser for help

import time
import board
import neopixel
import adafruit_hcsr04
import simpleio

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5 
d=0
r=0
b=0
g=0
while True:
    try:
        d = (sonar.distance)
        print(d)  #prints distance
        
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.05)
    if d <= 20:  #maps color values based on distance
        r=(simpleio.map_range(d,5,20,255,0))
        b=(simpleio.map_range(d,5,20,0,255))
        g=0
    elif d <= 35 and d > 20:
        r=0
        b=(simpleio.map_range(d,20,35,255,0))
        g=(simpleio.map_range(d,20,35,0,255))
    dot.fill((r,g,b)) #sets neopixel to r,g,b