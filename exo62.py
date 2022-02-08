from sense_hat import SenseHat 
sense = SenseHat()
"""
A magnetometer is an instrument that measures magnetization of magnetic material like a ferromagnet, or
the direction, strength, or the relative change of a magnetic field at a particular location.
"""
sense.set_imu_config(False, False, True)
"""
gyro, accel, magne
"""
while True:
	north = sense.get_compass()
	print("North: %s" % north)
