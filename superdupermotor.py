



import board
from time import sleep
import pwmio
from analogio import AnalogIn

pot = AnalogIn(board.A0)
motor = pwmio.PWMOut(board.D6, duty_cycle=0, frequency=440, variable_frequency=True)

while True:
    print(pot.value / 65520)
    sleep(.1)
    motor.duty_cycle=(pot.value)

