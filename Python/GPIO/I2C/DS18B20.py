# http://raspberrypi.tomasgreno.cz/thermal-sensor-i2c.html
#!/usr/bin/env python2.7

from sys import stdout
from sys import exit
from time import sleep

while True:

        try:

                temp = open("/mnt/1wire/28.C2D5C4040000/temperature", "r")
                t_raw = temp.read()
                temp.close()

                t = float(t_raw)

                print(('\r%.2f\xb0C   ') % t),
                stdout.flush()

                for x in range(10):
                        print('\b#'),
                        stdout.flush()
                        sleep(0.1)

                print('\r'),
                for x in range(15):
                        print(" "),
                stdout.flush()

        except KeyboardInterrupt:

                break

exit()