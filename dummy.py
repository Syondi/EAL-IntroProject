import RPi.GPIO as io
from car import Car
io.setmode(io.BCM)
import sys, tty, termios, time

io.cleanup()

car = Car()

'''
Wait for the switch button to be pressed.
'''
while True:
    # If button is pressed, get out of loop and listen to key presses
    # input_state = GPIO.input(18)
    if input_state == False:
        print('Button Pressed')

        while True:
            time.sleep(0.2)

    if input_state == True:
        # Turn everything off, break loop, listen to button again.
        car.shutoff(io)
        continue

io.cleanup()