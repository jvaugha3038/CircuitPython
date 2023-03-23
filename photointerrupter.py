import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import time
from digitalio import DigitalInOut, Direction, Pull

# get and i2c object
i2c = board.I2C()

# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)
interrupts = 0
photo = DigitalInOut(board.D4)
photo.direction = Direction.INPUT
photo.pull = Pull.UP
now = time.monotonic()  # Time in seconds since power on

while True:
    if photo.value:
        interrupts+=1
        while photo.value:
            time.sleep(.1)
        pass
    if (now + 4) < time.monotonic():  # If 4 seconds elapses
        lcd.clear()
        lcd.print("interrupted     "+str(interrupts)+" times")
        now = time.monotonic()