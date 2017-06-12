#!/usr/bin/python
# This is simple example how to use PIR sensor HC-SR501. This may be helpful to use
# any type of threshold sensors.
# Import required Python libraries
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Pin definitons:
GPIO_PIR = 7
GPIO_LED = 8

# Pin Setup:
GPIO.setup(GPIO_PIR, GPIO.IN)  # Echo
GPIO.setup(GPIO_LED, GPIO.OUT)
GPIO.output(8, False)

# helper vars
Current_State = 0
Previous_State = 0

try:
    # Loop until PIR output is 0
    while GPIO.input(GPIO_PIR) == 1:
        Current_State = 0
    # Loop until users quits with CTRL-C
    while True:
        # Read PIR state
        Current_State = GPIO.input(GPIO_PIR)
        if Current_State == 1 and Previous_State == 0:
            # PIR is triggered
            print " Motion detected!"
            status = " Motion detected!"
            GPIO.output(8, True)
            time.sleep(5)
            GPIO.output(8, False)
            # Record previous state
            Previous_State = 1
        elif Current_State == 0 and Previous_State == 1:  # REED has returned to ready state
            print " Ready"
            Previous_State = 0
        # Wait for 10 milliseconds
        time.sleep(0.01)
except KeyboardInterrupt:
    print " Quit"
    # Reset GPIO settings
    GPIO.cleanup()
