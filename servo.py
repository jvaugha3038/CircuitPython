#jayden vaughan
#button + servo assignment
#controls a servo with 2 buttons, one button moves the servo one way, and the other button moves it the other way.
#thanks to afton vanhooser for help
import board
from time import sleep
import pwmio
import servo
from digitalio import DigitalInOut, Direction
angle = 90


pwm = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

button = DigitalInOut(board.D7)
button.direction = Direction.INPUT
button2 = DigitalInOut(board.D6)
button2.direction = Direction.INPUT


while True:
    if button.value and angle < 180:
        angle += 1

    if button2.value and angle > 0:
        angle -=1
   
    print(angle)
    my_servo.angle = angle
    sleep(0.01)