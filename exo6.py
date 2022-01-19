#!/usr/bin/python
from sense_hat import SenseHat
import time
"""
A magnetometer is a device used to measure the intensity or direction of a magnetic field, or the magnetization of a sample.
set_imu_config(compass_enabled, gyro_enabled, accel_enabled) 
"""
sense = SenseHat()
sense.set_imu_config(True, False, False)  #Magnetometer only
while True:
    north = sense.get_compass()
    print("North : {}".format(north))
    #Gets the raw x, y and z axis magnetometer data
    raw = sense.get_compass_raw()
    print("------------------------------------")
    print("x: {x}, y: {y}, z: {z}".format(**raw))
    print("------------------------------------")
    print("------------------------------------")
    time.sleep(2)


"""
calibration is needed 
source : https://raspberrytips.com/sense-hat-tutorial-2/
"""

