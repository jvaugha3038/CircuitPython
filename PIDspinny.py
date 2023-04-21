import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import time
import rotaryio
import digitalio
import adafruit_mpu6050
import pwmio

# get and i2c object
i2c = board.I2C()
fan = pwmio.PWMOut(board.D10, duty_cycle=0, frequency=440, variable_frequency=True)
# some LCDs are 0x3f... some are 0x27.

mpu = adafruit_mpu6050.MPU6050(i2c)
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)
#screen test
lcd.print("hey")
print("hey")
time.sleep(1)
lcd.clear()
#setting up stuff
encoder = rotaryio.IncrementalEncoder(board.D2, board.D3, divisor=2)
button = digitalio.DigitalInOut(board.D4)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

deg=0
KP=1
KI=0
KD=0
encoder.position=0
menu=1
last_position = 0
Set=45
dt=2
prev=0
ierr=0
op=0

while True:
    def pid(Set,deg,prev,ierr,dt):
        # Parameters in terms of PID coefficients
        op0 = 0
        # upper and lower bounds on heater level
        ophi = 100
        oplo = 0
        # calculate the error
        prev=deg
        error = Set-deg
        # calculate the integral error
        ierr = ierr + KI * error * dt
        # calculate the measurement derivative
        dpv = (deg - prev) / dt
        # calculate the PID output
        P = KP * error
        I = ierr
        D = -KD * dpv
        op = op0 + P + I + D
        # implement anti-reset windup
        if op < oplo or op > ophi:
            I = I - KI * error * dt
            # clip output
            op = max(oplo,min(ophi,op))
        # return the controller output and PID terms
        return [op,P,I,D]
    position = encoder.position
    deg=(round(float(mpu.gyro[0])+0.038, 1)*(dt)*(180/3.14))+prev
    if position == (last_position+1):
        menu+=1
    elif position == (last_position-1):
        menu-=1
    if menu<0:
        menu=4
    elif menu>4:
        menu=1

#checks which page is selected
    if menu == 1:
        lcd.clear()
        lcd.print("kP = "+str(KP))
    if menu == 2:
        lcd.clear()
        lcd.print("kI = "+str(KI))
    if menu == 3:
        lcd.clear()
        lcd.print("kD = "+str(KD))
    if menu == 4:
        lcd.clear()
        lcd.print("kP="+str(KP)+"  kI="+str(KI)+"  kD="+str(KD))
    #increases variable by 1 if button is down
    if not button.value:
        if menu == 1:
            KP += 1
        if menu == 2:
            KI += 1
        if menu == 3:
            KD += 1
        time.sleep(.2)
    last_position = position
    time.sleep(.2)
    print("-------------")
    print(str(op))
    print(str(deg))
    pid(Set,deg,prev,ierr,dt)