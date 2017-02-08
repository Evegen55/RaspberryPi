# MMA7455 I2C address 1D
# addresses
# 06 at X
# 07 at Y
# 08 at Z
# 16 set working settings  x1000101 is able to measure up to 2g 0x45
# 16 set working settings  x1000001 is able to measure up to 8g 0x41
# 16 set working settings  x1010101 calibration in mode 2g 0x55
# !/usr/bin/python
import smbus
import time
import os


class Accel():
    b = smbus.SMBus(0)

    def Calib(self):
        # set calibration mode
        self.b.write_byte_data(0x1D, 0x16, 0x55)
        # firs calibration
        self.b.write_byte_data(0x1D, 0x10, 0)
        self.b.write_byte_data(0x1D, 0x11, 0)
        self.b.write_byte_data(0x1D, 0x12, 0)
        self.b.write_byte_data(0x1D, 0x13, 0)
        self.b.write_byte_data(0x1D, 0x14, 0)
        self.b.write_byte_data(0x1D, 0x15, 0)

    # Get an acceleration at X
    def getX(self):
        return self.b.read_byte_data(0x1D, 0x06)

    # Get an acceleration at Y
    def getY(self):
        return self.b.read_byte_data(0x1D, 0x07)

    # Get an acceleration at Z
    def getZ(self):
        return self.b.read_byte_data(0x1D, 0x08)


MMA7455 = Accel()
MMA7455.Calib()

for a in range(10000):
    x = MMA7455.getX()
    y = MMA7455.getY()
    z = MMA7455.getZ()

    print "x=", x
    print "y=", y
    print "z=", z

    time.sleep(0.1)
    os.system('clear')

# see also http://www.robot-electronics.co.uk/i2c-tutorial
# https://learn.sparkfun.com/tutorials/i2c
