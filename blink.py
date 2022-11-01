#jayden vaughan
#neopixel blinking assignment
#controls a neopixel and makes it blink red, green, and blue.

import board #importing libraries
import neopixel
from time import sleep

dot = neopixel.NeoPixel(board.NEOPIXEL, 1) #sets the neopixel to a variable "dot"
dot.brightness = 0.5 #sets brightness. don't change this

print("Make it red!")

while True:
    dot.fill((255, 0, 0)) #makes neopixel red
    sleep(1)
    dot.fill((0,255,0)) #then green
    sleep(1)
    dot.fill((0,0,255)) #then blue
    sleep(1)