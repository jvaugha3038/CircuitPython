#jayden vaughan
#LCD counting assignment
#lcd.py makes an LCD screen print a number, which can be increased and decreased with one button.
#a second button controls whether the first button increases or decreases the number.
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from time import sleep
from digitalio import DigitalInOut, Direction

# get and i2c object
i2c = board.I2C()

# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

button = DigitalInOut(board.D7)
button.direction = Direction.INPUT
button2 = DigitalInOut(board.D6)
button2.direction = Direction.INPUT
countBy=1
count=0

while True:
    if button.value:
        count+=countBy
        print(str(count))
        lcd.clear()
        lcd.print("count-o-tron 900")
        lcd.print(str(count))
        while button.value:
            sleep(.1)
    if button2.value:
        countBy = countBy*-1
        print("flip flop")
        while button2.value:
            sleep(.1)