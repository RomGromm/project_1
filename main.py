#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.iodevices import I2CDevice

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
motorb = Motor(Port.B)
motorc = Motor(Port.C)
compass = I2CDevice(Port.S1, 0x01)

compass.write(reg = 0x41, data = b'\0x43')
motorb.dc(15)
motorc.dc(-15)  
ev3.speaker.beep()
wait(20000)
ev3.speaker.beep()
compass.write(reg = 0x41, data = b'\0x00')
motorb.stop()
motorc.stop()
wait(1000)
while True:
    result, = compass.read(reg = 0x42, length = 1)
    ev3.screen.clear()
    ev3.screen.print(result * 2)
    wait(10)
# Write your program here.
