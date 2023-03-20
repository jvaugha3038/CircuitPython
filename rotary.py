#jayden vaughan
#temp sensor
#temp sensor gets temperature, prints it on LCD screen
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from time import sleep
import rotaryio
# get and i2c object
i2c = board.I2C()

# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

encoder = rotaryio.IncrementalEncoder(board.D3, board.D4)
last_position = None
while True:
    position = encoder.position
    if last_position is None or position != last_position:
        lcd.print(str(position))
        sleep(.5)
        lcd.clear()
    last_position = position