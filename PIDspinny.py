import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from time import sleep
import rotaryio
from digitalio import DigitalInOut, Direction, Pull
import digitalio
import adafruit_mpu6050
# get and i2c object
i2c = board.I2C()

# some LCDs are 0x3f... some are 0x27.

mpu = adafruit_mpu6050.MPU6050(i2c)
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)
#screen test
lcd.print("hey")
print("hey")
sleep(1)
lcd.clear()
#setting up stuff
encoder = rotaryio.IncrementalEncoder(board.D2, board.D3, divisor=2)
button = digitalio.DigitalInOut(board.D4)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

deg=0
ack=1
kP=1
kI=0
kD=0
encoder.position=0
menu=1
last_position = 0
Setpoint=45
dt=5
prev=0


while True:
    position = encoder.position
    sleep(.05)
    prev=deg
    deg=(round(float(mpu.gyro[0])+0.038, 1)*(.05)*(180/3.14))+prev

    

    if ack==2:
        if position == (last_position+1):
            menu+=1
        elif position == (last_position-1):
            menu-=1
        if menu<0:
            menu=4
        elif menu>4:
            menu=1
        Previous_error=Error
        Error = Setpoint - deg
        Integral = Integral + (Error*dt)
        Derivative = (Error - Previous_error)/dt
        Drive = (Error*kP) + (Integral*kI) + Derivative*kD
    #checks which light is selected
        if menu == 1:
            lcd.print("kP = "+str(kP))
        if menu == 2:
            lcd.print("kI = "+str(kI))
        if menu == 3:
            lcd.print("kD = "+str(kD))
        if menu == 4:
            lcd.print("kP="+str(kP)+"|kI="+str(kI)+"|kD="+str(kD))
        #activates light if button is down
        if not button.value:
            if menu == 1:
                kP+=1
            if menu == 2:
                kI+=1
            if menu == 3:
                kD+=1
            sleep(.2)
        last_position = position
        sleep(.2)
        lcd.clear()


