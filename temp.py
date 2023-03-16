#jayden vaughan
#temp sensor
#temp sensor gets temperature, prints it on LCD screen
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from time import sleep
from analogio import AnalogIn
# get and i2c object
i2c = board.I2C()

# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)
t=AnalogIn(board.A1)

while True:
    lcd.clear()
    #i did guess and check to find 588
    celcius=((int(t.value)-500)/588)
    #converting temp to fahrenheit
    fahr=(((celcius*9)/5)+32)
    lcd.print(""+str(round(celcius,1))+"C | "+str(round(fahr,1))+"F")
    #describes temp
    if fahr > 80:
        lcd.print("     hot")
    elif fahr < 50:
        lcd.print("     cold")
    else:
        lcd.print("     good")
    sleep(1)