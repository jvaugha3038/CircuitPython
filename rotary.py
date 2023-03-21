#jayden vaughan
#temp sensor
#temp sensor gets temperature, prints it on LCD screen
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from time import sleep
import rotaryio
from digitalio import DigitalInOut, Direction, Pull
import digitalio
# get and i2c object
i2c = board.I2C()

# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)
#screen test
lcd.print("hey")
sleep(1)
lcd.clear()
#setting up stuff
encoder = rotaryio.IncrementalEncoder(board.D2, board.D3, divisor=2)
button = digitalio.DigitalInOut(board.D4)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
rled = DigitalInOut(board.D8)
rled.direction = Direction.OUTPUT
yled = DigitalInOut(board.D9)
yled.direction = Direction.OUTPUT
gled = DigitalInOut(board.D10)
gled.direction = Direction.OUTPUT
encoder.position=0
light=1
last_position = 1

while True:
    position = encoder.position
    if position == (last_position+1):
        light+=1
    elif position == (last_position-1):
        light-=1
    if light>3 or light<0:
        light=1
#checks which light is selected
    if light == 1:
        lcd.print('''change to
red''')
    if light == 2:
        lcd.print('''change to
yellow''')
    if light == 3:
        lcd.print('''change to
green''')
    #activates light if button is down
    if not button.value:
        if light == 1:
            rled.value=True
            yled.value=False
            gled.value=False
        if light == 2:
            yled.value=True
            rled.value=False
            gled.value=False
        if light == 3:
            gled.value=True
            yled.value=False
            rled.value=False
        sleep(2)
    last_position = position
    sleep(.5)
    lcd.clear()
