'''
The main class that represent control board with electronic elements for drive an arm
'''

# TODO
from stepper_L293_bipolar import *

def enable_driver_X():
    enable_motor()

def disable_driver_X():
    disable_motor()

def clockwise_X(delay, steps):
    backwards(delay, steps)

def counter_clockwise_X(delay, steps):
    forward(delay, steps)