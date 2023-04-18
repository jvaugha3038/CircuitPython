import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import time
import rotaryio
import digitalio
import adafruit_mpu6050
import pwmio
from simple_pid import PID

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

pid = PID(1, 0, 0, setpoint=45)
pid.sample_time = 0.01
v = controlled_system.update(0)
pid.output_limits = (0, 10)

deg=0
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
    time.sleep(.05)
    prev=deg
    deg=(round(float(mpu.gyro[0])+0.038, 1)*(.05)*(180/3.14))+prev
    if position == (last_position+1):
        menu+=1
    elif position == (last_position-1):
        menu-=1
    if menu<0:
        menu=4
    elif menu>4:
        menu=1
    control = pid(v)
    v = controlled_system.update(control)
    output = pid(current_value)
#checks which light is selected
    if menu == 1:
        lcd.clear()
        lcd.print("kP = "+str(pid.Kp))
    if menu == 2:
        lcd.clear()
        lcd.print("kI = "+str(pid.Ki))
    if menu == 3:
        lcd.clear()
        lcd.print("kD = "+str(pid.Kd))
    if menu == 4:
        lcd.clear()
        lcd.print("kP="+str(pid.Kp)+"| kI="+str(pid.Ki)+"| kD="+str(pid.Kd))
    #activates light if button is down
    if not button.value:
        if menu == 1:
            pid.Kp += 1.0
        if menu == 2:
            pid.Ki += 1.0
        if menu == 3:
            pid.Kd += 1.0
        time.sleep(.2)
    last_position = position
    time.sleep(.2)
    print("-------------")
    print(output)
    