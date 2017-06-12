import time
import RPi.GPIO as GPIO

# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

# Pin definitons:
GPIO_PIR = 7

# Pin Setup:
GPIO.setup(GPIO_PIR, GPIO.IN)  # Echo

try:
    while True:
        # Read PIR state
        Current_State = GPIO.input(GPIO_PIR)
        print Current_State
except KeyboardInterrupt:
    print " Quit"
    # Reset GPIO settings
    GPIO.cleanup()
